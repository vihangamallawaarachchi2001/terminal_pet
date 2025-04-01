from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class ActivityTracker(FileSystemEventHandler):
    def __init__(self, pet):
        self.pet = pet

    def on_modified(self, event):
        if event.is_directory:
            return
        self.pet.set_mood("happy")
        self.pet.speak(f"You modified {event.src_path}!")

if __name__ == "__main__":
    from pet import ASCIIPet

    pet = ASCIIPet()
    event_handler = ActivityTracker(pet)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
