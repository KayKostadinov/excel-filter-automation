import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from FileFilter import FileFilter as ff


class Watcher:

    def __init__(self, path):
        self.observer = Observer()
        self.directory = path

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.directory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    def on_any_event(self, event):
        # if event.is_directory:
        #     return None
        if event.event_type == 'created':
            path = event.src_path
            name = path.split('/')[-1]
            name, file_type = name.split('.')
            # test
            print({'name': name, 'type': file_type})

            # filter document
            # TODO: check for correct name of file
            if name == 'Book2':
                ff.awaiting_name(file_path=path, file_type=file_type)
