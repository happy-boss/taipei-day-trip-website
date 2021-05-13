//這裡是要拿到網址的id，數字的部分
var url = location.href.split("/");
console.log(url);
var attractionId = url[4];
console.log(attractionId);
var indexPic = 0;
//將網址射程全域變數
var imgUrl;
//將網址長度變成全域變數
var imgLength;





function getId(attractionId) {
  console.log(attractionId);
  // /api/attraction/${attractionId}
  fetch(`/api/attraction/${attractionId}`)
    .then(function (response) {
      return response.json();
    })
    .then(function (myJson) {
      console.log(myJson);
      let data = myJson.data;
      // 成功用出xhttps弄出的效果
      // console.log(data.id);
      //先拿到平安鐘這個名字
      // indexPic = 1;

      let name = data.name;
      console.log(name);
      //拿到公共藝術
      let category = data.category;
      console.log(data.category);

      //我在外面設一個痊癒變數，要讓裡面那一串

      //拿到圖片
      // let difficultImg=data.images;
      // console.log(difficultImg);
      
      imgUrl = data.images.split(",");
      console.log(imgUrl);

      imgLength = imgUrl.length;
      console.log(imgLength);



      //這裡來做中間的部分
      let imgBox = document.getElementById("imgBox");
      imgBox.classList.add("imgBox");
      let Pic = document.createElement("img");

      Pic.src = imgUrl[indexPic];

      Pic.classList.add("Pic");
      imgBox.appendChild(Pic);

      //這裡放左邊的文字
      let textBox = document.getElementById("textBox");
      let spotName = document.createElement("div");
      spotName.classList.add("spotName");
      spotName.appendChild(document.createTextNode(name));
      textBox.appendChild(spotName);

      let spotDescribe = document.createElement("div");
      spotDescribe.classList.add("spotDescribe");
      spotDescribe.appendChild(document.createTextNode(category));
      textBox.appendChild(spotDescribe);





      //這裡把下面的部分做出來了!!
      let descrip = data.description;
      console.log(descrip);
      let place = data.address;
      console.log(place);
      let Mrtname = data.transport;
      console.log(Mrtname);



      //先做出下面的文字區塊
      let article = document.getElementById("article");
      console.log(article);
      //這是描述的部分
      let content = document.createElement("div");
      content.classList.add("content");
      console.log(content);
      content.appendChild(document.createTextNode(descrip));
      article.appendChild(content);
      //這是景點地址的部分
      let addressTitle = document.createElement("div");
      addressTitle.classList.add("addressTitle");
      addressTitle.appendChild(document.createTextNode("景點地址："));
      article.appendChild(addressTitle);
      //這是地點的部分
      let address = document.createElement("div");
      address.classList.add("address");
      address.appendChild(document.createTextNode(place));
      article.appendChild(address);
      //這是交通的部分
      let transportation = document.createElement("div");
      transportation.classList.add("transportation");
      transportation.appendChild(document.createTextNode("交通方式："));
      article.appendChild(transportation);
      //這是捷運站名字的部分
      let mrtName = document.createElement("div");
      mrtName.classList.add("mrtName");
      mrtName.appendChild(document.createTextNode(Mrtname));
      article.appendChild(mrtName);


    })

}

getId(attractionId);

//左邊的按鈕
var leftslide = document.getElementById("leftslide");
console.log(leftslide);
leftslide.addEventListener("click", function () {
  if (indexPic < imgLength-2) {
    indexPic++;
  }
  else{
    indexPic=0;
  }
  changeUrl(indexPic);
}
)

//右邊的按鈕
var rightslide = document.getElementById("rightslide");
console.log(rightslide);
rightslide.addEventListener("click", function () {
  // console.log("嗨");
  if (indexPic < imgLength-2) {
    indexPic++;
  }
  else{
    indexPic=0;
  }
  changeUrl(indexPic);
}
)


function changeUrl(indexPic) {
  console.log(indexPic);
  // console.log(imgUrl);
  // let picimgUrl = ;
  // console.log(picimgUrl);
   document.querySelector(".Pic").src = imgUrl[indexPic];
  // img.src = "http://" + picture[indexPic].split("'")[1];
}



//點上半天變2000
var firstDay = document.querySelector('#firstDay');
console.log(firstDay);
firstDay.addEventListener("click", function () {
  console.log("嗨");
  document.querySelector('#twothousand').innerHTML = "";
  document.querySelector('#twothousand').innerHTML = "新台幣2000元"
}

)
//點下半天變2500
var secondDay = document.querySelector('#secondDay');
console.log(secondDay);
secondDay.addEventListener("click", function () {
  console.log("嗨");
  document.querySelector('#twothousand').innerHTML = "";
  document.querySelector('#twothousand').innerHTML = "新台幣2500元"
}

)