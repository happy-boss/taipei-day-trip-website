from flask import Flask, request, render_template, redirect, session, url_for, jsonify
import mysql.connector
# 第一步先將景點的檔案開啟，這個檔案是json，做資料上的處理
import json

from werkzeug.utils import append_slash_redirect
# with open("data\\taipei-attractions.json", mode="r", encoding='utf-8') as file:
with open("data\\taipei-attractions.json", mode="r", encoding='utf-8') as file:
    data = json.load(file)
    #data\\taipei-attractions.json
# 確定抓到資料了
# print(data)
# 把資料處理


app = Flask(
    __name__, static_folder="public", static_url_path="/")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2021",
    database="mydatabase",
    buffered=True
)

mycursor = mydb.cursor()


spotlist = data["result"]["results"]
print(len(spotlist))
# print(clist)
# with open("data.txt","w",encoding='utf-8') as file:
#     for place in clist:
#         url="http://"+place["file"].split("http://")[1]
#         print(url)
#         file.write(place["info"]+","+place["stitle"]+","+place["longitude"]+","+place["latitude"]+","+url+"\n")


# for i in range(0,len(spotlist)):
#     index=spotlist[i]["_id"]
#     # print(i)
#     name =spotlist[i]["stitle"]
#     category = spotlist[i]["CAT2"]
#     description = spotlist[i]["xbody"]
#     address = spotlist[i]["address"]
#     transport = spotlist[i]["info"]
#     mrt = spotlist[i]["MRT"]
#     latitude = spotlist[i]["latitude"]
#     longitude = spotlist[i]["longitude"]

#     mylist=spotlist[i]["file"].split("http://")
    
#     for j in range(len(mylist)):
#         mylist[j]="http://"+mylist[j]
#         print(mylist[j]+'\n')

        
        # for j in range(0,len(mylist[k])):
        #     want=mylist[j]
        #     if ".jpg" in mylist[j]o:
                
        #      ".JPG" in mylist[j]or 
        #      ".png" in mylist[j]or
        #       ".PNG" in mylist[j]:
        #         mylist.append(want)
        #         #這步到拿出我要的網址
        #         # print(mylist)
        #         images=str(mylist)
                #print(type(images))

        #         #寫入sql
        


for travel in spotlist:

    index = travel["_id"]
    name = travel["stitle"]
    category = travel["CAT2"]
    description = travel["xbody"]
    address = travel["address"]
    transport = travel["info"]
    mrt = travel["MRT"]
    latitude = travel["latitude"]
    longitude = travel["longitude"]
    images = travel["file"]
    images = images.split("http")
    # print(images)
    website = ''
    for web in images:
        # print(type(web))
        # print(web)
        if ".jpg" in web:  
            website = website + "http" + web + ","
                
        elif ".JPG" in web:
            website = website + "http" + web + ","

        elif ".PNG" in web:
            website = website + "http" + web + ","
        else:
            pass
            print(website)
    sql = "INSERT INTO power (id,name,category,description,address,transport,mrt,latitude,longitude,images) VALUES (%s,%s, %s,%s,%s, %s,%s,%s, %s,%s)"
    val = (index,name,category,description,address,transport,mrt,latitude,longitude,website)
    mycursor.execute(sql, val)
    mydb.commit()



