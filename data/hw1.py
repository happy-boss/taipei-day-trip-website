from flask import Flask, request, render_template, redirect, session, url_for, jsonify
import mysql.connector
# 第一步先將景點的檔案開啟，這個檔案是json，做資料上的處理
import json

from werkzeug.utils import append_slash_redirect
with open("taipei-attractions.json", mode="r", encoding='utf-8') as file:
    data = json.load(file)
    #data\\taipei-attractions.json

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
    websiteUrl = ''
    for url in images:
        # print(type(web))
        # print(web)
        if ".jpg" in url or ".JPG" in url or ".png" in url or ".PNG" in url:  
            websiteUrl = websiteUrl + "http" + url + ","
            print(websiteUrl)
                
       
    sql = "INSERT INTO power (id,name,category,description,address,transport,mrt,latitude,longitude,images) VALUES (%s,%s, %s,%s,%s, %s,%s,%s, %s,%s)"
    val = (index,name,category,description,address,transport,mrt,latitude,longitude,websiteUrl)
    mycursor.execute(sql, val)
    mydb.commit()
