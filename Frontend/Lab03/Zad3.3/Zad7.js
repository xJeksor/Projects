class Fraction {
    constructor(numerator, denumerator) {
        this.numerator = numerator;
        this.denumerator = denumerator;
    }

    multiplyBy(fractionOrNumber) {
        if (fractionOrNumber instanceof Fraction) {
            this.numerator *= fractionOrNumber.numerator;
            this.denumerator *= fractionOrNumber.denumerator;
        } else if (typeof fractionOrNumber === 'number') {
            this.numerator *= fractionOrNumber;
        }
    }

    static multiply(fraction1, fraction2) {
        const numerator = fraction1.numerator * fraction2.numerator;
        const denumerator = fraction1.denumerator * fraction2.denumerator;
        return new Fraction(numerator, denumerator);
    }

    print() {
        return `${this.numerator}/${this.denumerator}`;
    }
}

const u = new Fraction(1, 2);
const v = new Fraction(2, 3);

u.multiplyBy(v);
console.log(u.print());

u.multiplyBy(4);
console.log(u.print());

const x = new Fraction(3, 4);
const y = new Fraction(5, 6);

const z = Fraction.multiply(x, y);
console.log(z.print());
