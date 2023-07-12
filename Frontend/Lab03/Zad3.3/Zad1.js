function find_FirstNotRepeatedChar(str) {
    let charMap = new Map();

    for (let i = 0; i < str.length; i++) {
        let char = str.charAt(i);
        if (charMap.has(char)) {
            charMap.set(char, charMap.get(char) + 1);
        } else {
            charMap.set(char, 1);
        }
    }

    for (let i = 0; i < str.length; i++) {
        let char = str.charAt(i);
        if (charMap.get(char) === 1) {
            return char;
        }
    }
}


find_FirstNotRepeatedChar("abacddbec");