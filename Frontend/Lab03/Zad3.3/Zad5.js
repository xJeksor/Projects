const newMovie1 = {
    country: 'USA',
    title: 'Zielona Mila',
    director: 'Frank Darabont',
    year: 1999,
    genre: 'Dramat'
};

delete newMovie1.country;
delete newMovie1.year;
delete newMovie1.genre;

console.log(newMovie1);
