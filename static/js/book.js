
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
  }
  else {
    // document.querySelector(".schedule").style.display = "block";
    // document.querySelector(".user").style.display = "block";
    window.location.href="/";
  }
}).catch((error) => {
  // 錯誤
  console.log(error)

})



window.onload = function bookcontent() {



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
      //這裡是時間
      booktime = myJson.data.time;


      console.log(bookId);
      console.log(bookname);
      console.log(bookaddress);
      console.log(bookurl);

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
      bookPrice.appendChild(document.createTextNode(bookprice));
      bookFee.appendChild(bookPrice);
      //這裡造出地點
      let bookLocation = document.querySelector(".bookLocation");
      let bookAddress = document.createElement("span");
      bookAddress.classList.add("bookLocation");
      bookAddress.appendChild(document.createTextNode(bookaddress));
      bookLocation.appendChild(bookAddress);
    })
}


