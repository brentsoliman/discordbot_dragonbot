import easyocr
import download_image


class Image_Reader:
    
    
    def readImage(self,url):
        dimage = download_image.Download_Image()
        
        dimage.getImage(url)
        reader = easyocr.Reader(['en'])
        result = reader.readtext('img.jpg')
        #word = ' '.join(result)
        dimage.removeImage()

        return result