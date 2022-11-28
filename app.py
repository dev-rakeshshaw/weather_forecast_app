from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


root = Tk()
root.title("Weather Forecast App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
# root.attributes('-alpha',0.7) 
# root.wm_attributes('-transparentcolor','#57adff')
root.resizable(False,False)

bg_pic=PhotoImage(file="./images/bg.png")
bg_label=Label(root,image=bg_pic)
bg_label.place(x=0,y=0)

#Find the wind direction
def getWindDir(deg):
    if deg == 90:
        dir = "E"
    elif deg == 180:
        dir = "S"
    elif deg == 270:
        dir = "W"
    elif deg == 360:
        dir = "N"
    elif ((deg > 90) & (deg < 180)):
        dir = "SE"
    elif ((deg > 180) & (deg < 270)):
        dir = "SW"
    elif ((deg > 270) & (deg < 360)):
        dir = "NW"
    elif ((deg < 360) & (deg < 90)):
        dir = "N"
    return dir
    



#creating getWeather function:
def getWeather():
    city = textfield.get() #Get the city name from the text field

    #Finding the Latitude and Longitude for the City
    geolocator = Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj = TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone_.config(text=result)
    long_lat.config(text=f"({round(location.latitude,4)}° N,{round(location.longitude,4)}° E)")

    #Finding the Current date and time for the City using Lat. snd Long.
    home = pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p %Z")
    current_date=local_time.strftime("%d/%m/%Y")
    clock.config(text=current_time)
    date_.config(text=current_date)
    
    #open_weather_api
    api = (f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location.latitude},{location.longitude}/next7days?unitGroup=metric&elements=datetime%2Ctempmax%2Ctempmin%2Ctemp%2Cfeelslike%2Chumidity%2Cwindspeed%2Cwinddir%2Cpressure%2Ccloudcover%2Csunrise%2Csunset%2Cmoonphase%2Cconditions%2Cdescription%2Cicon&include=days%2Ccurrent&key=A9MYG5NFY46JJ5M6RVFG6SSXM&contentType=json")
  
    #Fetching the whole from the open_weather_api
    json_data=requests.get(api).json()

    #Fetching the current data from the open_weather_api and setting them on their respective labels
    temp = json_data["currentConditions"]["temp"]
    humidity = json_data["currentConditions"]["humidity"]
    pressure = json_data["currentConditions"]["pressure"]
    windspeed = json_data["currentConditions"]["windspeed"]
    winddir = getWindDir(json_data["currentConditions"]["winddir"])
    conditions = json_data["currentConditions"]["conditions"]


    Temperature_label_value.config(text=(temp,"°C"))
    Humidity_label_value.config(text=(humidity,"%"))
    Pressure_label_value.config(text=(pressure,"mb"))
    Wind_Speed_label_value.config(text=(winddir,windspeed,"km/h"))
    Description_label_value.config(text=(conditions))

    #>>>>>>>>>>>> Fiting data on the bottom Boxes <<<<<<<<<<<<<<<<
    #First box
    first_day = datetime.now()
    first_day_label.config(text=first_day.strftime("%A"))

    first_day_image = json_data["currentConditions"]['icon']
    icon1=PhotoImage(file=f"./icon/{first_day_image}.png")
    first_day_image_label.config(image=icon1)
    first_day_image_label.image=icon1

    first_day_max_temp=(json_data["days"][0]["tempmax"])
    first_day_min_temp=(json_data["days"][0]["tempmin"])
    sunrise = json_data["currentConditions"]['sunrise']
    sunset = json_data["currentConditions"]['sunrise']

    first_day_tempandsun_label.config(text=(f"Max:{first_day_max_temp} °C \n Min:{first_day_min_temp} °C \n Sunrise:{sunrise[0:5]} AM \n Sunset:{sunset[0:5]} PM"))


    # first_day_sun_label.config(text=(f"Sunrise:{sunrise}\nSunsey:{sunset}"))

    #Second box
    second_day = first_day+timedelta(days=1)
    second_day_label.config(text=second_day.strftime("%A"))

    second_day_image = json_data["days"][1]["icon"]
    img=(Image.open(f"./icon/{second_day_image}.png")) 
    resized_image= img.resize((50,50))
    photo2 = ImageTk.PhotoImage(resized_image) 
    second_day_image_label.config(image=photo2) 
    second_day_image_label.image=photo2
    
    second_day_max_temp=(json_data["days"][1]["tempmax"])
    second_day_min_temp=(json_data["days"][1]["tempmin"])
    second_day_temp_label.config(text=(f"Max:{second_day_max_temp} °C\nMin:{second_day_min_temp} °C"))


    #Third Box
    third_day = first_day+timedelta(days=2)
    third_day_label.config(text=third_day.strftime("%A"))

    third_day_image = json_data["days"][2]["icon"]
    img=(Image.open(f"./icon/{third_day_image}.png")) 
    resized_image= img.resize((50,50))
    photo3 = ImageTk.PhotoImage(resized_image) 
    third_day_image_label.config(image=photo3) 
    third_day_image_label.image=photo3

    third_day_max_temp=(json_data["days"][2]["tempmax"])
    third_day_min_temp=(json_data["days"][2]["tempmin"])
    third_day_temp_label.config(text=(f"Max:{third_day_max_temp} °C\nMin:{third_day_min_temp} °C"))


    #Fourth Box
    fourth_day = first_day+timedelta(days=3)
    fourth_day_label.config(text=fourth_day.strftime("%A"))

    fourth_day_image = json_data["days"][3]["icon"]
    img=(Image.open(f"./icon/{fourth_day_image}.png")) 
    resized_image= img.resize((50,50))
    photo4 = ImageTk.PhotoImage(resized_image) 
    fourth_day_image_label.config(image=photo4) 
    fourth_day_image_label.image=photo4
 
    fourth_day_max_temp=(json_data["days"][3]["tempmax"])
    fourth_day_min_temp=(json_data["days"][3]["tempmin"])
    fourth_day_temp_label.config(text=(f"Max:{fourth_day_max_temp} °C\nMin:{fourth_day_min_temp} °C"))


    #Fifth Box
    fifth_day = first_day+timedelta(days=4)
    fifth_day_label.config(text=fifth_day.strftime("%A"))

    fifth_day_image = json_data["days"][4]["icon"]
    img=(Image.open(f"./icon/{fifth_day_image}.png")) 
    resized_image= img.resize((50,50))
    photo5 = ImageTk.PhotoImage(resized_image) 
    fifth_day_image_label.config(image=photo5) 
    fifth_day_image_label.image=photo5
        
    fifth_day_max_temp=(json_data["days"][4]["tempmax"])
    fifth_day_min_temp=(json_data["days"][4]["tempmin"])
    fifth_day_temp_label.config(text=(f"Max:{fifth_day_max_temp} °C\nMin:{fifth_day_min_temp} °C"))


    #Sixth Box
    sixth_day = first_day+timedelta(days=5)
    sixth_day_label.config(text=sixth_day.strftime("%A"))

    sixth_day_image = json_data["days"][5]["icon"]
    img=(Image.open(f"./icon/{sixth_day_image}.png")) 
    resized_image= img.resize((50,50))
    photo6 = ImageTk.PhotoImage(resized_image) 
    sixth_day_image_label.config(image=photo6) 
    sixth_day_image_label.image=photo6

    sixth_day_max_temp=(json_data["days"][5]["tempmax"])
    sixth_day_min_temp=(json_data["days"][5]["tempmin"])
    sixth_day_temp_label.config(text=(f"Max:{sixth_day_max_temp} °C\nMin:{sixth_day_min_temp} °C"))


    #Seventh Box
    seventh_day = first_day+timedelta(days=6)
    seventh_day_label.config(text=seventh_day.strftime("%A"))
    
    seventh_day_image = json_data["days"][6]["icon"]
    img=(Image.open(f"./icon/{seventh_day_image}.png")) 
    resized_image= img.resize((50,50))
    photo7 = ImageTk.PhotoImage(resized_image) 
    seventh_day_image_label.config(image=photo7) 
    seventh_day_image_label.image=photo7
        
    seventh_day_max_temp=(json_data["days"][6]["tempmax"])
    seventh_day_min_temp=(json_data["days"][6]["tempmin"])
    seventh_day_temp_label.config(text=(f"Max:{seventh_day_max_temp} °C\nMin:{seventh_day_min_temp} °C"))


    

#_________________________________________________________________________________________________________________________________________________________

#app_icon
app_icon=PhotoImage(file="./Images/logo.png")
root.iconphoto(False,app_icon)

#Clock_Label
clock=Label(root,text="Clock",font=('Helvetica',20,"bold"),fg="white",bg="#FF5867")
clock.place(x=30,y=60)


#Date_Label
date_=Label(root,text="Date",font=('Helvetica',20,"bold"),fg="white",bg="#FF5867")
date_.place(x=30,y=20)

#timezone_Label
timezone_=Label(root,text="Timezone",font=('Helvetica',20),fg="#40403e",bg="#FFC0B5")
timezone_.place(x=700,y=20)

#Lat and Long._Label
long_lat=Label(root,text="Lat./Long.",font=('Helvetica',10),fg="#40403e",bg="#FFC0B5")
long_lat.place(x=700,y=50)

####>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Current Weather Box Starts <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#Setting Round_box image to display temperature, Humidity,Pressure, Wind_speed and Description
round_box_image=PhotoImage(file="./Images/Rounded_Rectangle_1.png")
round_box_image_label=Label(root,image=round_box_image,bg="#5D5378").place(x=30,y=110)

#Labels of temperature, Humidity,Pressure, Wind_speed and Description on the round box
Temperature_label=Label(root,text="Temperature:",font=('Helvetica',11),fg="white",bg="#203243")
Temperature_label.place(x=35,y=120)

Humidity_label=Label(root,text="Humidity:",font=('Helvetica',11),fg="white",bg="#203243")
Humidity_label.place(x=35,y=140)

Pressure_label=Label(root,text="Pressure:",font=('Helvetica',11),fg="white",bg="#203243")
Pressure_label.place(x=35,y=160)

Wind_Speed_label=Label(root,text="Wind Speed:",font=('Helvetica',11),fg="white",bg="#203243")
Wind_Speed_label.place(x=35,y=180)

Description_label=Label(root,text="Description:",font=('Helvetica',11),fg="white",bg="#203243")
Description_label.place(x=35,y=200)

#Labels of temperature Value, Humidity Value,Pressure Value, Wind_speed Value and Description Value on the round box
Temperature_label_value=Label(root,font=('Helvetica',11),fg="white",bg="#203243")
Temperature_label_value.place(x=125,y=120)

Humidity_label_value=Label(root,font=('Helvetica',11),fg="white",bg="#203243")
Humidity_label_value.place(x=123,y=140)

Pressure_label_value=Label(root,font=('Helvetica',11),fg="white",bg="#203243")
Pressure_label_value.place(x=123,y=160)

Wind_Speed_label_value=Label(root,font=('Helvetica',11),fg="white",bg="#203243")
Wind_Speed_label_value.place(x=123,y=180)

Description_label_value=Label(root,font=('Helvetica',11),fg="white",bg="#203243")
Description_label_value.place(x=123,y=200)
####>>>>>>>>>>>>>>>>>>>>> Current Weather Ends <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#Search box
search_box_image=PhotoImage(file="./Images/Rounded_Rectangle_3.png")
search_box_image_label=Label(root,image=search_box_image,bg="#213343")
search_box_image_label.place(x=270,y=150)

cloud_icon_image=PhotoImage(file="./Images/Layer_7.png")
cloud_icon_label=Label(root,image=cloud_icon_image,bg="#203243")
cloud_icon_label.place(x=290,y=157)

textfield = tk.Entry(root,justify="center",width=15,font=('Poppins',25,"bold"),fg="#203243",bg="white",border=0)
textfield.place(x=370,y=160)
textfield.focus()

search_icon_image=PhotoImage(file="./Images/Layer_6.png")
search_icon_button=Button(root,image=search_icon_image,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
search_icon_button.place(x=648,y=155)







####>>>>>>>>>>>>>>>>>>>>> Forecasted Weather Starts <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#Creating Bottom Frame to display the 7 days forecasted weather
bottom_frame = Frame(root,width=900,height=180,bg="#203243")
bottom_frame.pack(side=BOTTOM)

#Setting the 7 Bottom Box images.
first_box_image=PhotoImage(file="./Images/Rounded_Rectangle_2.png")
second_box_image=PhotoImage(file="./Images/Rounded_Rectangle_2_copy.png")

Label(bottom_frame,image=first_box_image,bg="#203243").place(x=30,y=20)
Label(bottom_frame,image=second_box_image,bg="#203243").place(x=300,y=30)
Label(bottom_frame,image=second_box_image,bg="#203243").place(x=400,y=30)
Label(bottom_frame,image=second_box_image,bg="#203243").place(x=500,y=30)
Label(bottom_frame,image=second_box_image,bg="#203243").place(x=600,y=30)
Label(bottom_frame,image=second_box_image,bg="#203243").place(x=700,y=30)
Label(bottom_frame,image=second_box_image,bg="#203243").place(x=800,y=30)


#>>>>>>>>>>Creating 7 frames for the 7 box on their respective Box images<<<<<<<<<<

#First Box
first_box_frame=Frame(root,width=230,height=132,bg="#C094BE")
first_box_frame.place(x=35,y=315)

first_day_label = Label(first_box_frame,font=('Arial',20),bg="#C094BE",fg="#ffffff")
first_day_label.place(x=95,y=5)

first_day_image_label=Label(first_box_frame,bg="#C094BE")
first_day_image_label.place(x=1,y=15)

first_day_tempandsun_label=Label(first_box_frame,bg="#C094BE",fg="#292F4D",font="arial 12 bold") 
first_day_tempandsun_label.place(x=80,y=43) 


#Second Box
second_box_frame=Frame(root,width=70,height=115,bg="#C094BE")
second_box_frame.place(x=305,y=325)

second_day_label = Label(second_box_frame,fg="#ffffff",bg="#C094BE")
second_day_label.place(x=5,y=5)

second_day_image_label=Label(second_box_frame,bg="#C094BE")
second_day_image_label.place(x=7,y=28)

second_day_temp_label=Label(second_box_frame,bg="#C094BE",fg="#292F4D") 
second_day_temp_label.place(x=2,y=80) 

#Third Box
third_box_frame=Frame(root,width=70,height=115,bg="#C094BE")
third_box_frame.place(x=405,y=325)

third_day_label = Label(third_box_frame,fg="#ffffff",bg="#C094BE")
third_day_label.place(x=5,y=5)

third_day_image_label=Label(third_box_frame,bg="#C094BE")
third_day_image_label.place(x=7,y=28)

third_day_temp_label=Label(third_box_frame,bg="#C094BE",fg="#292F4D") 
third_day_temp_label.place(x=2,y=80) 

#Fourth Box
fourth_box_frame=Frame(root,width=70,height=115,bg="#C094BE")
fourth_box_frame.place(x=505,y=325)

fourth_day_label = Label(fourth_box_frame,fg="#ffffff",bg="#C094BE")
fourth_day_label.place(x=5,y=5)

fourth_day_image_label=Label(fourth_box_frame,bg="#C094BE")
fourth_day_image_label.place(x=7,y=28)

fourth_day_temp_label=Label(fourth_box_frame,bg="#C094BE",fg="#292F4D") 
fourth_day_temp_label.place(x=2,y=80) 

#Fifth Box
fifth_box_frame=Frame(root,width=70,height=115,bg="#C094BE")
fifth_box_frame.place(x=605,y=325)

fifth_day_label = Label(fifth_box_frame,fg="#ffffff",bg="#C094BE")
fifth_day_label.place(x=5,y=5)

fifth_day_image_label=Label(fifth_box_frame,bg="#C094BE")
fifth_day_image_label.place(x=7,y=28)

fifth_day_temp_label=Label(fifth_box_frame,bg="#C094BE",fg="#292F4D") 
fifth_day_temp_label.place(x=2,y=80) 

#Sixth Box
sixth_box_frame=Frame(root,width=70,height=115,bg="#C094BE")
sixth_box_frame.place(x=705,y=325)

sixth_day_label = Label(sixth_box_frame,fg="#ffffff",bg="#C094BE")
sixth_day_label.place(x=5,y=5)

sixth_day_image_label=Label(sixth_box_frame,bg="#C094BE")
sixth_day_image_label.place(x=7,y=28)

sixth_day_temp_label=Label(sixth_box_frame,bg="#C094BE",fg="#292F4D") 
sixth_day_temp_label.place(x=2,y=80) 

#Seventh Box
seventh_box_frame=Frame(root,width=70,height=115,bg="#C094BE")
seventh_box_frame.place(x=805,y=325)

seventh_day_label = Label(seventh_box_frame,fg="#ffffff",bg="#C094BE")
seventh_day_label.place(x=5,y=5)

seventh_day_image_label=Label(seventh_box_frame,bg="#C094BE")
seventh_day_image_label.place(x=7,y=28)

seventh_day_temp_label=Label(seventh_box_frame,bg="#C094BE",fg="#292F4D") 
seventh_day_temp_label.place(x=2,y=80) 

root.mainloop()