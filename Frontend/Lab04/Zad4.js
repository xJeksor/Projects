const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function answer(input) {
    const numbers = input.split(' ').map(num => parseInt(num.trim()));
    return numbers.filter(num => num !== 0 && num % 2 === 0);
}

rl.on('line', input => {
    console.log(answer(input).join(' '));
});


