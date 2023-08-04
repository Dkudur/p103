import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemHandler

from_dir = "C:/Users/Anike/Downloads"

class FileEventHandler(FileSystemHandler):
    def on_created(self , event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self , event):
        print(f"Oops! Someone deleted {event.src_path}!")

    def on_moved(self , event):
        print(f"What? Someone moved {event.src_path}!")

    def on_modified(self , event):
        print(f"Oh, someone changed {event.src_path}!")






eventHandler = FileEventHandler()

observer = Observer()

observer.schedule(eventHandler , from_dir , recursive = True)
observer.start()



try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()