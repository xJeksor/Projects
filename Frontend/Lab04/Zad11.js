function answer(arr) {
    return arr.map(obj => {
        const sum = obj.x.length + obj.y.length;
        return {...obj, key: sum};
    });
}

const arr = [
    { key: 0, x: [4,5,6], y: [1,2,3,4]},
    { key: 0, x: [1], y: [] }
]

console.log(answer(arr));