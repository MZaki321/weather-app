let city = document.getElementById("city");
let type = document.getElementById("type");
let temp = document.getElementById("temp");
let image = document.getElementById("img");
let input = document.getElementById("inp");
let apikey = "99f119b582c21a2a777a8f47beb75f88";


const data = async function(search){
    let getData = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${search}&appid=${apikey}&units=metric`);
    
    let jsondata =await getData.json();
    console.log(jsondata);
    console.log(jsondata.name);

    if(jsondata.cod == 400){
        alert("please enter location");
        img.src = 'error1.png';
        city.innerHTML="";
        temp.innerHTML = "";
        type.innerHTML = "";
    }
    if(jsondata.cod == 404){
        alert("please enter right location");
        img.src = 'error2.png';
        city.innerHTMLsearch;
        temp.innerHTML = "";
        type.innerHTML = "";
    }
    city.innerHTML=search;
    temp.innerHTML=Math.floor(jsonData.main.temp)+"°C";
    type.innerHTML=jsondata.weather[0].main;

   

    if(type.innerHTML == "Clouds"){
        image.src = "clouds.png"
    }

    else if(type.innerHTML == "clear"){
        image.src = "clears.png";
    }

    else if(type.innerHTML == "rain"){
        image.src = "rain.png";
    }
    else if(type.innerHTML == "haze"){
        image.src = "haze.png";
    }
    else if(type.innerHTML == "strom"){
        image.src = "strom.png";
    }

    input.value = "";
}

function myFun(){
    search = input.value;
    data(search);
}




