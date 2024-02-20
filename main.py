from util.moveFile import moveFile
import json
import os

def scanfolder():
    
    with open('file-organizer.settings.json') as organizerSettings:
        fosData = json.load(organizerSettings)
    
    source = fosData["dirs"]["source"]
    target = fosData["dirs"]["target"]
        
    with open('dirMapping.json') as dirMap:
        dirMapData = json.load(dirMap)

    if os.path.exists(source) == False:
        os.makedirs(source)
    
    with os.scandir(source) as entries:
        for entry in entries:
            if entry.is_file():
                print (f'{entry.name}')
                moveFile(entry.name,source,target,dirMapData['dirMap'])
    
if __name__ == "__main__":
    print("Scanfolder\n")
    scanfolder()
