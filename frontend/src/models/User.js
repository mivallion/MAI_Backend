export default class User
{
    constructor(id, username, firstName, lastName, email) {
        this.id = id;
        this.username = username;
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
    }

    static createFrom(data) {
        const {id, username, firstName, lastName, email} = data;
        return new this(id, username, firstName, lastName, email);
    }
}