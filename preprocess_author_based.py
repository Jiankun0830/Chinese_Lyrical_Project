typeName = "songci"
filepath = "./dataset/" + typeName + "/"
filesavepath = "./dataset/" + typeName + "/author_based/"
filename = filepath + typeName + ".txt"

database = {}


file = open(filename, "r", encoding="UTF-8")
for line in file:  # every line is a poem
    title, author, poem = line.strip().split("::")  # get title and poem
    if author not in database:
        database[author] = []
    database[author].append(poem+"\n")

file.close()



for author in database:
    try:
        saveFile_content = open(filesavepath + typeName + "_"+author+".txt", "w", encoding="UTF-8")
    except:
        continue
    for poem in database[author]:
        saveFile_content.write(poem + "\n")
    saveFile_content.close()

