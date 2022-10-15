
from PIL import Image
from PIL import ImageGrab

def get_result(msg):
   
   myimage = ImageGrab.grab(bbox=  (813,93,931,120))   
   myimage.save('pricer.png')

get_result('hello')