import serial
import pyttsx3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text   import MIMEText
import webbrowser as vb
import  urllib.request as urllib
import json
import linecache
import cv2
import numpy as np
import time
#import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests
import os
import base64
from weather import Weather
import speech_recognition as sr



r = sr.Recognizer()
face=cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
try:
    defserial = serial.Serial('com3',9600)
except:
    pass
camera_input = cv2.VideoCapture(0);

m = 1
engine = pyttsx3.init()
rate= engine.getProperty('rate')
engine.setProperty('rate',rate-40)
volume = engine.getProperty('volume')
engine.setProperty('volume',volume + 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id )

while(True):
    ret,img = camera_input.read();
    g_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(g_img,1.3,5);
    for(x,y,w,h) in faces :
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        a = 1
        if(a==1):

            cv2.imshow('Face',img)
            if(cv2.waitKey(1)==ord('x')or m==0):
                break;
            time.sleep(0.5)
            camera_input.release()
            cv2.destroyAllWindows()
            print("Face has been detected")
            engine.say("Face has been detected")
            engine.runAndWait()

            
            while(True):
                     
                   
                        input_var=input("")
                                             
                        if "mail"  in input_var:
                            print("Send An E-mail??:")
                            engine.say("Send An E-mail??")
                            engine.runAndWait()
                            input_var1=input("")
                            if "yes" in input_var1:
                                fromaddress = 'adivijay10000@gmail.com'
                                engine.say("Enter the Receiver's Mail:")
                                engine.runAndWait()
                                rec=input("Enter the Receiver's Mail:")
                            
                                toaddress = rec
                                print("Enter the subject  name:")
                                engine.say("Enter the subject  name:")
                                engine.runAndWait()
                                sub=input("")
                                username = 'adivijay'
                                password ='adityaditya989845678'  
                                msg = MIMEMultipart()
                                msg['From'] =fromaddress
                                msg['To']=toaddress
                                msg['subject']=sub
                                print("Enter the Text You Want to Send:")
                                engine.say("Enter the Text You Want to Send:")
                                engine.runAndWait()
                                text=input("")


                                msg.attach(MIMEText(text,'plain'))
                                server = smtplib.SMTP('smtp.gmail.com',587)
                                server.ehlo()
                                server.starttls()
                                server.ehlo()
                                t2=msg.as_string()
                                server.login(fromaddress,"adityaditya989845678")
                                server.sendmail(fromaddress,toaddress,t2)
                                server.quit()
                                print("Your Message  has been sent")
                                engine.say("Your Message  has been sent")
                                engine.runAndWait()
                           
                        elif "facebook" in input_var:
                            vb.get('windows-default') .open ('http://www.facebook.com')
                            print("i have opened facebook")
                            engine.say("i opened facebook")
                            engine.runAndWait()

                        elif "google" in input_var:
                            vb.get('windows-default') .open ('http://www.google.co.in')
                            print("i have opened google")
                            engine.say("i opened Google")
                            
                            engine.runAndWait()
                            
                        elif"news" in input_var:
                            print("please wait i am fetching latest news:")
                            engine.say("please wait i am fetching latest news:")
                            engine.runAndWait()
                            c = urllib.urlopen('http://timesofindia.indiatimes.com/feeds/newsdefaultfeeds.cms?feedtype=sjson')
                            json_string = c.read()
                            parsed_news = json.loads(json_string)
                            
                            for i in range(1,4):
                                engine.say(parsed_news['NewsItem'][i]['HeadLine'] )
                                print(parsed_news['NewsItem'][i]['HeadLine'] )
                                engine.runAndWait()
                         
                        elif "light on" in input_var:
                                defserial.write('3'.encode())

                        elif "light off" in input_var:
                                defserial.write('2'.encode())
            


                        elif "object analysis" in input_var:
                            face = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
                            camera_input=cv2.VideoCapture(0)

                            identifier =input("Enter User Id:")
                            sample=0

                            while(True):
                                ret,img = camera_input.read()
                                sample=sample+1
                                path='D:/pics/images/userimg.jpg'
                                cv2.imwrite(os.path.join(path),img)
                                cv2.imshow('Face',img)
                                
                                

                                headers = {
                                'Content-Type': 'application/octet-stream',
                                'Ocp-Apim-Subscription-Key': '1671aa7ff1274203a0dc8b052660d970',
                                }

                                params = {
                                    'visualFeatures': 'Description',
                                    'details': 'Celebrities',
                                    'language': 'en',
                                }
                                image = open(path,'rb').read() # Read image file in binary mode

                                try:
                                    response = requests.post(url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze',
                                                             headers = headers,
                                                             params = params,
                                                             data = image)
                                    data = response.json()
                                    print(data["description"]["captions"][0]["text"])
                                    break;
                                
                                    
                                except Exception as e:
                                    print("[Errno {0}] {1}".format(e.errno, e.strerror))

                                


                            camera_input.release()
                            cv2.destroyAllWindows()

                        
                        elif "weather" in input_var :
                            weather = Weather()
                            # Lookup WOEID via http://weather.yahoo.com.

                            lookup = weather.lookup(560743)
                            condition = lookup.condition()
                            print(condition.text())

                            # Lookup via location name.

                            location = weather.lookup_by_location('ahmedabad')
                            condition = location.condition()
                            print(condition.text())

                            # Get weather forecasts for the upcoming days.

                            forecasts = location.forecast()
                            for forecast in forecasts:
                                print(forecast.text())
                                print(forecast.date())
                                print(forecast.high() + "        Fahrenheit")
                                print(forecast.low()  + "        Fahrenheit")

                                                       
                                                        
                        elif input_var in open('read.txt').read():
                            file='read.txt'
                            word=input_var
                            with open(file,'r') as text:
                                for num,line in enumerate(text):
                                    if word in line:
                                        num
                                        k=linecache.getline('read2.txt',num+1)
                                        print(k)
                                        engine.say(k)
                                        engine.runAndWait()
                        else:
                                    file3=open("read.txt","a+")#opening a notepad file for appending text
                                    file4=open("read2.txt","a+") #opening another notepad file for appending text
                                    file3.write(input_var+("\n"))#append the input given by user
                                    print("Can You Tell me the anwser :")
                                    engine.say('Can You Tell me the anwser :')
                                    engine.runAndWait()
                                    str2=input() #user has to give the meaning of privious input
                                    file4.write(str2+("\n"))
                                    file3.close()
                                    file4.close()
                            

camera_input.release()
cv2.destroyAllWindows()

   
