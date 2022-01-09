export default class Review
{
    constructor(id, title, content, generalRating, attractiveness, sociability, playfulness, user, cat) {
        this.id = id;
        this.title = title;
        this.content = content;
        this.generalRating = generalRating;
        this.attractiveness = attractiveness;
        this.sociability = sociability;
        this.playfulness = playfulness;
        this.user = user;
        this.cat = cat;
    }

    static createFrom(data) {
        const {id, attractiveness, sociability, playfulness} = data;
        const user = data.user_id;
        const cat = data.cat_id;
        const generalRating = data.general_rating;
        const content = data.review_text;
        const title = data.review_title;

        return new this(id, title, content, generalRating, attractiveness, sociability, playfulness, user, cat);
    }
}