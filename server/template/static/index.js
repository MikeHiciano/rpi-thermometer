var url = "/thermometer"

$.getJson(url,function(data){
    document.getElementById("temperature").innerHTML = data.data[0].temperature
    document.getElementById("humidity").innerHTML = data.data[0].humidity
})