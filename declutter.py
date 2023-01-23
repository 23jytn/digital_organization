import os
import shutil
import sys

home = os.path.expanduser('~')+'/'
try:
    path = sys.argv[1]
    if not path.endswith('/'):
        path += '/'
except IndexError:
    path = home # in the specified path
if os.path.exists(path):
    print("PATH Exists - "+path)
else:
    print("PATH Doesn't exist")

obj = os.scandir(path)

audio_folder = home+'Music/'
image_folder = home+'Pictures/'
video_folder = home+'Videos/'
document_folder = home+'Documents/'
package_folder = home+'Packages/'

audio_files = (
    '.mp3'
)
image_files = (
    '.png',
    '.PNG',
    '.jpg',
    '.jpeg'
)
video_files = (
    '.mp4',
    '.mov',
    '.wmv',
    '.avi',
    '.avchd',
    '.flv',
    '.f4v',
    '.swf',
    '.mkv',
    '.webm',
    '.html5'
)
document_files = (
    '.pdf',
    '.ppt',
    '.doc',
    '.docx',
    '.docx',
    '.xlsx',
    '.csv',
    '.drawio',
)
package_files = (
    '.tar',
    '.tar.gz',
    '.tar.xz',
    '.zip',
    '.iso',
    '.whl',
    '.deb'
)

for entry in obj :
    if entry.is_file():
        if entry.name.endswith(image_files):
            shutil.move(path+entry.name, image_folder+entry.name)
        elif entry.name.endswith(audio_files):
            shutil.move(path+entry.name, audio_folder+entry.name)
        elif entry.name.endswith(video_files):
            shutil.move(path+entry.name, video_folder+entry.name)
        elif entry.name.endswith(document_files):
            shutil.move(path+entry.name, document_folder+entry.name)
        elif entry.name.endswith(package_files):
            shutil.move(path+entry.name, package_folder+entry.name)
    elif entry.is_dir():
        pass

obj.close()
