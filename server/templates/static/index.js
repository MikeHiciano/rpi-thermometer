var url = "/thermometer";

var myvar = setInterval(() => {
    $.getJSON(url, function(data){
        document.getElementById("temperature").innerHTML = data.data.temperature;
        document.getElementById("humidity").innerHTML = data.data.humidity;
    });
}, 10000);

