

from flask_cors import CORS,cross_origin
from flask import Flask, render_template, request,jsonify
import os
from scrapperImage.ScrapperImage import ScrapperImage
from businesslayer.BusinessLayerUtil import BusinessLayer


app = Flask(__name__)


@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/showImages')
@cross_origin()
def displayImages():
    lists= os.listdir('static')
    print(lists)

    try:
        if (len(lists)>0):
            return render_template('showImage.html',user_images=lists)
        else:
            return 'images are not present'

    except Exception as e:
         print("No images found",e)
         return "Please try with a different search keyword"


@app.route('/searchImages',methods= ['Get','POST'])
def searchImages():
    if request.method== 'POST':
        search_term = request.form['keyword']
    else:
        print('Please enter something')

    imagescrapperutil= BusinessLayer
    imagescrapper= ScrapperImage()
    list_images= os.listdir('static')
    imagescrapper.delete_images(list_images)

    image_name= search_term.split()
    image_name="+".join(image_name)

    header= { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36 '}


    lst_images= imagescrapperutil.downloadImages(search_term,header)

    return displayImages()

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8000,debug=True)

