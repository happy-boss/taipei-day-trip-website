
//這裡是要拿到網址的id，訂單的部分
var url = location.href.split("=");
console.log(url);
//這裡吃到我要的訂單編號
var orderNumber=url[1];
console.log(orderNumber)

function thank(orderNumber){
    fetch(`/api/order/${orderNumber}`)
    .then(function (response) {
        return response.json();
      })
      .then(function (myJson) {
        console.log(myJson);
        thankbody(myJson)

        
      })
}

thank(orderNumber)


//這裡要創出感謝頁面
function thankbody(myJson){
  console.log(myJson)
  let name=myJson.data.contact.name
  console.log(name)
  let email=myJson.data.contact.email
  console.log(email)
  let phone=myJson.data.contact.phone
  console.log(phone)

  //這裡放其他的資訊
  let number=myJson.data.number
  console.log(number)
  let price=myJson.data.price
  console.log(price)

  //景點名稱
  let spotname=myJson.data.trip.attraction.name
  console.log(spotname)
  let image=myJson.data.trip.attraction.image
  console.log(image)
  let date=myJson.data.trip.date
  console.log(date)
  let time=myJson.data.trip.time
  console.log(time)
  //這裡造圖片
  let trippic = document.querySelector(".tripImagebox");
  trippic.classList.add("bookpic")
  let tripPic = document.createElement("img");
  tripPic.src = image;
  tripPic.classList.add("tripPic");
  trippic.appendChild(tripPic);
  //這裡造景點名字
  let tripname=document.querySelector("#tripname")

  let tripName=document.createElement('span')
  tripName.appendChild(document.createTextNode(spotname));
  tripname.appendChild(tripName);
  //這裡造旅遊日期
  let tripdate=document.querySelector("#tripdate")

  let tripDate=document.createElement('span')
  tripDate.appendChild(document.createTextNode(date));
  tripdate.appendChild(tripDate);
  //這裡造旅遊時間
  let tripTime=document.querySelector("#tripTime")

  let triptime=document.createElement('span')
  triptime.appendChild(document.createTextNode(time));
  tripTime.appendChild(triptime);
  //這裡造訂單編號
  let tripnumber=document.querySelector("#tripnumber")

  let tripNumber=document.createElement('span')
  tripNumber.appendChild(document.createTextNode(orderNumber));
  tripnumber.appendChild(tripNumber);
  //造出客人名字
  let contactName=document.querySelector("#contactName")

  let customer=document.createElement('span')
  customer.appendChild(document.createTextNode(name));
  contactName.appendChild(customer);
  //造出價錢
  let tripfee=document.querySelector("#tripPrice")

  let tripFee=document.createElement('span');
  tripFee.appendChild(document.createTextNode(price));
  tripfee.appendChild(tripFee)


}







// function eroll() {

//   fetch("/api/user").then(function (response) {
//     return response.json();
//   }).then(function (myJson) {
//     console.log(myJson.data)
//     if (myJson.data != null) {
//       console.log(myJson.data.name);
//       userName = myJson.data.name;
//       document.querySelector(".schedule").style.display = "none";
//       document.querySelector(".user").style.display = "none";
//       document.querySelector(".logout").style.display = "block";
//       document.querySelector(".logout").style.display = "flex";
//       document.querySelector(".welcomeUser").textContent = "歡迎您，" + userName;
//     }
//     else {
//       document.querySelector(".schedule").style.display = "block";
//       document.querySelector(".user").style.display = "block";
//     }
//   }).catch((error) => {
//     // 錯誤

//   })

// }
// eroll()
