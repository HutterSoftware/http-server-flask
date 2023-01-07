
function sendRequest(host, method, responseFunc, data) {
    var request = new XMLHttpRequest();
    if (method === "GET") {
        var dataList = Object.values(data);
        for (var i = 0; i < dataList.length; i++) {
            console.log(dataList[i]);
        }
    }

    request.open(method, host, true);
    request.setRequestHeader("Content-Type", "application/json");

    console.log(data);
    if (method === "POST") {
        data = JSON.stringify(data)
        request.send(data);
    } else {
        request.send();
    }
}