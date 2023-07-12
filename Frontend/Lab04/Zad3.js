function answer(users) {
    return users.map(user => {
        const age = user.name.length * 10;
        return {
            [user.name]: user.likes,
            age: age
        };
    });
}

const myUsers = [
    { name: 'shark', likes: 'ocean' },
    { name: 'turtle', likes: 'pond' },
    { name: 'otter', likes: 'fish biscuits' }
];

console.log(answer(myUsers));