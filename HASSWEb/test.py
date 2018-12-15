# -*- coding: UTF-8 -*-
from flask import Flask,render_template,flash,redirect,url_for,session,logging,request,session,escape
import os
from io import BytesIO
import sys
from importlib import reload

app = Flask(__name__)
app.secret_key = '123'



@app.route('/',methods=['GET','POST'])
def home():
    return render_template('lyrical.html')

@app.route('/word_cloud',methods=['GET','POST'])
def wordcloud():
	return render_template('word_cloud.html')


@app.route('/tang',methods=['GET','POST'])
def tang():
	#to avoid mac ds_store
	names = os.listdir(os.path.join(app.static_folder, 'tangshi'))
	if ".DS_Store" in names:
		names.remove(".DS_Store")
	return render_template('tang.html',rows=names)

@app.route('/songshi',methods=['GET','POST'])
def songshi():
	#to avoid mac ds_store
	names = os.listdir(os.path.join(app.static_folder, 'songshi'))
	if ".DS_Store" in names:
		names.remove(".DS_Store")
	return render_template('songshi.html',rows=names)

@app.route('/songci',methods=['GET','POST'])
def songci():
	#to avoid mac ds_store
	names = os.listdir(os.path.join(app.static_folder, 'songci'))

	return render_template('songci.html',rows=names)

@app.route('/shijing',methods=['GET','POST'])
def shijing():
	#to avoid mac ds_store
	names = os.listdir(os.path.join(app.static_folder, 'shijing'))
	if ".DS_Store" in names:
		names.remove(".DS_Store")
	return render_template('shijing.html',rows=names)
@app.route('/styletrans',methods=['GET','POST'])
def styletrans():
	return render_template("styletrans.html")
@app.route('/transsutd',methods=['GET','POST'])
def transsutd():
	return render_template("transsutd.html")
@app.route('/transmarina',methods=['GET','POST'])
def transmarina():
	return render_template('transmarina.html')

@app.route('/reference',methods=['GET','POST'])
def reference():
	return render_template('col3.html')




@app.route('/pic_1',methods=['GET','POST'])
def pic_1():
	return render_template('pic_1.html')
@app.route('/pic_2',methods=['GET','POST'])
def pic_2():
	return render_template('pic_2.html')
@app.route('/pic_3',methods=['GET','POST'])
def pic_3():
	return render_template('pic_3.html')
@app.route('/pic_4',methods=['GET','POST'])
def pic_4():
	return render_template('pic_4.html')

	
@app.route('/pic_5',methods=['GET','POST'])
def pic_5():
	return render_template('pic_5.html')
@app.route('/pic_6',methods=['GET','POST'])
def pic_6():
	return render_template('pic_6.html')
@app.route('/pic_7',methods=['GET','POST'])
def pic_7():
	return render_template('pic_7.html')
@app.route('/pic_8',methods=['GET','POST'])
def pic_8():
	return render_template('pic_8.html')

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=8000,debug=True)


