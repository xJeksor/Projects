const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (input) => {
    let number = input;
    const numberOfDigits = number.length;
    let sum = 0;
    let temp = parseInt(input);

    while (temp > 0) {
        let remainder = temp % 10;
        sum += remainder ** (numberOfDigits);
        temp = parseInt(temp / 10);
    }

    if (sum === parseInt(input)) {
        console.log(`true`);
    }
    else {
        console.log(`false`);
    }
});
