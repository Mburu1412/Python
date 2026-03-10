# commands.py
from datetime import datetime
import random
import re
import requests

ASSISTANT_NAME = "Friday"

# ────────────────────────────────────────────────
# Personality & Time-aware elements
# ────────────────────────────────────────────────
def get_time_of_day():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    else:
        return "evening"

GREETINGS = [
    lambda: f"Good {get_time_of_day()}, sir! Ready when you are.",
    lambda: f"Hey! Good {get_time_of_day()}. How can Friday help today?",
    lambda: f"Good {get_time_of_day().capitalize()} sir. What's the mission?",
    lambda: f"{get_time_of_day().capitalize()} vibes detected. What's up?",
]

THANKS_REPLIES = [
    "You're welcome — anytime, sir.",
    "My pleasure!",
    "No problem at all 😎",
    "Glad I could help.",
]

MOOD_REPLIES = [
    f"Feeling sharp this {get_time_of_day()}. How about you?",
    "All systems green and caffeinated (digitally). You good?",
    "Running at 100%. What's on your mind?",
]

GOODBYE_REPLIES = [
    "Goodbye, sir. Call me when you need me.",
    f"See you later — enjoy your {get_time_of_day()}!",
    "Friday signing off. Stay awesome.",
    "Catch you next time, sir.",
]

JOKES = [
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why do programmers prefer dark mode? Light attracts bugs.",
    "I told my computer I needed a break... now it's sending me KitKat ads.",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why was the math book sad? It had too many problems.",
]

FUN_FACTS = [
    "Octopuses have three hearts: two pump blood to the gills, one to the body.",
    "Honey never spoils — pots over 3,000 years old are still edible.",
    "Bananas are berries, but strawberries aren't (botanically speaking).",
    "The Eiffel Tower grows 15 cm taller in summer due to thermal expansion.",
    "A flock of crows is called a 'murder'.",
]

def matches_any(text: str, keywords: list[str]) -> bool:
    """Case-insensitive substring match"""
    t = text.lower().strip()
    return any(kw.lower() in t for kw in keywords)


def safe_eval_math(expression: str) -> str:
    """Safely evaluate simple arithmetic (no dangerous code)"""
    try:
        if not re.match(r'^[\d\s\+\-\*\/\(\)\.xX÷]+$', expression):
            return "Sorry, that's not a valid math expression I can handle yet."
        
        expr = expression.replace('x', '*').replace('X', '*').replace('÷', '/').replace('times', '*').replace('divided by', '/')
        result = eval(expr, {"__builtins__": {}}, {})
        return f"{expression} = {result}"
    except Exception:
        return "Couldn't calculate that. Try e.g. '25 times 4' or '15 + 7 - 3'."


def get_weather(city: str = "Nairobi") -> str:
    """Current weather via free Open-Meteo API (Nairobi default)"""
    try:
        # Nairobi coordinates (lat, lon)
        url = "https://api.open-meteo.com/v1/forecast?latitude=-1.286389&longitude=36.817223&current=temperature_2m,relative_humidity_2m,weather_code&timezone=Africa/Nairobi"
        r = requests.get(url, timeout=6)
        data = r.json()
        
        if "current" not in data:
            return "Weather service is taking a quick nap. Try again soon!"
        
        temp = data["current"]["temperature_2m"]
        hum = data["current"]["relative_humidity_2m"]
        code = data["current"]["weather_code"]
        
        desc = {
            0: "clear sky", 1: "mainly clear", 2: "partly cloudy", 3: "overcast",
            45: "fog", 51: "light drizzle", 61: "light rain", 71: "light snow",
            80: "rain showers", 95: "thunderstorm", 99: "heavy thunderstorm"
        }.get(code, "conditions I can't quite describe yet")
        
        return f"In {city} right now: {temp}°C, {hum}% humidity, {desc}."
    except Exception:
        return "Couldn't reach the weather service. Network hiccup maybe?"


def process_command(text: str) -> str:
    """
    Process the cleaned user command text and return only the response string.
    Do NOT modify assistant state here (no self.running, no shutdown_event).
    """
    t = text.lower().strip()

    # ──────────────────────────────────────────────────────────────
    # Exit / shutdown commands
    # ──────────────────────────────────────────────────────────────
    if matches_any(t, ["bye", "goodbye", "quit", "exit", "stop", "shut down", "later", "abort now", "sign off"]):
        return random.choice(GOODBYE_REPLIES)

    # ──────────────────────────────────────────────────────────────
    # Greetings (time-aware)
    # ──────────────────────────────────────────────────────────────
    if matches_any(t, ["hello", "hi", "hey", "morning", "evening", "sup", "yo", "what's up", "howdy"]):
        return random.choice(GREETINGS)()

    # ──────────────────────────────────────────────────────────────
    # Thanks
    # ──────────────────────────────────────────────────────────────
    if matches_any(t, ["thanks", "thank you", "thx", "ty", "appreciate", "cheers"]):
        return random.choice(THANKS_REPLIES)

    # ──────────────────────────────────────────────────────────────
    # How are you
    # ──────────────────────────────────────────────────────────────
    if matches_any(t, ["how are you", "how r u", "how's it going", "status", "you good", "how you doing"]):
        return random.choice(MOOD_REPLIES)

    # ──────────────────────────────────────────────────────────────
    # Time & Date
    # ──────────────────────────────────────────────────────────────
    if matches_any(t, ["time", "what time", "current time", "tell me the time"]):
        return f"The time is {datetime.now().strftime('%H:%M')}."

    if matches_any(t, ["date", "what date", "today's date", "what day"]):
        return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."

    # ──────────────────────────────────────────────────────────────
    # Weather
    # ──────────────────────────────────────────────────────────────
    if matches_any(t, ["weather", "how's the weather", "forecast", "temperature", "how hot", "how cold"]):
        return get_weather()

    # ──────────────────────────────────────────────────────────────
    # Math / calculate
    # ──────────────────────────────────────────────────────────────
    if matches_any(t, ["calculate", "what is", "compute", "math"]):
        expr_match = re.search(r'(?:calculate|what is|compute)\s+(.+?)(?:\s*$|\s+please)', t, re.IGNORECASE)
        if expr_match:
            return safe_eval_math(expr_match.group(1).strip())
        return "Tell me what to calculate — e.g. 'calculate 42 times 17'"


    # ──────────────────────────────────────────────────────────────
    # Joke / Fun fact
    # ──────────────────────────────────────────────────────────────
    if matches_any(t, ["joke", "tell me a joke", "something funny", "make me laugh"]):
        return random.choice(JOKES)

    if matches_any(t, ["fact", "fun fact", "tell me a fact", "something interesting"]):
        return random.choice(FUN_FACTS)

    # ──────────────────────────────────────────────────────────────
    # Who are you
    # ──────────────────────────────────────────────────────────────
    if matches_any(t, ["who are you", "what's your name", "introduce yourself"]):
        return f"I'm {ASSISTANT_NAME}, your voice assistant. Always ready to help."

    # ──────────────────────────────────────────────────────────────
    # Fallback
    # ──────────────────────────────────────────────────────────────
    return random.choice([
        f"Hmm… '{text}' — could you say that again?",
        f"Got '{text}'. Not quite sure yet — what did you mean?",
        f"Interesting… '{text}'. Give me a clearer command?",
        f"I'm still learning that one. Try something else?",
    ])