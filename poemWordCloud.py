from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

typeName = "poetrySong"
type = "topics"
filename = "./dataset/"+ typeName + "/" + typeName + "_" + type+ ".txt"
file =  open(filename ,encoding="utf-8")

SUTD_mask = np.array(Image.open("SUTD.png"))
text=file.read()
wordcloud=WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",mask = SUTD_mask,
background_color="white",width=600,
height=300,max_words=50).generate(text)
#image=wordcloud.to_image()
#image.show()

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
