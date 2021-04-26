from flask import *
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2021",
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
def api_attractions():
    page=request.args.get("page")
    page=int(page)*12
    # page=str(page)
    print(page)
    keyword=request.args.get("keyword")
    #nextpage寫在這裡去做判斷處理，思考順序如下總數檢調目前抓下來的資料得到剩下的比數，再去做運算搞出下一頁
    # def nextpage(page):
    #     #我前面有將page乘12了
    #     nextpage=(319-page)
    #     #有兩種狀況一個是餘數大於12跟小於12
    #     #第一個是餘數大於12，例如地24頁的資料的id是從289到300
    #     #剩下的資料比數剩19筆也就是nexpage要表示2頁
    #     #我放到運算式中(319-page)/12=2.5833333
    #     #要的就是那個2

    #     #第一種情況是餘數大於12
    #     if nextpage>12:
    #         nextpage=nextpage//12
    #         #這裡的情況是頁數是25的狀況要回傳2
    #         return nextpage
    #     #第二種狀況是餘數小餘12，代表沒有下一頁
    #     else:
    #         nextpage=None
    #         return nextpage



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
                    "id":result[i][0],
                    "name":result[i][1],
                    "category":result[i][2],
                    "description":result[i][3],
                    "address":result[i][4],
                    "transport":result[i][5],
                    "mrt":result[i][6],
                    "latitude":result[i][7],
                    "longitude":result[i][8],
                    "images":result[i][9]
                    }

                    myseclist.append(want)

                    # print("迴圈後印出來的",myseclist)
                
                return json.dumps({"nextpage":1,"data":myseclist},sort_keys=False)
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

                return json.dumps({"nextpage":1,"data":myseclists},sort_keys=False)   
        else:
            return  jsonify({
                "error":"True",
                "message":"你可能頑皮搞錯指令或是伺服器異常"
            })
           
    #這裡是有page跟keyword的狀況          
    else:
        mycursor.execute(f"SELECT  * FROM power where name like '%{keyword}%' limit 12 offset {page}")
        results=mycursor.fetchall()
        print('type(results): ', type(results))
        print("兩個條件都有的結果",results)
        if results!=None:
            mytirlist=[]
            for i in range(len(results)):
                want={
                "id":results[i][0],
                "name":results[i][1],
                "category":results[i][2],
                "description":results[i][3],
                "address":results[i][4],
                "transport":results[i][5],
                "mrt":results[i][6],
                "latitude":results[i][7],
                "longitude":results[i][8],
                "images":results[i][9]
                }

                mytirlist.append(want)

                # print("第二個迴圈後印出來的",mytirlist)
                
            return json.dumps({"nextpage":1,"data":mytirlist},sort_keys=False)
        else:
            return  jsonify({
                "error":"True",
                "message":"你可能頑皮搞錯指令或是伺服器異常"
            })  
         


@app.route("/api/attraction/<attractionId>")
def api_attraction(attractionId):
    print(attractionId)
    mycursor.execute("SELECT  * FROM power WHERE id= '%s'"%(attractionId))
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


app.run(port=3000)


