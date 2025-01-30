const display = document.getElementById("display");

function appendToDisplay(input) {
    display.value += input;
}

function clearToDisplay() {
    display.value = "";
}

function calculate() {
    try {
        display.value = eval(display.value);
    } catch (error) {
        display.value = "error can't display"
    }

}

var home_link = document.getElementById("home-link");

home_link.addEventListener("click", function(event) {
    event.preventDefault();
    window.location.href = "/";


});