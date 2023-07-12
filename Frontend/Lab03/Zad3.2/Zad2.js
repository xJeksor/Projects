const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let num1, num2;

rl.on('line', (input) => {
    const nums = input.split(' ').map(parseFloat);
    if (nums.length === 2 && !isNaN(nums[0]) && !isNaN(nums[1])) {
        num1 = nums[0];
        num2 = nums[1];
        console.log(num1 + num2);
        rl.close();
    }
});
