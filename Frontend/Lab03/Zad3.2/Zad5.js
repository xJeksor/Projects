const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


rl.on("line", (n) => {
    let ans = '';
    for (let i = 1; i <= n; i++) {
        ans += '*'.repeat(i) + '\n';
    }
    for (let i = n; i >= 1; i--) {
        ans += '*'.repeat(i) + '\n';
    }
    for (let i = 0; i < n; i++) {
        ans += ' '.repeat(i) + '*'.repeat(n - i) + '\n';
    }
    for (let i = n; i >= 1; i--) {
        ans += ' '.repeat(i - 1) + '*'.repeat(n - i + 1) + '\n';
    }
    console.log(ans);
});


