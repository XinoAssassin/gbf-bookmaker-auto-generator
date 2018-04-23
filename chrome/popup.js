/* eslint-disable */
document.getElementById("getButton").addEventListener("click", getData);
document.getElementById("sendButton").addEventListener("click", sendData)

var data = {
    "north": 0,
    "west": 0,
    "east": 0,
    "south": 0
}

function getData() {
    chrome.tabs.query(
        {
            active: true,
            currentWindow: true
        },
        function (tabs) {
            console.log(tabs[0].id);
            chrome.tabs.sendMessage(
                tabs[0].id,
                {
                    msg: "getData"
                },
                function (response) {
                    console.log(response);
                    data = response;
                    var textarea = document.getElementById("ta1");
                    textarea.innerText = "North: " + response.north + '\n'
                        + "West: " + response.west + '\n'
                        + "East: " + response.east + '\n'
                        + "South: " + response.south;
                }
            );
        });
}

function sendData() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://xinoassassin.me:9911", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(data));
    xhr.onreadystatechange == function () {
        if (this.onreadystatechange == 200)
        {
            return;
        }
    }
}