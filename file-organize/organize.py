import os
from pathlib import Path

SUBDIR = {
        "DOCUMENTS":[".pdf",".docx",".txt"],
        "AUDIO":[".m4a",".m4b",".mp3"],
        "IMAGES":[".jpg",".jpeg",".png"]
        }
def pickDir(value):
    for category, ekstensi in SUBDIR.items():
        for suffix in ekstensi:
            if suffix == value:
                return category

def organizeDir():
    for item in os.scandir():
        if item.is_dir():
                continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDir(filetype)
        if directory == None:
            continue
        directoryPath = Path(directory)
        print(directoryPath)
        if directoryPath.is_dir() != True:
                directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

