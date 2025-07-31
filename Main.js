let num1 = document.getElementById("num1").innerText;
let num2 = document.getElementById("num2").innerText;
let num3 = document.getElementById("num3").innerText;

function add() {
    let sum = parseInt(num1) + parseInt(num2) + parseInt(num3);
    document.getElementById("result").innerText = "Sum: " + sum;
}
function subtract() {
    let sum = parseInt(num1) - parseInt(num2) - parseInt(num3);
    document.getElementById("result").innerText = "Subtraction is: " + sum;
} function multiply() {
    let sum = parseInt(num1) * parseInt(num2) * parseInt(num3);
    document.getElementById("result").innerText = "Multiplication is: " + sum;
}
