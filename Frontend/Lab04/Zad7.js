const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function answer(input) {
    const numbers = input.split(" ").map(num => parseFloat(num.trim()));
    return numbers.filter(num => num % 1 === 0).map(num=> Math.pow(num,2).toFixed(2));
}

rl.on('line', (input) => {
    console.log(answer(input));
});