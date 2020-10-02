var url = "/thermometer";
console.log("test");

$.getJSON(url, function(data){
    console.log(data.temperature);
    document.getElementById("temperature").innerHTML = data.temperature;
    document.getElementById("humidity").innerHTML = data.humidity;
});