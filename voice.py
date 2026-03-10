# voice.py – TTS with edge-tts + pygame playback

import threading
import queue
import time
import speech_recognition as sr
import edge_tts
import os
import tempfile
import warnings
import logging
import sys

# ────────────────────────────────────────────────
# SILENT STARTUP
# ────────────────────────────────────────────────
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
warnings.filterwarnings("ignore", module=r"pygame.*")
logging.getLogger('pygame').setLevel(logging.CRITICAL + 10)

import pygame 

try:
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2048)
except Exception as e:
    print(f"Critical: mixer init failed → {e}")
    sys.exit(1)

# ────────────────────────────────────────────────
# CONFIG
# ────────────────────────────────────────────────
WAKE_WORD         = "friday are you there"
ASSISTANT_NAME    = "Friday"

LISTEN_TIMEOUT    = 5.0
PHRASE_TIME_LIMIT = 12.0

VOICE = "en-GB-LibbyNeural" 

from commands import process_command 

# ────────────────────────────────────────────────
class VoiceAssistant:
    def __init__(self):
        self.shutdown_event = threading.Event()
        self.speech_queue  = queue.Queue(maxsize=8)
        self.running       = False
        self.tts_thread    = None
        self.ASSISTANT_NAME = ASSISTANT_NAME

    def speak(self, text: str):
        if not text or not text.strip():
            return
        print(f"{self.ASSISTANT_NAME}: {text}")
        try:
            self.speech_queue.put_nowait(text)
        except queue.Full:
            pass 

    def tts_worker(self):
        while not self.shutdown_event.is_set():
            try:
                text = self.speech_queue.get(timeout=1.5)
                if text is None:
                    break

                try:
                    communicate = edge_tts.Communicate(text, VOICE)
                    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
                        tmp_path = tmp.name
                        communicate.save_sync(tmp_path)
                except Exception as e:
                    print(f"TTS failed: {e}")
                    self.speech_queue.task_done()
                    continue

                try:
                    pygame.mixer.music.load(tmp_path)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() and not self.shutdown_event.is_set():
                        time.sleep(0.08)
                    pygame.mixer.music.unload()
                except Exception as e:
                    print(f"Playback failed: {e}")

                try:
                    os.remove(tmp_path)
                except:
                    pass

                self.speech_queue.task_done()

            except queue.Empty:
                continue
            except Exception:
                pass

    def start_tts(self):
        if self.tts_thread is None or not self.tts_thread.is_alive():
            self.tts_thread = threading.Thread(target=self.tts_worker, daemon=True)
            self.tts_thread.start()

    def run_listening_loop(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        try:
            with microphone as source:
                # ─── SENSITIVITY SETTINGS ──────────────────────────
                recognizer.energy_threshold = 200
                recognizer.dynamic_energy_threshold = True
                recognizer.dynamic_energy_adjustment_damping = 0.10   
                recognizer.dynamic_energy_ratio = 1.3                 
                recognizer.adjust_for_ambient_noise(source, duration=1.0)
             #  print("Microphone calibrated (increased sensitivity)")
        except Exception as e:
            print(f"Microphone init failed: {e}")
            return

        is_active = False

        while not self.shutdown_event.is_set() and self.running:
            try:
                with microphone as source:
                    audio = recognizer.listen(
                        source,
                        timeout=LISTEN_TIMEOUT,
                        phrase_time_limit=PHRASE_TIME_LIMIT
                    )

                text = recognizer.recognize_google(audio).strip().lower()
                if not text:
                    continue

                if not is_active:
                    if WAKE_WORD in text:
                        is_active = True
                        self.speak("At your service, sir!")
                    continue

                print(f"You: {text}")

                command = text.replace(WAKE_WORD, "").strip()
                if not command:
                    continue

                response = process_command(command)
                self.speak(response)

                if any(keyword in command for keyword in [
                    "bye", "goodbye", "quit", "exit", "stop", "shut down", "later", "abort now", "sign off"
                ]):
                    self.speak("Goodbye, sir!")
                    self.running = False
                    self.shutdown_event.set()
                    break

            except (sr.WaitTimeoutError, sr.UnknownValueError):
                continue
            except sr.RequestError as e:
                print(f"Google Speech-to-Text error: {e}")
                time.sleep(1.2)
            except Exception as e:
                print(f"Unexpected error in listening loop: {e}")
                time.sleep(0.9)

# ────────────────────────────────────────────────
# Control functions
# ────────────────────────────────────────────────
def start_friday(assistant: VoiceAssistant):
    assistant.start_tts()
    assistant.running = True
    voice_thread = threading.Thread(target=assistant.run_listening_loop, daemon=True)
    voice_thread.start()
    print(f"{assistant.ASSISTANT_NAME} is up and ready!")
    return voice_thread

def stop_friday(assistant: VoiceAssistant, voice_thread):
    assistant.running = False
    assistant.shutdown_event.set()
    try:
        assistant.speech_queue.put_nowait(None)
    except:
        pass
    if voice_thread and voice_thread.is_alive():
        voice_thread.join(timeout=5.0)
    if assistant.tts_thread and assistant.tts_thread.is_alive():
        assistant.tts_thread.join(timeout=4.0)
    print("Friday has shut down.")

# ────────────────────────────────────────────────
if __name__ == "__main__":
    assistant = VoiceAssistant()
    thread = start_friday(assistant)
    try:
        thread.join()
    except KeyboardInterrupt:
        print("\nShutting down via Ctrl+C...")
        stop_friday(assistant, thread)