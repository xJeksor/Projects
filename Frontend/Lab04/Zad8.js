const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function answer(input) {
    const words = input.split(' ');
    const histogram = words.reduce((acc, curr) => {
        acc[curr] = (acc[curr] || 0) + 1;
        return acc;
    }, {});
    return JSON.stringify(histogram)
        .replace(/\"/g, "").replace(/:/g,": ")
        .replace(/,/g,", ").replace(/{/g,"{ ")
        .replace(/}/g," }");
}

rl.on('line', (input) => {
    console.log(answer(input));
});
