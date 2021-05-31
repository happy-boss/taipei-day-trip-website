// 左邊點擊出現小視窗
var schedule = document.querySelector(".schedule");
console.log(schedule);
schedule.addEventListener('click', function () {
    document.querySelector('.signBox').style.display = "block";
}
)
//右邊點即出現小視窗
var user = document.querySelector(".user");
user.addEventListener('click', function () {
    document.querySelector('.signBox').style.display = "block";
}
)


var X_mark = document.querySelector(".X_mark")

X_mark.addEventListener("click", () => {
    document.querySelector('.signBox').style.display = "none";
}
)


var X_marksec = document.querySelector(".X_marksec")

X_marksec.addEventListener("click", () => {
    document.querySelector('.erollBox').style.display = "none";
}
)

//點下面的文字換註冊介面
var erollbuttonText = document.querySelector(".erollbuttonText")

erollbuttonText.addEventListener("click", () => {
    document.querySelector('.erollBox').style.display = "block";
    document.querySelector('.signBox').style.display = "none";
}

)

//點下面的文字換登入介面
var haveAccount = document.querySelector('.haveAccount')

haveAccount.addEventListener("click", () => {
    document.querySelector('.signBox').style.display = "block";
    document.querySelector('.erollBox').style.display = "none";
}

)

//這裡做註冊的事情
var erollAccount = document.querySelector(".erollAccount");
console.log(erollAccount);
erollAccount.addEventListener("click", (event) => {
    event.preventDefault();
    var name = document.getElementById("erollname").value;
    console.log(name);
    var email = document.getElementById("erollemail").value;
    var password = document.getElementById("erollpassword").value;

    var data = {
        "name": name,
        "email": email,
        "password": password
    }
    console.log(data);
    let src = "/api/user";
    fetch(src, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: new Headers({
            'Content-Type': 'application/json'
        })
    }).then(function (response) {
        return response.json();
    }).then(function (erolljson) {
        console.log(erolljson);
        console.log(erolljson[0].ok);
        if (erolljson[0].ok == true) {
            // console.log("帥")
            document.getElementById("erollname").value = "";
            document.getElementById("erollemail").value = "";
            document.getElementById("erollpassword").value = "";
            document.getElementById("erollok").style.display = "block";
            document.getElementById("erollok").textContent = "恭喜註冊成功"
        }
        else {
            document.getElementById("erollname").value = "";
            document.getElementById("erollemail").value = "";
            document.getElementById("erollpassword").value = "";
            document.getElementById("erollok").style.display = "block";
            document.getElementById("erollok").textContent = "你註冊失敗，你個爛的"
        }
    })

}
)

//這裡做登入的事情
var signAccount = document.querySelector(".signAccount");
signAccount.addEventListener("click", (signinevent) => {
    signinevent.preventDefault();
    var signemail = document.getElementById("signemail").value;
    var signpassword = document.getElementById("signpassword").value;

    var data = {
        "email": signemail,
        "password": signpassword
    };
    console.log(data)
    let src = "/api/user";
    fetch(src, {
        method: 'PATCH',
        body: JSON.stringify(data),
        headers: new Headers({
            'Content-Type': 'application/json'
        })


    }).then(function (response) {
        return response.json();
    }).then(function (signinJson) {
        console.log(signinJson);
        console.log(signinJson[0].ok)
        if (signinJson[0].ok == true) {
            //   document.getElementById("signemail").value="";
            //   document.getElementById("signpassword").value="";
            //   document.getElementById("signok").textContent="恭喜你，登入成功"
            // window.location.reload()
            document.querySelector(".signBox").style.display = "none";
            eroll()
        }
        else {
            document.getElementById("signemail").value = "";
            document.getElementById("signpassword").value = "";
            document.getElementById("signok").textContent = "你個爛的，帳密亂打"
        }
    }
    )



}

)

var userName;


function eroll() {
    fetch("/api/user").then(function (response) {
        return response.json();
    }).then(function (myJson) {
        console.log(myJson.data)
        if (myJson.data != null) {
            console.log(myJson.data.name);
            userName = myJson.data.name;
            document.querySelector(".schedule").style.display = "none";
            document.querySelector(".user").style.display = "none";
            document.querySelector(".logout").style.display = "block";
            document.querySelector(".logout").style.display = "flex";
            // document.querySelector(".welcomeUser").style.display="block";
            // document.querySelector(".logoutbtn").style.display="block";
            document.querySelector(".welcomeUser").textContent = "歡迎您，" + userName;

            gobooking()
        }
        else {
            document.querySelector(".schedule").style.display = "block";
            document.querySelector(".user").style.display = "block";
        }
    }).catch((error) => {
        // 錯誤

    })

}



//這裡要做登出的動作
var logoutbtn = document.querySelector(".logoutbtn");
console.log(logoutbtn);

logoutbtn.addEventListener("click", () => {
    console.log("要登出");
    let src = "/api/user";
    fetch(src, {
        method: 'DELETE',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': 'application/json'

        })
    }).then(function (response) {
        return response.json();
    }).then(function (logoutJson) {
        console.log(logoutJson.ok)
        if (logoutJson.ok == true) {
            // window.location.reload();
            // getData(currentPage, keyword)
            document.querySelector(".schedule").style.display = "block";
            document.querySelector(".user").style.display = "block";
            document.getElementById("signemail").value = "";
            document.getElementById("signpassword").value = "";
            document.querySelector(".logout").style.display = "none"
        }
    })


}

)


//點擊按鈕要去/book
var bookbutton = document.getElementById("bookbutton");
console.log(bookbutton)

// ,{method:"GET"}
bookbutton.addEventListener("click", function gobooking() {
    fetch("/api/user"
    ).then(function (response) {
        return response.json();
    }).then(function (myJson) {
        console.log(myJson);
        console.log(myJson.data);
        if (myJson.data == null) {
            console.log("快去登入")
            document.querySelector(".signBox").style.display = "block"
        }
        else {

            // window.location.href="/booking";
            book(attractionId)
        }

    }
    )
}

)







//做測試
function book(attractionId) {
    let orderdate = document.querySelector('.choosedate').value;
    // window.location.href="/booking";
    let orderdata = {
        "attractionId": attractionId,
        "date": orderdate,
        "time": ordertime,
        "price": ordermoney,
        "user": userName

    }
    console.log(orderdata)
    let src = "/api/booking";
    fetch(src, {
        method: 'POST',
        body: JSON.stringify(orderdata),
        headers: new Headers({
            'Content-Type': 'application/json'
        })
    }).then(function (response) {
        return response.json();
    }).then(function (myJson) {
        console.log(myJson);
        console.log(myJson[0].ok);
        if (myJson[0].ok === true) {
            window.location.href = "/booking";
        }

    })

}

