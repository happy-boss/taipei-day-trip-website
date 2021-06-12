
// 設置好等等 GetPrime 所需要的金鑰
TPDirect.setupSDK(20535, "app_PUFIcJxRIl9TzubOsY9IDEaZqQ6x2EQ826gBc922TTTHIsBtO5vZ1JeiD4y0"
    , 'sandbox')
// 把 TapPay 內建輸入卡號的表單給植入到 div 中
TPDirect.card.setup('#cardview-container')




var fields = {
    number: {
        // css selector
        element: '#card-number',
        placeholder: '**** **** **** ****'
    },
    expirationDate: {
        // DOM object
        element: document.getElementById('card-expiration-date'),
        placeholder: 'MM / YY'
    },
    ccv: {
        element: '#card-ccv',
        placeholder: '後三碼'
    }
}

TPDirect.card.setup({
    fields: fields,
    styles: {
        // Style all elements
        'input': {
            'color': 'gray'
        },
        // Styling ccv field
        'input.ccv': {
            'font-size': '16px'
        },
        // Styling expiration-date field
        'input.expiration-date': {
            'font-size': '16px'
        },
        // Styling card-number field
        'input.card-number': {
            'font-size': '16px'
        },
        // style focus state
        ':focus': {
            'color': 'black'
        },
        // style valid state
        '.valid': {
            'color': 'green'
        },
        // style invalid state
        '.invalid': {
            'color': 'red'
        },
        // Media queries
        // Note that these apply to the iframe, not the root window.
        '@media screen and (max-width: 400px)': {
            'input': {
                'color': 'orange'
            }
        }
    }
})






var feebutton = document.querySelector('#submit-button');

feebutton.addEventListener("click", (event) => {
    console.log("這裡是要付款的地方");

    event.preventDefault()

    //中間兩個地方碼調 就成功了@@程式好難

    // 取得 TapPay Fields 的 status
    // const tappayStatus = TPDirect.card.getTappayFieldsStatus()

    // 確認是否可以 getPrime
    // if (tappayStatus.canGetPrime === false) {
    //     alert('can not get prime')
    //     return
    // }

    // Get prime
    TPDirect.card.getPrime((result) => {
        if (result.status !== 0) {
            console.log('get prime error ' + result.msg)
            // return
            document.querySelector(".errorpay").textContent = "請輸入正確的付款資訊"
        }
        console.log('get prime 成功，prime: ' + result.card.prime)

        // send prime to your server, to pay with Pay by Prime API .
        // Pay By Prime Docs: https://docs.tappaysdk.com/tutorial/zh/back.html#pay-by-prime-api
        let prime = result.card.prime;
        console.log(prime);

        //這裡可以拿到景點資訊嗎
        let tripdata={
            "id": bookId,
            "name": bookname,
            "address":bookaddress,
            "image":bookurl
        }
        console.log(tripdata);
        //要放到post的資料們
        let orderdata = {
            // "前端從第三方金流 TapPay 取得的交易碼"
            "prime": prime,
            "order": {
                "price": bookprice,
                "trip": {
                    "attraction": tripdata,
                   "date":bookdate,
                   "time":booktime
                },
                "contact":{
                    //這裡放book頁的資料
                    "name":document.querySelector(".booknameinput").value,
                    "email":document.querySelector(".bookemailinput").value,
                    "phone":document.querySelector(".bookphoneinput").value
                }
            }

        }

        

        console.log(orderdata)

        let src = "/api/orders";
        fetch(src, {
            method: 'POST',
            body: JSON.stringify(orderdata),
            headers: new Headers({
                'Content-Type': 'application/json'
            })
        }
        ).then(function (response) {
            return response.json();
        }).then(function (orderJson) {
            console.log(orderJson);
            console.log(orderJson.data.payment.status)
            if(orderJson.data.payment.status==0){
                console.log(orderJson.data.number)
                location.href = "/thankyou?number="+orderJson.data.number;
            }
            else{
                alert("您付款失敗，請確認資料或是其他錯誤原因")
                return
            }
        })







    })




}

)
