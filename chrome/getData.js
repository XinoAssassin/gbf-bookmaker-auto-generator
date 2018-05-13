/* eslint-disable */
var data = {
    north: 0,
    west: 0,
    east: 0,
    south: 0
}

function getData(){

    var a = document.getElementsByClassName("point");
    var n = a[0].innerText;
    var w = a[1].innerText;
    var e = a[2].innerText;
    var s = a[3].innerText;

    data.north = n;
    data.west = w;
    data.east = e;
    data.south = s;
}

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse){
        if (request.msg == "getData")
        {
            getData();
            getBetData();
            sendResponse(data);
        }
        return;
    }
)

function getBetData(){
    var a = document.getElementsByClassName("num");
    var b = "";
    for (let i = 4; i < a.length; i++) 
    {
        b = b + "\n" + a[i].title;
    }
    console.log(b);
}