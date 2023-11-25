from util.moveFile import moveFile
import json
import os

def scanfolder():
    fos = open('file-organizer.settings.json')
    fosData = json.load(fos)
    source = fosData["dirs"]["source"]
    target = fosData["dirs"]["target"]
    
    dirMap = open('dirMapping.json')
    dirMapData = json.load(dirMap)

    if os.path.exists(source) == False:
        os.makedirs(source)
    
    with os.scandir(source) as entries:
        for entry in entries:
            if entry.is_file():
                print (entry.name)
                moveFile(entry.name,source,target,dirMapData['dirMap'])
    
if __name__ == "__main__":
    scanfolder()
