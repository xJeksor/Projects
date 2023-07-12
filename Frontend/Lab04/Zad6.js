const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function answer(input) {
    const numbers = input.split(" ").map(num => parseFloat(num.trim()));
    return numbers.reduce((acc, curr) => acc + curr, 0);
}

rl.on('line', (input) => {
    console.log(answer(input));
});