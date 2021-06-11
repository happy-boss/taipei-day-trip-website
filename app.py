from datetime import datetime
from flask import *

from flask import session
import time
import requests

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

# mycursor = mydb.cursor(buffered=True)




app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# mycursor = mydb.cursor(buffered=True)


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
    # mycursor = mydb.cursor()
    mycursor = mydb.cursor(buffered=True)
    
    page=request.args.get("page")
    page=int(page)*12
    # page=str(page)
    print('是你嗎',page)
    keyword=request.args.get("keyword")
    #這裡是只有page存在的時候發生的條件
    if keyword==None:
        #用f字串要加上{}讓他的型態改變
        # mycursor = mydb.cursor()
        # mycursor = mydb.cursor(buffered=True)
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
                    print('頁碼',page)
                    # print("迴圈後印出來的",myseclist)
                # mycursor.close()    
                
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
                # mycursor.close()
                return json.dumps({"nextpage":"null","data":myseclists},sort_keys=False)   
        else:
            # mycursor.close()
            return  jsonify({
                "error":"True",
                "message":"你可能頑皮搞錯指令或是伺服器異常"
            })
           
    #這裡是有page跟keyword的狀況          
    else:
        # mycursor = mydb.cursor(buffered=True)

        mycursor.execute(f"SELECT  * FROM power where name like '%%{keyword}%%' limit 12 offset {page}")
        results=mycursor.fetchall()
        #這裡要做的事是抓出全部的筆數
        mycursor.execute(f"select count(name) FROM power where name like '%%{keyword}%%'")
        total=mycursor.fetchall()
        print('了解',total)
        total=total[0][0]
        print('中',total)
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
        # mycursor.close()                               
        return json.dumps({"nextpage":nextpage,"data":mytirlist},sort_keys=False)
        #如果資料筆數共有30筆，第零頁是12第一頁是24第二頁有6筆
        #第二頁就小於12了，這裡要回傳none    


@app.route("/api/attraction/<attractionId>")
def api_attraction(attractionId):
    print('attraction',attractionId)
    mycursor = mydb.cursor(buffered=True)
    # 放在這裡
    # mydb = mysql.connector.connect()
    # mycursor = mydb.cursor()
    # mydb = connection_pool.get_connection()
    # spotcursor = mydb.cursor(buffered=True)
    # mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM power WHERE id='%s'"%(attractionId))
    user=mycursor.fetchone()
    print("你有跑嗎?",user)
    if user!=None:
        mylsit={
            "id":user[0],"name":user[1],"category": user[2],"description": user[3],"address": user[4],"transport": user[5],
            "mrt": user[6],"latitude": user[7],"longitude": user[8],"images":user[9]
            }
        mycursor.close()    
        return json.dumps({"data":mylsit},sort_keys=False)
    else:
        # spotcursor.close()
        return jsonify({
            "error":"True",
            "message":"你的景點編號輸入錯誤或是伺服器異常"
        })    



