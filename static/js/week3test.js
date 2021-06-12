fetch("/api/attraction/92")
  .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    console.log(myJson);
    let data=myJson.data;
    // 成功用出xhttps弄出的效果
    console.log(data.id);
    //先拿到平安鐘這個名字
    console.log(data.name);
    //拿到公共藝術
    console.log(data.category);
    //拿到圖片
    let picture=data.images.split(",");
    console.log(picture);
    for(var i=1;i<picture.length;i++){
    let pictureUrl="http://"+picture[i];
    console.log(pictureUrl+"\n");
    }
  });





  //這裡要刪除行程
// var deletebutton=document.querySelector(".deletebutton");
// console.log(deletebutton)

// deletebutton.addEventListener("click",()=>{
//   console.log('刪除')
//   src="/api/booking"
//   fetch(src,{
//     method: 'DELETE',
//     headers: new Headers({
//         'Content-Type': 'application/json',
        

//     })
//   }).then(function (response) {
//     return response.json();
// }).then(function (deleteJson){
//   console.log(deleteJson)
//   bookcontent()
// }
// )
    
// }
// )


// window.onload = eroll()
// window.onload = function eroll() {
// // function eroll() {
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
//       // document.querySelector(".welcomeUser").style.display="block";
//       // document.querySelector(".logoutbtn").style.display="block";
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
