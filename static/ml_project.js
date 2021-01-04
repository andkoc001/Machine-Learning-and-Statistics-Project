/*
Machine Learning Project, GMIT 2021
Author: Andrzej Kocielski, G00376291@gmit.ie
GitHub: https://github.com/andkoc001/Data_Rep_Project
Lecturer: Dr. Ian McLoughlin
*/
// ////////////////////


// ////////////////////
// Machine Learning model 

// predict the power output from simlple linear regression
function doApplyModel_linReg() {

  $("#doApplyButton_linReg").click(function (e) {
    e.preventDefault();
    var inputWind = parseInt(document.getElementById('user_input').value);
    console.log("Here 1. Input read: " + inputWind)
    // check inputs if within turbine operative range
    if ((inputWind >= 0) && (inputWind <= 25)) {
      console.log("Here 2. Condition checked (good): " + inputWind);
      inputWind = parseInt(inputWind);
      $.getJSON("/api/lin-reg-model/" + encodeURI(inputWind), function (data) {
        $('#power_output_linReg').val(parseFloat(data).toFixed(2));
        console.log("Here 3. Model applied and the prediction is: " + data);
        // $('#power_output').val("Here 3. Model applied and the prediction is: " + data);
      });
    } else {
      console.log("Here 4 - out of range: " + inputWind);
      $("#power_output_linReg").val("Wrong input. It should be a number between 0 and 25.");
    };
  });
};

// predict the power output from polynomial regression
function doApplyModel_polyReg() {

  $("#doApplyButton_polyReg").click(function (e) {
    e.preventDefault();
    var inputWind = parseInt(document.getElementById('user_input').value);
    console.log("Here 1. Input read: " + inputWind)
    // check inputs if within turbine operative range
    if ((inputWind >= 0) && (inputWind <= 25)) {
      console.log("Here 2. Condition checked (good): " + inputWind);
      inputWind = parseInt(inputWind);
      $.getJSON("/api/poly-reg-model/" + encodeURI(inputWind), function (data) {
        $('#power_output_polyReg').val(parseFloat(data).toFixed(2));
        console.log("Here 3. Model applied and the prediction is: " + data);
        // $('#power_output').val("Here 3. Model applied and the prediction is: " + data);
      });
    } else {
      console.log("Here 4 - out of range: " + inputWind);
      $("#power_output_polyReg").val("Wrong input. It should be a number between 0 and 25.");
    };
  });
};


// ////////////////////
// random number 1-24
function doRandom() {
  var random_wind = (Math.floor(Math.random() * 24) + 1);
  console.log("Random wind speed: " + random_wind);
  document.getElementById("user_input").innerText = random_wind;
}

// ////////////////////
// random number generator 

// Adapted from stack overflow posts.
$("#normal-button").click(function (e) {
  e.preventDefault();
  $.getJSON("/api/normal", function (data) {
    $('#rand_num_output').val(data.value);
  });
});
$("#uniform-button").click(function (e) {
  e.preventDefault();
  $.getJSON("/api/uniform", function (data) {
    $('#rand_num_output').val(data.value);
  });
});

// ////////////////////
// currency exchange 

function bitcoinRate() {
  $.ajax({
    "url": "https://api.coindesk.com/v1/bpi/currentprice.json",
    "method": "GET",
    "data": "",
    "dataType": "JSON",
    "success": function (result) {
      //console.log(result);
      var rate = result.bpi.EUR.rate
      document.getElementById("outputBitcoin").innerText = "1 BitCoin (Ƀ) = €" + rate;
    },
    "error": function (xhr, status, error) {
      //console.log("error: " + status + " msg:" + error);
      var rate = result.bpi.EUR.rate
      document.getElementById("outputBitcoin").innerText = rate;
    }
  });
}


// ////////////////////
// Scroll up to top of page functionality
// Adopted from: https://www.w3schools.com/howto/howto_js_scroll_to_top.asp

// Get signal from the button
var mybutton = document.getElementById("toTop");

// The button appears when the user scrolls down 50px from the top of the document
window.onscroll = function () { scrollFunction() };
function scrollFunction() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// ////////////////////
// Input validation

// -----------------
// Login to server; adopted from: https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_login_form_modal

// Open the modal (login box)
var modal = document.getElementById('login_pop');

// -----------------
// The following is a JavaScript verification function 
// Adopted from: https://www.daniweb.com/programming/web-development/code/330933/a-simple-html-login-page-using-javascript
function check(form) {
  // the following code checkes whether the entered password is matching 
  if (form.u_name.value == "User" && form.psw.value == "GMIT") {
    window.open("equipment.html") // opens the target page while password matches
  }
}
