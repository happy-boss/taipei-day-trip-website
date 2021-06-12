
var bookId;
var bookname;
var bookaddress;
var bookurl;
var customer;
var bookprice;
var bookdate;
var booktime;





fetch("/api/user").then(function (response) {
  return response.json();
}).then(function (myJson) {
  console.log(myJson)
  if (myJson.data != null) {
    console.log(myJson.data.name);
    userName = myJson.data.name;
    document.querySelector(".schedule").style.display = "none";
    document.querySelector(".user").style.display = "none";
    document.querySelector(".logout").style.display = "block";
    document.querySelector(".logout").style.display = "flex";
    document.querySelector(".welcomeUser").textContent = "歡迎您，" + userName;
    bookcontent()
  }
  else {
    //沒登入給我滾回首頁
    location.href = "/";
  }
}).catch((error) => {
  // 錯誤
  console.log(error)

})

// window.onload = function bookcontent() {
  // eroll()


function bookcontent() {
  //這裡抓booking的事情
  src = "/api/booking",
    fetch(src).then(function (response) {
      return response.json();
    }).then(function (myJson) {

      console.log(myJson);
      bookId = myJson.data.attraction.id;

      bookname = myJson.data.attraction.name;
      bookaddress = myJson.data.attraction.address;
      bookurl = myJson.data.attraction.image;
      bookuser = myJson.data.customer;
      console.log(bookuser);
      //這裡是價錢
      bookprice = myJson.data.price;
      //這裡是日期
      bookdate = myJson.data.date;
      console.log(bookdate)
      //這裡是時間
      booktime = myJson.data.time;

      if (bookId !== null) {
        //這裡造出名字
        let customer = document.querySelector(".customer");
        console.log(customer);
        let bookUser = document.createElement("span");
        bookUser.classList.add("customer");
        bookUser.appendChild(document.createTextNode(bookuser));
        customer.appendChild(bookUser);


        //這裡造出圖片
        let bookpic = document.querySelector(".bookpic");
        bookpic.classList.add("bookpic")
        let bookPic = document.createElement("img");
        bookPic.src = bookurl;
        bookPic.classList.add("bookPic");
        bookpic.appendChild(bookPic);


        //這裡造出平安鐘的名字
        let booktextname = document.getElementById("booktextname");
        let bookName = document.createElement("span");
        console.log(bookName);
        bookName.classList.add("booktitle");
        bookName.appendChild(document.createTextNode(bookname));
        booktextname.appendChild(bookName);
        //這裡造出日期
        let bookDate = document.querySelector(".bookDate");
        let Bookdate = document.createElement("span");
        Bookdate.classList.add("bookDate");
        Bookdate.appendChild(document.createTextNode(bookdate));
        bookDate.appendChild(Bookdate);
        //這裡造出時間
        let bookTime = document.querySelector(".bookTime");
        let booktiming = document.createElement("span");
        booktiming.classList.add("bookTime");
        booktiming.appendChild(document.createTextNode(booktime));
        bookTime.appendChild(booktiming);
        //這裡造出費用
        let bookFee = document.querySelector(".bookFee");
        let bookPrice = document.createElement("span");
        bookPrice.classList.add("bookFee");
        bookPrice.appendChild(document.createTextNode("新台幣"+bookprice+"元"));
        bookFee.appendChild(bookPrice);
        //這裡造出地點
        let bookLocation = document.querySelector(".bookLocation");
        let bookAddress = document.createElement("span");
        bookAddress.classList.add("bookLocation");
        bookAddress.appendChild(document.createTextNode(bookaddress));
        bookLocation.appendChild(bookAddress);

        //這裡造出費用
        let totalfee = document.querySelector(".totalfee");
        let totalFee = document.createElement("span");
        totalFee.classList.add("totalfee");
        totalFee.appendChild(document.createTextNode("新台幣"+bookprice+"元"));
        totalfee.appendChild(totalFee);
      }
      else {
        console.log("這裡要把你們刪掉")
      }
    }).catch((error) => {
      // 錯誤
      console.log("這裡要把你們刪掉");
      document.querySelector(".booktopflex").style.display = "none";
      document.querySelector(".booktoptext").style.display = "none";
      document.querySelector(".bookcenter").style.display = "none";
      document.querySelector(".bookbottom").style.display = "none";
      document.querySelector(".bookunder").style.display = "none";
      //水平線消失
      document.querySelector(".line").style.display = "none";
      document.querySelector(".linecenter").style.display = "none";
      document.querySelector(".linebottom").style.display = "none";
      document.querySelector(".coryright").style.display = "none";
      //造出一段文字
      // noordertext
      document.querySelector(".noordertext").style.display = "block";

      document.querySelector(".coryrighttwo").style.display = "block";
    })

}

//這裡要刪除行程
var deletebutton = document.querySelector(".deletebutton");
console.log(deletebutton)

deletebutton.addEventListener("click", () => {
  console.log('刪除')
  src = "/api/booking"
  fetch(src, {
    method: 'DELETE',
    headers: new Headers({
      'Content-Type': 'application/json',
    })
  }).then(function (response) {
    return response.json();
  }).then(function (deleteJson) {
    console.log(deleteJson)
    bookcontent()
  }
  )

}
)