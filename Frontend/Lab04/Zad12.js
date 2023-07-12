function getValue(object, path) {
    const keys = path.split('.');
    const result =  keys.reduce((obj, key) => (obj && obj[key] !== undefined) ? obj[key] : null, object);
    return result ? result.length : null;
}


const obj = {
    person: {
        address: {
            street: 'Wiejska'
        },
        name: 'Tomasz'
    }
}
console.log(getValue(obj, 'person.address.street'));
console.log(getValue(obj, 'person.name'));
console.log(getValue(obj, 'person.lastName'));