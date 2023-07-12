const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function answer(arr,search){
    binarySearch(arr,0,arr.length,search);
}

function binarySearch(list,start,stop,search){
    if(start>stop){
        console.log("Brak elementu w ciągu!!!");
    } else {
        const q = parseInt((start + stop)/2);
        if(search == list[q]){
            console.log(q);
        } else if (search > list[q]){
            binarySearch(list,q+1,stop,search);
        } else {
            binarySearch(list,start,q-1,search);
        }
    }
}

rl.on('line', (input) => {
    const arr = input.split(" ").map(num => parseInt(num.trim()));
    rl.on('line', (input)=>{
        answer(arr,input);
        rl.close();
    });
});