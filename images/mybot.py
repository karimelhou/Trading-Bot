from ast import If
from time import sleep
import pyautogui as pt 
import pyperclip as pc
from PIL import Image
from PIL import ImageGrab
from pytesseract import pytesseract
from PIL import Image
import cv2
import os
from time import gmtime, strftime
import time
import sys


def my_program(msg):
 #sleep(1)
 res3 = ''
 act = 2
 
 #<<--------------Function to detect the mt4 notificatiom ------------------->>

 def locate_notification(mesg):
   locate = pt.locateOnScreen('images/ring.png' , confidence =.7)
   while locate == None :
      sleep(1)
      locate = pt.locateOnScreen('images/ring.png')
   
   pt.moveTo(locate , duration=.2)
 #locate_notification('hello')


 #<<--------------Function to take screenshot of the notificatiom ------------------->>

 ##function to take screenshot of the alert
 def take_screenshot(mymsg):
   image = ImageGrab.grab(bbox=  (0,50,1500,200))   #size ||||
   image.save('sc.png')

 #take_screenshot('hello')
   
 #<<--------------Function to extract text from notificatiom screenshot ------------------->>

 def extract_text(msg):
   #img = Image.open('images/readpic2.png')
   img2 = cv2.imread('sc.png')

   #res = pytesseract.image_to_string(img)
   res2 = pytesseract.image_to_string(img2)
   #print(res)
   print(res2)
   global res3 
   res3 = res2[res2.find("(")+1:res2.find(",")]
   print(res3)
   global act

   if res2.find("SELL")!=-1:
       print("LETS SELL")
       act = 1

   else:
       print("LETS BUY")
       act = 0

   print(act)

 extract_text('hello')

 #<<--------------Function to open webbrowser ------------------->>

 def go_to_webbrowser(mesg):
   #  icon = pt.locateOnScreen('images/safari.png')
   #  pt.moveTo(icon , duration=1)
   #  pt.clickeurGbp()
    os.system("open /Applications/safari.app")
    os.system('say "Web Browser opened successfully"')

 go_to_webbrowser('hello')

 #<<--------------Function to select the right stock ------------------->>

 def move_move_search(message):
   myposition = pt.locateOnScreen('images/pic1.png', confidence =.7)
   pt.moveTo(myposition , duration= .2)
   pt.move(-100, 0)
   pt.click()

   myposition = pt.locateOnScreen('images/search.png', confidence =.7)
   pt.moveTo(myposition , duration= .2)
   pt.click()
   global res3
   pt.write(res3)  
   print(res3)


 move_move_search('hello')

 #<<--------------Function to select to compare otc stock with normal one ------------------->>

 def compare_otc(te):
   # image = ImageGrab.grab(bbox=  (400,400,500,100))
   # image.save('otc.png')
   myposition1 = pt.locateOnScreen('images/star.png', confidence =.9)
   pt.moveTo(myposition1 , duration=1)
   pt.move(50, 0, duration = .2)
   pt.click()
   os.system('say "stock selected"')


 compare_otc('hi') 



 #<<--------------Function to calculate the right time ------------------->>
 def locate_time(message):
   while True:
    print(strftime("%H:%M:%S", gmtime()))
    time.sleep(1)

 #locate_time('hello')


 #<<--------------Function to calculate the right time ------------------->>

 sleep(1)

 def get_price1(msg): 
   myimage = ImageGrab.grab(bbox=  (813,93,931,120))   
   myimage.save('price1.png')
      
 get_price1('hi')

 def action(mtg):
   global act
   os.system('say "Waiting for the right time"')
   if act == 0:
      myposition = pt.locateOnScreen('images/higher.png', confidence =.7)
      pt.moveTo(myposition , duration=.2)
      while strftime("%H:%M:%S", gmtime()) != strftime("%H:%M:00", gmtime()) :
         sleep(1)
      pt.click()
   elif act == 1:
      myposition = pt.locateOnScreen('images/lower.png', confidence =.7)
      pt.moveTo(myposition , duration=.2)
      while strftime("%H:%M:%S", gmtime()) != strftime("%H:%M:00", gmtime()) :
         sleep(1)
      pt.click()
   else:
      print('error : we cant know if i should buy or sell !!!')


 action('finally')

 def get_price(msg): 
   
   #price after
   myimage = ImageGrab.grab(bbox=  (813,93,931,120))   
   myimage.save('price.png')
   priceImg = cv2.imread('price.png')
   priceV = pytesseract.image_to_string(priceImg)
   print(priceV)
   priceV = priceV[priceV.find("$")+1:priceV.find(",")]
   print(priceV)
   priceV = float(priceV)

   #price before 
   priceImg = cv2.imread('price1.png')
   price1 = pytesseract.image_to_string(priceImg)
   print(price1)
   price1 = price1[price1.find("$")+1:price1.find(",")]
   print(price1)
   price1 = float(price1)

   if price1 > priceV :
    print("trade successfully")
    os.system('say "Trade successfully"')
   else:
       print("trade failed")
   
      

 #get_price('hi')

 def open_notification(msg):
   os.system('say "Trade successfully"')
   locate = pt.locateOnScreen('images/mt4.png' , confidence =.7)
   pt.moveTo(locate , duration=.1)
   pt.click()

 #open_notification('hello')

  


 
while True:
  my_program('hello')



