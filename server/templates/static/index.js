var url = "/thermometer";

$.getJSON(url, function(data){
    console.log(data.temperature);
    document.getElementById("temperature").innerHTML = data.data.temperature;
    document.getElementById("humidity").innerHTML = data.data.humidity;
});