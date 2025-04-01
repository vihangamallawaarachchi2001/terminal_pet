import time
from ascii_art import ASCIIPet
from activity_tracker import ActivityTracker
from motivator import Motivator
from git_tracker import GitTracker
from watchdog.observers import Observer

def main():
    pet = ASCIIPet()
    git_tracker = GitTracker()
    observer = Observer()
    observer.schedule(ActivityTracker(pet), path=".", recursive=True)
    observer.start()

    pet.display()
    pet.speak("Hello! I'm your coding companion!")

    try:
        while True:
            time.sleep(10)
            pet.set_mood("neutral")
            commits_today = git_tracker.get_commit_count_today()
            if commits_today > 0:
                pet.set_mood("happy")
                pet.speak(f"Great job! {commits_today} commits today!")
            else:
                pet.set_mood("sad")
                pet.speak("No commits yet... Keep going!")
            pet.display()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
