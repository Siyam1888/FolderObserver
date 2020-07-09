import time
from transfer import automated_file_transfer
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from termcolor import colored

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = False # windows file system is case insensitive
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

path = "C:\\Users\\Administrator\\Downloads"


def on_created(event):
    split_file_path = event.src_path.split('\\')
    name = split_file_path[-1]
    print(colored(f"(-->CREATED)~ hey, {name} has been created!", "green"))

def on_deleted(event):
    split_file_path = event.src_path.split('\\')
    name = split_file_path[-1]
    print(colored(f"(-->DELETED)~ hey, Someone deleted {name}!!!", "red"))

def on_modified(event):
    split_file_path = event.src_path.split('\\')
    name = split_file_path[-1]
    print(colored(f"(-->MODIFIED)~ hey buddy, {name} has been modified", "cyan"))
    time.sleep(2)
    automated_file_transfer(path)

def on_moved(event):
    split_file_path = event.src_path.split('\\')
    name = split_file_path[-1]
    print(colored(f"(--->MOVED)~ hey buddy, {name} has been moved", "magenta"))
    automated_file_transfer(path)



    


my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved

my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=True)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
