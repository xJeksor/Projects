function answer(abc) {
    return abc.reduce((acc, curr) => ({...acc, [curr.id]: curr}), {});
}
const abc = [
    {
        id: 'abc',
        name: 'Ala'
    },
    {
        id: 'def',
        name: 'Tomek'
    },
    {
        id: 'ghi',
        name: 'Jan'
    }
];
console.log(answer(abc));
