# friday.py
import time
from voice import VoiceAssistant, start_friday, stop_friday

def main():
    assistant = VoiceAssistant()
    voice_thread = start_friday(assistant)

    try:
        while assistant.running:
            time.sleep(0.6)
    except KeyboardInterrupt:
        pass
    finally:
        stop_friday(assistant, voice_thread)

if __name__ == "__main__":
    main()