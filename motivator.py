import random

class Motivator:
    MESSAGES = [
        "You're making progress!",
        "Coding every day builds habits!",
        "One step closer to mastery!",
        "Break your problem down, you got this!"
    ]

    @staticmethod
    def get_message():
        return random.choice(Motivator.MESSAGES)

if __name__ == "__main__":
    print(Motivator.get_message())
