from Watcher import Watcher
import os

downloads_path = os.path.expanduser('~/Downloads')
# desktop_path = os.path.expanduser('~/Desktop')

# enable watcher
watcher = Watcher(downloads_path)
watcher.run()



