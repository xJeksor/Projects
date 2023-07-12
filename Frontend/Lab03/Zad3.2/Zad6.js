function camelize(str) {
    // usuń spacje z napisu i rozdziel słowa
    let words = str.replace(/\s+/g, ' ').trim().split(' ');

    // przekształć każde słowo, zaczynając od drugiego, do postaci z wielką literą na początku
    for (let i = 0; i < words.length; i++) {
            words[i] = words[i].charAt(0).toUpperCase() + words[i].slice(1);
    }

    // połącz słowa i zwróć wynik
    return words.join('');
}
