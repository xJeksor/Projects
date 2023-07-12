const students = [
    { name: 'Quincy', grade: 96 },
    { name: 'Jason', grade: 84 },
    { name: 'Alexis', grade: 100 },
    { name: 'Sam', grade: 65 },
    { name: 'Katie', grade: 90 }
];

function answer(students) {
    return students.filter(student => student.grade >= 84 && student.grade <= 95)
}

console.log(answer(students));