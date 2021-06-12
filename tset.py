
# def test():
#     if 2<1:
#         print("答對了")
#     else:
#         return error()

# def error():
#     x="答錯了"
#     print(x)

# test()  
    
# test()
# print(x)

def func():
    x = 19
    getX(x)
    return getX(x)
def getX(bbb):
    gggg=bbb+1
    return gggg

print(func())


#     return x
# def setX(n):
#     nonlocal x
#     x = n
#     return (getX, setX)

# getX, setX = func()
# z=getX()
# setX(20)
# print(setX(20))
# b=getX()
# print(z)

# # c=setX(20)

# # b=getX()
# print(b)




# 做實驗加看看pooling
# from mysql.connector import pooling



# connection_pool = mysql.connector.connect(
#     pool_name="pynative_pool",
#     pool_size=5,
#     pool_reset_session=True,
#     host="localhost",
#     user="root",
#     password="2021",
#     database="mydatabase",
#     buffered=True
# )

# mydb=connection_pool.get_connection()

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
        tid = str(date) + 'Uid' + str(session["email"])
        print('印tid給我瞧瞧',tid)
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
            val=(tid,price,tripid,tripname,tripaddress,tripimage,tripdate,triptime,contactname,contactemail,contactphone)
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.close()    
            return json.dumps({
                            "data": {
                                "number": tid,
                                "payment": {
                                    "status": 0,
                                    "message": "付款成功"
                                }
                            }
                        })

        else:
            return json.dumps({
                            "data": {
                                "number": tid,
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
    
        return 200
