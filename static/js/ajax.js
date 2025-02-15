function reqst()
{
  var xmlhttp;
  var myArr;
  if (window.XMLHttpRequest)
  {
    // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
    xmlhttp=new XMLHttpRequest();
  }
  else
  {
    // IE6, IE5 浏览器执行代码
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function()
  {
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
      try{
        myArr = JSON.parse(this.responseText);
      } catch (e) {

      }
      
      $(document).ready(function(){
        $(".profile-pic").html("<img src=\""+myArr.data.image+"\" alt=\"Profile\">")
    })
    }
  }
  xmlhttp.open("GET","/api/get/userimage",true);
  xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xmlhttp.send();
}
function reqst_user()
{
  var xmlhttp;
  var user;
  var myArr;
  if (window.XMLHttpRequest)
  {
    // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
    xmlhttp=new XMLHttpRequest();
  }
  else
  {
    // IE6, IE5 浏览器执行代码
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function()
  {
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {

      try{ myArr = JSON.parse(this.responseText);}catch(e){} 
      try{ $(document).ready(function(){
        $(".profile-pic-me").html("<img src=\""+myArr.data.image+"\" alt=\"Profile\">")
    })}catch(e){} 
      
    }
  }
  $(document).ready(function() {
      var usernameShow = $('.profile-pic-me-id').text();
      xmlhttp.open("GET","/api/get/userimage/"+usernameShow,true);
      xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
      xmlhttp.send();
  });
}


document.addEventListener("DOMContentLoaded", function () {
  // reqst();
  try{ reqst_user();}catch(e){} 
});
function machimage(id,class_) {
  reqst();
  const imageContainer = document.querySelector(`.${class_}`);
  const imageId = id; // 替换为实际的图片ID

  // 构造图片的URL
  const imageUrl = `/api/blog/img/${imageId}`;

  // 使用fetch或XMLHttpRequest发送请求
  fetch(imageUrl)
      .then(response => {
          if (!response.ok) {
              throw new Error("图片加载失败");
          }
          return response.blob(); // 将响应转换为Blob对象
      })
      .then(blob => {
          const imageUrl = URL.createObjectURL(blob); // 创建图片的URL
          const imgElement = document.createElement("img"); // 创建图片元素
          imgElement.src = imageUrl; // 设置图片源
          imgElement.alt = "封面"; // 设置图片描述
          imageContainer.appendChild(imgElement); // 将图片插入到容器中
      })
      .catch(error => {
          console.error("加载图片时出错：", error);
          imageContainer.innerHTML = "<p>加载图片失败，请检查图片ID是否正确。</p>";
      });
}


// document.addEventListener('touchstart', handler, { passive: true });
// document.addEventListener('touchmove', handler, { passive: true });
// document.addEventListener('mousewheel', handler, { passive: true });