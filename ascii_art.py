from rich.console import Console
from rich.text import Text
import random

class ASCIIPet:
    PETS = {
        "happy": "(^_^)",
        "neutral": "(•_•)",
        "sad": "(T_T)"
    }

    def __init__(self):
        self.console = Console()
        self.mood = "neutral"

    def set_mood(self, mood):
        if mood in self.PETS:
            self.mood = mood

    def display(self):
        pet_art = self.PETS.get(self.mood, "(•_•)")
        self.console.print(f"[bold cyan]{pet_art}[/bold cyan]")

    def speak(self, message):
        self.console.print(Text(message, style="bold yellow"))

# Example usage
if __name__ == "__main__":
    pet = ASCIIPet()
    pet.display()
    pet.speak("Keep coding, you're doing great!")
