const movie = {
    title: 'Nietykalni',
    directors: ['Olivier Nakache', 'Éric Toledano'],
    country: 'Francja',
    year: 2011,
    actors: {
        Philippe: 'François Cluzet',
        Dris: 'Omar Sy',
        Yvonne: 'Anne Le Ny'
    }
};

const defaultValues = {
    title: "Nieznany tytuł",
    directors: [],
    country: "Nieznany kraj",
    year: "Nieznany rok",
    actors: {}
};

Object.keys(movie).forEach(key => {
    if (!movie[key]) {
        movie[key] = defaultValues[key];
    }
});

const { title, directors, actors } = movie;
const director1 = directors[0];
const DrisRole = actors.Dris;

console.log(title); // Nietykalni
console.log(director1); // Olivier Nakache
console.log(DrisRole); // Omar Sy

//Testowanie
movie.title = ``;
movie.year = null;

Object.keys(movie).forEach(key => {
    if (!movie[key]) {
        movie[key] = defaultValues[key];
    }
});

console.log(`\n` + movie.title); // Nieznany tytuł
console.log(movie.year); // Nieznany rok
