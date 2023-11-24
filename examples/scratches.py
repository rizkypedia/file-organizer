print ("dict with array")

def getFileExension(filename):
    fileExtension = filename.split(".")
    return fileExtension[-1:]

dict = {
    "videos":["avi","mpeg","mpg","m4v"],
    "images":["jpg","jpeg","gif"]
}
filename = "test.avi"

for x ,y in dict.items():
    fxt = getFileExension(filename)
    if fxt.pop() in y:
        print(x)