var currentPage = 0;
//這裡是處理頁數


function getData(currentPage, keyword) {


    // var currentPage=0;
    var req = new XMLHttpRequest();
    //關鍵字跟頁數都有的狀況
    
    console.log(keyword);
    if (keyword !== null) {
        console.log(currentPage,keyword);
        req.open("get", `/api/attractions?page=${currentPage}&keyword=${keyword}`)
        
    }

    //只有page的情況
    else {
        req.open("get", "/api/attractions?page=" + currentPage)
    };
    req.onload = function () {

        var data = JSON.parse(this.responseText);
        nextpage = data.nextpage;
        

        // console.log(nextpage);
        // return nextpage

        for (i = 0; i < data.data.length; i++) {
            var imagesUrl = data.data[i].images.split(",");
            console.log(imagesUrl[0])
            var pictureName = data.data[i].name
            var pictureMrt = data.data[i].mrt
            var pictureCategory = data.data[i].category
            var attractionId=data.data[i].id;
            // console.log(attractionId);

            var bigbox = document.getElementById("bigbox");
            bigbox.classList.add("bigbox")
            //裝景點資訊的盒子
            var box = document.createElement("div");
            var pictureA=document.createElement("a");
            pictureA.setAttribute("href",`/attraction/${attractionId}`);
            box.classList.add("box");
            box.id=attractionId;
            console.log(attractionId);
            var picture = document.createElement("img");

            // picture.src=imagesUrl[1];
            picture.src = imagesUrl[0];
            picture.classList.add("picture");
            // box.appendChild(picture);
            // bigbox.append(box);
            pictureA.appendChild(picture);
            box.appendChild(pictureA);
            bigbox.append(box);
            //這裡創名字的文字
            let name = document.createElement("div");
            name.classList.add("name");
            name.appendChild(document.createTextNode(pictureName));
            box.appendChild(name);
            bigbox.appendChild(box);
            //這裡創放分類跟捷運站的箱子
            let textBox = document.createElement("div");
            textBox.classList.add("textBox");
            //這裡創捷運的文字
            let mrt = document.createElement("div");
            mrt.classList.add("mrt");
            mrt.appendChild(document.createTextNode(pictureMrt));
            //這裡創分類的文字
            let category = document.createElement("div");
            category.classList.add("category");
            category.appendChild(document.createTextNode(pictureCategory));

            textBox.appendChild(mrt);
            textBox.appendChild(category);
            // console.log(textBox)
            box.appendChild(textBox);

        };
        // console.log(nextpage);
        // return nextpage

    };//onload 資料回傳可以方便弄資料

    req.send();//送出連線

};

getData(currentPage, null);


//這個是全域變數，他會更新，在裡頭的函示中會更新，之前的坑是我又在裡面var nextpage
var nextpage;
//這裡是無限滾動
window.addEventListener("scroll", () => {

    let scrollable = document.documentElement.scrollHeight - innerHeight;
    let scrolled = window.scrollY;
    // console.log(scrollable, scrolled);
    if (nextpage != null) {
        if (Math.ceil(scrolled) === scrollable) {

            // currentPage = nextpage;
            // console.log(currentPage);
            getData(nextpage, keyword)
        }
    }
    
})

var keyword=null;

let btn = document.getElementsByClassName("searchKeyword")[0];
console.log(btn);

btn.addEventListener("click",()=>{
    keyword = document.querySelector(".inputBox").value;
        console.log(keyword);
        document.getElementById("bigbox").innerHTML = "";
        getData(currentPage, keyword)
})



{/* <a href="/api/a" */}