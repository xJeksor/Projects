const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function answer(arr) {
    if (arr.length === 1) {
        return arr[0];
    } else {
        const sub_min = answer(arr.slice(1));
        return arr[0] < sub_min ? arr[0] : sub_min;
    }
}

rl.on(`line`, (input) => {
    console.log(answer(input.split(' ')));
});

