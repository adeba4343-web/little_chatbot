
import re
import random

def try_math(user_input):

    if re.match(r'^[0-9\+\-\*/\s]+$', user_input):
        try:
            return str(eval(user_input))
        except Exception:
            return "Hmm, I couldn't calculate that 🤔"
    return None


jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "Why did the Python go to school? Because it wanted to be a boa teacher! 🐍",
    "I would tell you a UDP joke, but you might not get it. 😉",
]

def random_joke():
    return random.choice(jokes)
