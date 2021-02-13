from scrapperImage.ScrapperImage import ScrapperImage

class BusinessLayer:
    keyword= ''
    fileLoc=''
    image_name=''
    header=''


    def downloadImages(keyword, header):
        imgScrapper= ScrapperImage
        url= imgScrapper.createImageUrl(keyword)
        rawHtml= imgScrapper.scrap_html_data(url,header)
        imageUrlList= imgScrapper.getImageUrlList(rawHtml)
        masterListOfImages = imgScrapper.downloadImagesFromURL(imageURLList, keyword, header)

        return masterListOfImages
