typeName = "poetryTang"
filepath = "./dataset/" + typeName + "/"
filename = filepath + typeName + ".txt"


saveFile_author = open(filepath + typeName + "_author.txt", "w", encoding="UTF-8")
saveFile_content = open(filepath + typeName + "_content.txt", "w", encoding="UTF-8")

file = open(filename, "r", encoding="UTF-8")
for line in file:  # every line is a poem
    title, author, poem = line.strip().split("::")  # get title and poem
    saveFile_content.write(poem+"\n")
    saveFile_author.write(author+"\n")

saveFile_author.close()
saveFile_content.close()
