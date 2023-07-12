const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const PLANETS = {
    MERKURY: 0.2408467,
    WENUS: 0.61519726,
    ZIEMIA: 1,
    MARS: 1.8808158,
    JOWISZ: 11.862615,
    SATURN: 29.447498,
    URAN: 84.016846,
    NEPTUN: 164.79132
};

const AGE_SECONDS = 1000000000;
const SECONDS_PER_YEAR = 31557600;

function getAgeOnPlanet(planet, age) {
    const ageInYears = age / SECONDS_PER_YEAR;
    const ageOnPlanet = ageInYears / planet;
    return ageOnPlanet.toFixed(2);
}

rl.on('line', (age) => {
    rl.on('line', (planetName) => {
        const planet = PLANETS[planetName.toUpperCase()];
        if (!planet) {
            console.log('Invalid planet name');
            rl.close();
            return;
        }
        const ageOnPlanet = getAgeOnPlanet(planet, age);
        console.log(`${ageOnPlanet}`);
        rl.close();
    });
});