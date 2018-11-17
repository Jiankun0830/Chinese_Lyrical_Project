from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

typeName = "songci"
filepath = "./dataset/"+typeName+"/famous_authors_words"

SUTD_mask = np.array(Image.open("SUTD.png"))


def generateWordCloud(filename):
    file = open(filename, encoding="utf-8")
    savafile = filename[0:-10]+".jpg"

    print(savafile)
    text=file.read()
    wordcloud=WordCloud(font_path= "C:/Windows/Fonts/simfang.ttf",
    background_color="white",width=600,
    height=300,max_words=50).generate(text)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(savafile)
    plt.show()
    plt.close("all")

def eachFile(filePath):
    file_name_list = os.listdir(filePath)
    for filename in file_name_list:
        newFileName = filePath + "/" + filename
        generateWordCloud(newFileName)

if __name__ == '__main__':
    eachFile(filepath)