@app.route("/api/user",methods=["POST","GET","PATCH","DELETE"])
def api_route():
    # mycursor = mydb.cursor(buffered=True)
    mycursor = mydb.cursor()
    
    # 這裡是註冊
    if request.method=="POST":
        req=request.get_json()
        print(req)
        print(req["email"])
       
        
        mycursor.execute("SELECT * FROM spot WHERE email='%s'"%(req["email"]))
        check_email=mycursor.fetchone()
        print(check_email)

        if check_email==None:
            sql="INSERT INTO spot (name,email,password) VALUES (%s, %s, %s)"
            val=(req["name"],req["email"],req["password"])
            mycursor.execute(sql, val)
            mydb.commit()

            return jsonify({"ok":True},200)

        else:
            return jsonify({"error":True,"message":"註冊失敗"},400)
        # 這裡是登入動作
    elif request.method=="PATCH":
        signreq=request.get_json()
        print("想要的結果",signreq)
        print("有拿到嗎?",signreq["email"])
        #這裡搞一個新的curor
        # patchmycursor=mydb.cursor(buffered=True)


        mycursor.execute("SELECT * FROM spot WHERE email='%s'"%(signreq["email"]))
        check_signemail=mycursor.fetchone()
        print(check_signemail)

        mycursor.execute("SELECT * FROM spot WHERE password='%s'"%(signreq["password"]))
        check_signpassword=mycursor.fetchone()
        print("密碼有正確嗎",check_signpassword)
        # 要信箱跟密碼正確才能登入成功
        # 第一種信箱錯誤
        if check_signemail==None:

            return jsonify({"error":True,"message":"信箱打錯"},400)
        # 第二種密碼錯了
        elif check_signpassword==None:

            return jsonify({"error":True,"message":"密碼打錯"},400)
        # 最後一種 全部打對
        else:
            session["email"]=check_signemail[2]
            
            print("session有沒有被拿到",session["email"])
            return jsonify({"ok":True},200)


    elif request.method == "GET":
        # try:
        email=session.get('email')
        print("看看有沒有拿到",email)
        usercursor = mydb.cursor(buffered=True)
        # buffered=True
        usercursor.execute("SELECT id,name,email FROM spot where email='%s'"%(email))
        myresult=usercursor.fetchone()
        print("想要的結果",myresult)
        if myresult!=None:
            
            usercursor.close()
            return jsonify({"data":{
                    'id' : myresult[0],
                    'name' : myresult[1],
                    'email' : myresult[2]
                        }
                    })
        else:
            
            return  jsonify({"data":myresult},200)
        # except:
        #     print("get出事了")
            

        #     return jsonify({"message":"這裡出事了"},500)     

    elif request.method == "DELETE":
        try:
            session.clear()
            # print("有被刪掉嗎?",session["user"])
            return jsonify({"ok":True})   
        except:
            print("delete出事了")
            return jsonify({"message":"這裡出事了"},500)        
         

@app.route("/api/booking",methods=["POST","GET","DELETE"])
def api_booking():

    
    if request.method=="GET":
        # 先登入再說
        if session["email"]:
            bookcursor = mydb.cursor(buffered=True)
            session['id']
            print(session['id'])
            bookcursor.execute("SELECT id,name,address,images FROM power where id='%s'"%(session['id']))
            Bookresult=bookcursor.fetchone()
            print("看有抓到要的景點資訊嗎",Bookresult)

            # bookcursor = mydb.cursor()
            bookcursor.execute("SELECT * FROM book where user='%s'"%(session['user']))
            
            bookresult=bookcursor.fetchone()
            print("想要的結果",bookresult)
            if bookresult:
                bookcursor.close()
                return json.dumps({"data":{"attraction":{
                    "id":Bookresult[0],
                    "name":Bookresult[1],
                    "address":Bookresult[2],
                    "image":Bookresult[3].split(',')[0]
                },
                "date":bookresult[1],
                "time":bookresult[2],
                "price":bookresult[3],
                "customer":bookresult[4]
                }
                },sort_keys=False)
            else:
                # bookcursor.close()
                return jsonify({"message":"請把訂購資訊填妥"},500)
        else:
            return json.dumps({"error": True,"message": "尚未登入系統"}), 403



    elif request.method=="POST":
        book=request.get_json()
        print("post有進來嗎",book)
        session['user']=book['user']
        print("使用者你在嘛",session['user'])
        session['id']=book["attractionId"]
        mycursor = mydb.cursor()
        
        if book['attractionId'] !=None and book['date']!=None:
            sql="INSERT INTO book (attractionId,date,time,price,user) VALUES (%s, %s,%s, %s, %s)"
            val=(book["attractionId"],book["date"],book["time"],book["price"],book["user"])
            mycursor.execute(sql, val)
            mydb.commit()
            # mycursor.close()
            return jsonify({"ok":True},200)

        # else:
        #     return jsonify({"error":True,"message":"註冊失敗"},400)
    elif request.method == "DELETE":
        if session["email"]:
            session.pop('user',None)
            session.pop('id',None)

            return jsonify({"ok":True})              



