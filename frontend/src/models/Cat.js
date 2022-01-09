export default class Cat
{
    constructor(id, birthYear, name) {
        this.id = id;
        this.birthYear = birthYear;
        this.name = name;
    }

    static createFrom(data) {
        const {id, name} = data;
        const birthYear = data.birth_year;
        return new this(id, birthYear, name);
    }
}