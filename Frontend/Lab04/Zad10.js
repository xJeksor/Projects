function func(arr, input){
    return arr.find(input)
}

let element = func([ 'Ala', 'Kot', 'Pies' ],  y => y === 'Ala');
let notFound = func([ 'Ala', 'Kot', 'Pies' ],  y => y === 'Jakub');

console.log(element); // ‘Ala’
console.log(notFound);