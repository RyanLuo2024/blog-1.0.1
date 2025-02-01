function searchInPage() {
    var searchText = prompt("请输入要查找的内容：", "");
    if (searchText) {
      if (window.find) {
        var found = window.find(searchText,false,false,false,true,false,false);
        if (!found) {
          alert("未找到匹配的内容！");
        }
      } else {
        alert("您的浏览器不支持页面搜索功能！");
      }
    }
}