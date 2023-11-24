from util.moveFile import moveFile
import json
import os

def scanfolder():
    f = open('file-organizer.settings.json')
    data = json.load(f)
    source = data["dirs"]["source"]
    target = data["dirs"]["target"]
    
    if os.path.exists(source) == False:
        os.makedirs(source)
    
    with os.scandir(source) as entries:
        for entry in entries:
            if entry.is_file():
                moveFile(entry.name,source,target)
    
if __name__ == "__main__":
    scanfolder()
