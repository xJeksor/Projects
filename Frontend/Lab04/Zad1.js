const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (input) => {
    console.log(answer(input));
});

function answer(input) {
    let splitInput = input.split(" ");
    return splitInput.map(element => parseInt(element));
}