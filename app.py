from flask import *
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="debian-sys-maint",
    password="a6OS5uhB5j7X6cer",
    database="mydatabase",
    buffered=True
)



mycursor = mydb.cursor()


# Pages
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/attraction/<id>")
def attraction(id):
    return render_template("attraction.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

@app.route("/api/attractions")
# 另外開一個函示去處理，先處理只有Page的情況



def api_attractions():
    page=request.args.get("page")
    page=int(page)*12
    # page=str(page)
    print(page)
    keyword=request.args.get("keyword")
    #這裡是只有page存在的時候發生的條件
    if keyword==None:
        #用f字串要加上{}讓他的型態改變
        mycursor.execute(f"SELECT  * FROM power  limit 12 offset {page}")
        result=mycursor.fetchall()
        #抓出來的result存在就讓他跑
        if result!=None:
        # print('type(result): ', type(result))
        # print(result)
            if len(result)==12:
                myseclist=[]
                for i in range(12):
                    want={
                    "id":result[i][0],"name":result[i][1],"category":result[i][2],"description":result[i][3],"address":result[i][4],
                    "transport":result[i][5],"mrt":result[i][6],"latitude":result[i][7],"longitude":result[i][8],"images":result[i][9]
                    }

                    myseclist.append(want)
                    nextpage=page//12+1
                    print(page)
                    # print("迴圈後印出來的",myseclist)
                return json.dumps({"nextpage":nextpage,"data":myseclist},sort_keys=False)
            else:
                myseclists=[]
                for j in range(len(result)):
                    wants={
                        "id":result[j][0],
                        "name":result[j][1],
                        "category":result[j][2],
                        "description":result[j][3],
                        "address":result[j][4],
                        "transport":result[j][5],
                        "mrt":result[j][6],
                        "latitude":result[j][7],
                        "longitude":result[j][8],
                        "images":result[j][9]
                        }

                    myseclists.append(wants)

                return json.dumps({"nextpage":"null","data":myseclists},sort_keys=False)   
        else:
            return  jsonify({
                "error":"True",
                "message":"你可能頑皮搞錯指令或是伺服器異常"
            })
           
    #這裡是有page跟keyword的狀況          
    else:
        mycursor.execute(f"SELECT  * FROM power where name like '%%{keyword}%%' limit 12 offset {page}")
        results=mycursor.fetchall()
        #這裡要做的事是抓出全部的筆數
        mycursor.execute(f"select count(name) FROM power where name like '%%{keyword}%%'")
        total=mycursor.fetchall()
        print(total)
        total=total[0][0]
        print(total)
        mytirlist=[]
        # nextpage=page//12+1
        for i in range(len(results)):
            want={
                    "id":results[i][0],"name":results[i][1],"category":results[i][2],
                    "description":results[i][3],"address":results[i][4],"transport":results[i][5],
                    "mrt":results[i][6],"latitude":results[i][7],"longitude":results[i][8],"images":results[i][9]
                    }
            mytirlist.append(want)
            if total>=page+12:
                nextpage=page//12+1
            else:
                nextpage="null"    
                                       
        return json.dumps({"nextpage":nextpage,"data":mytirlist},sort_keys=False)
        #如果資料筆數共有30筆，第零頁是12第一頁是24第二頁有6筆
        #第二頁就小於12了，這裡要回傳none    
       
            






            # return  jsonify({
            #         "error":"True",
            #         "message":"你可能頑皮搞錯指令或是伺服器異常"
            #         })  
         


@app.route("/api/attraction/<attractionId>")
def api_attraction(attractionId):
    print(attractionId)
    mycursor.execute("SELECT  FROM power WHERE id= '%s'"%(attractionId))
    user=mycursor.fetchone()
    print(user)
    if user!=None:
        mylsit={
            "id":user[0],
            "name":user[1],
            "category": user[2],
            "description": user[3],
            "address": user[4],
            "transport": user[5],
            "mrt": user[6],
            "latitude": user[7],
            "longitude": user[8],
            "images":user[9]
            }
        return json.dumps({"data":mylsit},sort_keys=False)
    else:
        return jsonify({
            "error":"True",
            "message":"你的景點編號輸入錯誤或是伺服器異常"
        })    


app.run( host="0.0.0.0",port=3000)
# host="0.0.0.0",
