const myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Udało się!");
    }, 5000);
});

myPromise.then((result) => {
    console.log(result);
});