# 第六周的api
@app.route("/api/orders", methods=["POST"])
def api_orders():
    #先確認有沒有登入
    ordersdata=request.get_json()
    print("post有進來嗎",ordersdata)
    #prime把它拿出來看看
    prime=ordersdata['prime']
    print("prime印出來吧",prime)
    price=ordersdata['order']['price']
    
    tripid=ordersdata['order']['trip']['attraction']['id']
    tripname=ordersdata['order']['trip']['attraction']['name']
    tripaddress=ordersdata['order']['trip']['attraction']['address'] 
    tripimage=ordersdata['order']['trip']['attraction']['image']
    tripdate=ordersdata['order']['trip']['date']
    triptime=ordersdata['order']['trip']['time']
    contactname=ordersdata['order']['contact']['name']
    contactemail=ordersdata['order']['contact']['email']
    contactphone=ordersdata['order']['contact']['phone']
    print("contactname",contactname)
    if session["email"]!=None:
        
        # 建立交易編號 tid
        date = time.time()
        # tid = str(date) + 'Uid' + str(session["email"])
        tid = str(date) 
        Tid=tid.split('.')[0]

        print('印Tid給我瞧瞧',Tid)
        order_params={'MerchantTradeNo': datetime.now().strftime("NO%Y%m%d%H%M%S")}
        print("試試看有沒有印出orderp",order_params)
        # 準備請求 URL
        url = 'https://sandbox.tappaysdk.com/tpc/payment/pay-by-prime'
        headers={
            'Content-type': 'application/json',
             "x-api-key":"partner_aPfrgwTXnpRlaEopHMe1uTSEvjV2S9t9sbURhgs6JjIJklRc8LaeeYZ1",
             
             }
        data={
              'prime':prime,
              "partner_key":"partner_aPfrgwTXnpRlaEopHMe1uTSEvjV2S9t9sbURhgs6JjIJklRc8LaeeYZ1",
              "merchant_id": "112112himar_TAISHIN",
              "details":"TapPay Test",
              "amount":price,
              "cardholder": {
                "phone_number": contactphone,
                "name": contactname,
                "email": contactemail,      
                },
        }

        # "merchant_id": "112112himar_TAISHIN"
        triprequest = requests.post(url,json=data, headers=headers)
        # data=json.dumps(data)
        # json=data
        print(triprequest)
        tripresponse = json.loads(triprequest.text)
        getstatus = tripresponse['status']
        print(getstatus)
        getmsg=tripresponse['msg']
        if getstatus==0:
            mycursor = mydb.cursor(buffered=True)
            sql="INSERT INTO orders (ordersnumber,ordersprice,ordersid,ordersname,ordersaddress,ordersimage,ordersdate,orderstime,ordersusername,ordersemail,ordersphone) VALUES (%s, %s,%s, %s, %s,%s,%s, %s, %s,%s,%s)"
            val=(Tid,price,tripid,tripname,tripaddress,tripimage,tripdate,triptime,contactname,contactemail,contactphone)
            mycursor.execute(sql, val)
            mydb.commit()
                
            return json.dumps({
                            "data": {
                                "number": Tid,
                                "payment": {
                                    "status": 0,
                                    "message": "付款成功"
                                }
                            }
                        })

        else:
            return json.dumps({
                            "data": {
                                "number": Tid,
                                "payment": {
                                    "status": getstatus,
                                    "message": getmsg
                                }
                            }
                        })
    #沒登入的狀況
    elif session['email']==None:
        return{
                "error": True,
                "message": "麻煩登入系統"
            }

@app.route("/api/order/<orderNumber>")
def api_order(orderNumber):
    print("有印出訂單嗎?",orderNumber)
    if session['email']==None:
            return jsonify({"error":True, "message":"未登入系統"}),403
    if orderNumber:        
        print("第六周",session['email'])
        ordercursor = mydb.cursor(buffered=True)
        ordercursor.execute("SELECT * FROM orders where ordersnumber='%s'"%(orderNumber))
        orderData=ordercursor.fetchone()
        print("第六周資料進來了嗎",orderData)
        
        return jsonify({"data":{
            "number":orderData[0],
            "price":orderData[1],
            "trip":{
                "attraction":{
                    "id":orderData[2],
                    "name":orderData[3],
                    "address":orderData[4],
                    "image":orderData[5]
                },
                "date":orderData[6],
                "time":orderData[7],
            },"contact":{
                "name":orderData[8],
                "email":orderData[9],
                "phone":orderData[10]
            },
            "status":1
        }
        
        })
    else:
        return jsonify({
        "error": True,
        "message": "系統出現問題"
        })    
    


app.run(host="0.0.0.0",port=3000, debug=True)
# host="0.0.0.0",
