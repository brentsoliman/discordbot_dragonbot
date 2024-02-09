import requests
import os

class Download_Image():
    
    def getImage(self,url):
        data = requests.get(url).content
        # Opening a new file named img with extension .jpg
        # This file would store the data of the image file
        f = open('img.jpg','wb')
        
        # Storing the image data inside the data variable to the file
        f.write(data)
        f.close()
        
    def removeImage(self):
        os.remove('./img.jpg')