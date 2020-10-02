var url = "/thermometer"

$.getJson(url,function(data){
    document.getElementById("temperature").innerHTML = data.temperature
    document.getElementById("humidity").innerHTML = data.humidity
})