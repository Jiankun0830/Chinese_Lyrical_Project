import jieba
import os

typeName =  "songci"
filePath = "./dataset/"+typeName+"/Famous_authors"
savePath = "./dataset/"+typeName+"/Famous_authors_words"

def process_file(fileName):
    file = open(fileName,"r",encoding="utf-8")
    poem_words = []
    for line in file:
        seg_list =jieba.cut(line,  cut_all= True)
        words = " ".join(seg_list)
        poem_words.append(words)
    file.close()

    saveFileName = fileName[0:-4]
    saveFileName += "_words.txt"
    print(saveFileName)
    save_file = open(saveFileName,"w",encoding="utf-8")
    for words in poem_words:
        save_file.write(words)
    save_file.close()

def eachFile(filePath):
    file_name_list = os.listdir(filePath)
    for filename in file_name_list:
        newFileName = filePath + "/" + filename
        process_file(newFileName)

if __name__ == '__main__':
    eachFile(filePath)
