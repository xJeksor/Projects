const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

var odp = '';
function answer(a, b) {
    if (a <= b) {
        odp += a.toString() + " ";
        answer(a + 1, b);
    }
    else {
        console.log(odp);
    }
}

rl.on(`line`, (input) =>{
   const [a ,b] = input.split(' ').map(Number);
   answer(a,b);
   rl.close();
});

