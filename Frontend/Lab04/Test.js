// const l = {
//     name:"ola",
//     cos:"cos",
// }
//
// const l2 = {
//     name:"Ada",
//     cos2:"ez"
// }
//
// const age = 13;
//
// const test = {
//     ...l,
//     age
// }
//
// const e = {
//     ...l,
//     ...l2
// }
//
// const a = ["1","2","3"]
// const b = ["4"]
//
// const c = ("1","2","3")
// const d = ("4")
//
// console.log(test)
// console.log(a.concat(b))
// console.log(c.concat(d))
// console.log(e)
//
// const f = [[[]]];
// console.log(f)
//
//
//
//
//
// //
// function test() {
//     console.log(a);
//     console.log(foo());
//
//     var a = 1;
//     function foo() {
//         return 2;
//     }
// }
//
// test();
//
// const in_f = logger => {
//     logger("logger");
// }
//
//
// in_f(wiadomość => console.log(wiadomość));
// in_f("ez");

// const age = [21, 18, 42, 40, 64, 63, 34];
// const maxWiek = age.reduce((maks, age) => (
//     age < maks ? age : maks
// ), 0);
//
// console.log(maxWiek);

//
//
// const mojaFunkcja = ({nazwa}) => {}
// const mojaFunkcja = (nazwa) => {}
// const mojaFunkcja = funkcja(nazwa) => {}
// function mojaFunkcja({nazwa}) {}
// const mojaFunkcja = function (nazwa) {}
// function mojaFunkcja(nazwa) {}
//
//
// console.log("Pierwsza linia\nDruga linia");
// console.log(2+5+"3")
//
//
// let count = 0;
//
// while (count < 5) {
//     console.log(count);
//     count++;
// }
// const liczba = (value, fn) => {
//     return  value > fn ? liczba(1, fn): fn(value);
// };
// liczba (10, wartość => console.log(wartość));
// console.log(10 > (wartość => console.log(wartość)));
//
// var topic = "JavaScript";
//
// if (topic) {
//     let topic = "Zareaguj";
//     console.log("blok", topic); // Zareaguj
// }
//
// console.log("globalny", topic); // JavaScript
//
// const one = ["1", "2", "3"];
// const twelve = one.filter(one => one[0] === "2");
// console.log(twelve);
//
//
// function example() {
//     let myVariable; // Bez użycia słowa kluczowego "var", "let" lub "const"
//     // console.log(typeof myVariable == null); // 10
//     console.log((typeof myVariable === typeof null) === (myVariable == null))
// }
//
// example();

// myVariable=20
// console.log(myVariable); // 10
//
// console.log(5 == "5");
// console.log(true == 1);
// console.log(null == undefined);
// console.log(isNaN(NaN));
// console.log(typeof (1+"3"));
// console.log(isNaN(typeof 'number'));
// console.log( [[[1]]]);
// console.log("ez \n ez");
//

const array = [[[1, 2, 3]]];
console.log(array[0]); // Output: [[1, 2, 3]]
console.log(array[0][0]); // Output: [1, 2, 3]
console.log(array[0][0][0]); // Output: 1


