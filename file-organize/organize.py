import os
from pathlib import Path

# define the file categories with dictionary
SUBDIR = {
        "01 DOCUMENTS":['.txt','.xls','.pdf','.docx'],
        "02 AUDIO":[".m4a",".mp3"],
        "03 VIDEO":['.mp4'],
        "04 IMAGES":[".jpg",".jpeg",".png",".svg"]
        }

def pickDir(value):
    '''
    value: str contain extension of the file.
    return name of the category who defined before.
    e.g. value = '.pdf' so the function will return DOCUMENTS.
    '''
    for category, ekstensi in SUBDIR.items():
        for suffix in ekstensi:
            if suffix == value:
                return category

def scanRecurse(baseDir):
    '''
    baseDir: str of directory for scan file.
    this function will scan file recursively.
    '''
    for entry in os.scandir(baseDir):
        if entry.is_file():
            yield entry
        else:
            yield from scanRecurse(entry.path)

def scanSuffix():
    '''
    this function will scan any file recursively and collect extention of file, count it and return into a dictionary.

    '''
    suffixDic={}

    for item in scanRecurse('./'):
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        if fileType in suffixDic.keys():
            suffixDic[fileType] += 1
        else:
            suffixDic[fileType] = 1
    return suffixDic


def organizeDir():
    '''
    this function will scan any files in the same directory, and then
    look at every extension of files and move that file to the exact category from calling the pickDir function.
    
    
    '''
    for item in scanRecurse('./'):
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        print(filePath)
        directory = pickDir(fileType)

        #just put into OTHERS, if the file extension not defined, and put .py file in the base directory.
        if directory == None:
            if fileType == '.py' :
                directory = './'
            else:
                directory = "05 OTHERS"

        directoryPath = Path(directory)

        #make new directory if the category's directory not found.
        if directoryPath.is_dir() == False:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(item.name))


def plotBarExtension():

    import matplotlib.pyplot as plt
    import numpy as np


    suffix = scanSuffix()

    #sort dict by the value
    suffixTuple = [(value, key) for (key,value) in suffix.items()]
    sortTuple = sorted(suffixTuple, reverse=True)
    suffix = dict([(k,v) for v,k in sortTuple])

    fig = plt.figure(figsize = (20,10))
    axes = fig.add_subplot(111)

    x,y = list(suffix.keys()),list(suffix.values())
    pos = np.arange(len(x))
    axes.bar(pos,y, log=1)
    axes.set_xticks(pos)
    axes.set_xticklabels(x, rotation=90)
    plt.show()


organizeDir()

#plot extension (optional)
plotBarExtension()
