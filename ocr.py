import image_reader
import utilsdb

utils = utilsdb.utilsDB()

r = image_reader.Image_Reader()
url = 'https://cdn.discordapp.com/attachments/1069415705524588564/1204278469232693278/Screenshot_20240205_211126_Strava.jpg?ex=65d426b9&is=65c1b1b9&hm=9af6e4aa70a2a400548be58b9a6d7e7bdf1a272778a34f56c8222b65c840001f&'
lst = r.readImage(url)
distance = utils.getPoints(lst)
print(utils.convertMetric(distance))