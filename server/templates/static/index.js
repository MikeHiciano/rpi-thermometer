var url = "/thermometer";

$.getJson(url,function(data){
    console.log(data.temperature);
    document.getElementById("temperature").innerHTML = data.temperature;
    document.getElementById("humidity").innerHTML = data.humidity;
});