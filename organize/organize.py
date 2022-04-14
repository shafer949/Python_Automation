import os
from pathlib import Path

#Setup our directories and filetype mapping
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO":['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

#Pick the directory the file should be in based on the filetype
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC' #If filetype doesn't exist in our dictionary

#Organize the file within the correct directory based on the filetype
def organizeDirectory():
    for item in os.scandir():
        #Skip if item is a directory
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        #If the directory the file maps to doesn't exists, create a new directory with that name
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        #Move the file to the correct directory
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()

#cd into the organize directory then
#Run py organize.py in the terminal (Windows)
#Notice the list of files have been moved to directories based on their filetype.