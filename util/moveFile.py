from .fileExtenstionExtractor import fileExtenstionExtractor
import shutil
import os

def moveFile(file, source, dest,dirMapDictionary):
    
    for dirname ,fileExtList in dirMapDictionary.items():
        fxt = fileExtenstionExtractor(file)
        if (fxt.pop()) in fileExtList:
            if os.path.exists(dest + "/" + dirname)==False:
                os.makedirs(dest + "/" + dirname)
            if os.path.isfile(dest + "/" + dirname + "/" + file)==False:
                shutil.move(source + "/" + file, dest + "/" + dirname + "/" + file)
            