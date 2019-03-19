import json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

name = "bill"
# Example
data = {}
data[f'name'] = f'{name}'

writeToJSONFile('./','file-name',data)