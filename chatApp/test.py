def writeFile(str):
    text_file = open("Output.txt", "w")
    text_file.write(str)
    text_file.close()

def readFile():
    text_file = open("Output.txt", "r")
    lines = text_file.read().split(',')
    return lines[0]
    text_file.close()       

writeFile("xx") 

readFile()   