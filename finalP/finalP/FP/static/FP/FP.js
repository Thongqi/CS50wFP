// window.bootstrap = require('bootstrap/dist/js/bootstrap.bundle.js');
// import * as bootstrap from 'bootstrap';
// window.bootstrap = bootstrap;
// import { Carousel } from 'bootstrap'

$(document).ready(function(){
    
    // multiple step form
    if ($("#m-step")){
        console.log("yes")
        var currentTab = 0
        showTab(currentTab)
    }

    $(".btn-primary").click(function(){
        $(this).toggleClass("btn-selected")
    })
    
    $("#from").change(function(){
        var text = $("#from").val()
        console.log(text)
    })

    //button changed color

    
    // to get the DURATION from one place to another by DRIVING
    $("#duration").click(function(event){
        event.preventDefault()
        const csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
        console.log(csrftoken)
        var from = $("#from").val()
        console.log(from)
        var to = $('#to').val()
        
        fetch('',{
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken': csrftoken,
                }, 
            mode: 'same-origin',
            method:'POST',
            body: JSON.stringify({
                from: from,
                to: to,
            })
        })
        .then(response=>response.json())
        .then(data => {
            console.log(data)
            var start = data.start.reverse() 
            var end = data.end.reverse()
            var coordinate = [start, end]
            console.log(coordinate)
            fetch(`https://api.mapbox.com/directions/v5/mapbox/driving/${coordinate.join(';')}?&access_token=pk.eyJ1IjoidGhvbmdxaSIsImEiOiJjbHg3NmJjNmIwcnowMmxzNWxyaHdkazUzIn0.q9LgpaGx-sfDPxHcQICUQQ`,{
                method:'GET',
            })
            .then(response=>response.json())
            .then(result =>{
                console.log(result)
                var duration = result.routes[0].duration
                if (duration > 3600){
                    var hour = Math.floor(duration/3600)
                }
                else {
                    hour = '0'
                }
                var minutes = Math.floor(duration/60)
                var seconds = Math.round(duration - minutes*60)

                console.log(hour + 'hr' + minutes + 'min' + seconds + 'sec')
            })
        })

        var places;
        fetch("places",{
            method:'GET',
        })
        .then(response=>response.json())
        .then(data=>{
            // convert from object to array
            places = $.map(data.places, function(obj){
                return obj.states
            })
            console.log(places)
        })

    // autocomplete search box
        $("#input-box").keyup(function(){
            // fetch("places",{
            //     method:'GET',
            // })
            // .then(response=>response.json())
            // .then(data=>{
            //     // convert from object to array
            //     let places = $.map(data.places, function(obj){
            //         return obj.states
            //     })
            //     console.log(places)
                // return array of search results
            // clear the search result first
            let result = []

            var input = $("#input-box").val()
            if(input.length > 0){
                console.log(input.length)
                result = places.filter((keyword)=>{
                    return keyword.toLowerCase().includes(input.toLowerCase())
                })
                console.log(result)
            }
            else {
                console.log(input.length)
            }
            display(result)

        })
    })

    // carousel
    if ('.carousel .carousel-item'){

        $('.carousel .carousel-item').carousel({
            interval: false
          });
        $('.carousel .carousel-item').each(function(){
            var next = $(this).next();
            console.log(next)
            if (!next.length) {
              next = $(this).siblings(':first');
            }
            next.children(':first-child').clone().appendTo($(this));
            
            if (next.next().length>0) {
              next.next().children(':first-child').clone().appendTo($(this));
            } else {
                $(this).siblings(':first').children(':first-child').clone().appendTo($(this));
            }
          });
    }
    
    if ('.ui_cont'){
        var thisPage = $(this).attr('id')
        var usefulInfo = ["language", "transport", "tips", "what-to-wear", "cash-or-card"]
        $(usefulInfo).remove(thisPage)
        console.log(usefulInfo)
        var random = getUnique(usefulInfo, 3)

        $(random).each(function(){
            $('.${this}').css("display","block")
        })
    
    }
    
})
function getUnique(arrayNum, count) {
  // Make a copy of the array
  var tmp = arrayNum.slice(arrayNum);
  var ret = [];
  
  for (var i = 0; i < count; i++) {
    var index = Math.floor(Math.random() * tmp.length);
    var removed = tmp.splice(index, 1);
    // Since we are only removing one element
    ret.push(removed[0]);
  }
  return ret;  
}

function showTab(n){
    var x = $(".tab")
    console.log(n)
    console.log(x.length)
    $(x[n]).show()

    if (n == 0){
        $("#prevBtn").hide()
    }
    else{
        $("#prevBtn").show()
    }

    if(n == (x.length - 1)){
        $("#nextBtn").html("Submit")
    }
    else{
        $("#nextBtn").html("Next")
    }

    fixStepIndicator(n)
}

function nextPrev(n){
    var x = $(".tab")

    var target = $('.tab:visible')
   

    var currentTab = $(x).index(target)
    if(n == 1 && !validateForm()) return false

    $(x[currentTab]).hide()

    currentTab = currentTab + n
    if (currentTab >= x.length){
        $("#m-step").submit()
        return false
    }

    showTab(currentTab)

}

function validateForm(){
    var x, y, i, valid = true
    x = $(".tab")
    valid = true
    return valid
}

function fixStepIndicator(n){
    var i, x = $(".step")
    for (i =0; i <x.length; i++){
        $(x[i]).addClass('').removeClass('active')
    }
    $(x[n]).addClass('active')
}


function display(result){
    console.log(result.length)
    if (result.length > '0' ){
        var content = $.map(result, (list)=>{
            return "<li onclick=selectInput(this)>" + list + "</li>"
        })
        console.log(content)
    }
    else {
        var content = "No result found"
    }

    // if nothing in input, clear result box
    if($("#input-box").val().length == '0'){
        $(".result-box").html('')
        $(".buttons1").show()
    }
    else{
        if (result.length >= '1'){
            $(".result-box").html(`
                <ul>
                ${content.join('')}
                </ul>
            `)
        }
        else{
            $(".result-box").html(`
                <ul>
                ${content}
                </ul>
            `)
        }
        
        

        //hide button when there is results
        $(".buttons1").hide()
    }
}

function selectInput(list){
    $("#input-box").val(list.innerHTML)
    $(".result-box").html('')
    $(".buttons1").show()
}

function search(){
    fetch("places",{
        method:'GET',
    })
    .then(response=>response.json())
    .then(data=>{
        // convert from object to array
        let places = $.map(data.places, function(obj){
            return obj.states
        })
        // console.log(places)
    })
    
}
