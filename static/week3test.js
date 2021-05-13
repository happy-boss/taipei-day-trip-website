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