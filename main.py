from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time

import pyduinocoin
import ctypes,win32con

import datetime
 
print("Startin...")
image = "Wallpaper.jpg"

client = pyduinocoin.DuinoClient() #creates the api connection instance

configs = []
config = open("config.txt","r")
for i in config:
    x = i.split("=")
    configs.append(x[1].replace('\n',''))
saveDataToTXT = bool(configs[2])
textColor = (tuple(configs[1]))
username = configs[0]
delay = int(configs[3]) * 60


def addText(imagePath,isPrint):
        
    response = client.user(username)['balance']
    miner = client.miners(username)
    print("Balance : "+str(response['balance']) + "      Miner : " + str(len(miner)))
    # print(response)
    img = Image.open(imagePath)
    I1 = ImageDraw.Draw(img)
    
    ft = ImageFont.truetype('ObelixPro-cyr.ttf', 14)
    x = 20
    I1.text((x, 20),"Rig Name : ", font=ft, stroke_fill=textColor,fill='white')   
    I1.text((x, 40),"Hashrate : ", font=ft, stroke_fill=textColor,fill='white')    
    I1.text((x, 60),"Accepted : ", font=ft, stroke_fill=textColor,fill='white')   
    x = 130
    for i in range(miner.index(miner[-1])+1):
        I1.text((x, 20),str(miner[i]["identifier"]), font=ft, stroke_fill=textColor,fill='white')   
        I1.text((x, 40),str(miner[i]["hashrate"]), font=ft, stroke_fill=textColor,fill='white')    
        I1.text((x, 60),str(miner[i]["accepted"]), font=ft, stroke_fill=textColor,fill='white')   
        x = x + 100

    # Print User Data    
    I1.text((20, 120),"Username : "+str(response["username"]), font=ft, stroke_fill=textColor,fill='white')   
    I1.text((20, 140),"Stake Amount : " + str(response["stakeamount"]), font=ft, stroke_fill=textColor,fill='white')   
    I1.text((20, 160),"Balance : " + str(response["balance"]), font=ft, stroke_fill=textColor,fill='white')   

    # Save the edited image
    img.save("Wallpaper2.png")
    path = 'C:\\Users\\chhin\\OneDrive\\Documents\\Duino Coin Visualizer\\Wallpaper2.png'
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
    # print("Wallpaper set")
    if(isPrint):
        saveData()
        print("Data Saved " + str(datetime.datetime.now())) 
    
    return


def saveData ():
    # using now() to get current time
    current_time = datetime.datetime.now()
    balance = client.user(username)['balance']['balance']
    dictionary = [str(current_time),str(balance)]

    fp = open("data.txt","a") 
    fp.write(dictionary[0] + " " + dictionary[1] + "\n")
    fp.close()    
    
state = 10

while True:
    addText(image,saveDataToTXT)
    time.sleep(delay)
