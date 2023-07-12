function multiplyAsync(x,y){
    return new Promise((resolve,reject) => {
        if (typeof x !== `number` || typeof y !== `number`){
            reject(new Error("Oby dwa argumenty muszą być liczbami"));
        }
        else {
            const result = x * y;
            resolve(result);
        }
    });
}

const callback = (result) => {
    console.log(result);
}

multiplyAsync(2, 3)
    .then(callback)
    .catch(callback);

multiplyAsync(2, 'a')
    .then(callback)
    .catch(callback);