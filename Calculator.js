const output = document.getElementById("result");
const history = document.getElementById("history");
const buttons = document.getElementById("keyboard");

let currentNumber = '0'
let previousNumber = ''
let operator = '';

function updateDisplay() {
    output.textContent = currentNumber;
    history.textContent = previousNumber + ' ' + operator;
}

buttons.addEventListener('click', function (e) {
    if (!e.target.matches('button')) return;

    const button = e.target;
    const value = button.textContent;
    const id = button.id;

    if (button.classList.contains('number')) {
        if (currentNumber == '0' || operator == '=') {
            currentNumber = value;
            if (operator == '=') {
                previousNumber = '';
                operator = '';
            }
        } else {
            currentNumber += value;
        }
    }

    if (button.classList.contains('operator')) {
        if (id == 'clear') {
            currentNumber = '0';
            previousNumber = '';
            operator = '';
        }
        else if (id == 'backspace') {
            currentNumber = currentNumber.slice(0, -1) || '0';
        }
        else if (id == 'equals') {
            calculate();
        }
        else if (id == 'percent') {
            currentNumber = parseFloat(currentNumber) / 100;
        }

        else {
            if (previousNumber && operator) {
                calculate();
            }
            previousNumber = currentNumber;
            operator = value;
            currentNumber = '0'
        }
    }

    updateDisplay();
});

function calculate() {
    const prev = parseFloat(previousNumber);
    const current = parseFloat(currentNumber);
    let result = 0;

    switch (operator) {
        case '+': result = prev + current; break;
        case '-': result = prev - current; break;
        case '*': result = prev * current; break;
        case '/': result = prev / current; break;
        default: return;
    }

    currentNumber = result.toString();
    operator = '=';
}

updateDisplay();