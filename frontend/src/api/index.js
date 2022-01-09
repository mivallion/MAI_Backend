import Review from '@/models/Review';
import Cat from '@/models/Cat';
import User from '@/models/User';
import axios from "axios";

// axios.defaults.headers.common['Authorization'] = localStorage.getItem('access_token') ? 'Bearer ' + localStorage.getItem('access_token') : null;

export default {
    async signInGoogle(token) {
        let user, accessToken, refreshToken;

        const res = await axios.post('http://localhost:8000/api/auth/login/google/', {
            access_token: token
        });
        const { data } = await res;
        user = data.user;
        accessToken = data.access_token;
        refreshToken = data.refresh_token;
        console.log(data);
        localStorage.setItem('access_token', accessToken);
        return { "accessToken": accessToken, "refreshToken": refreshToken, "user": user }
    },
    async signInSimple(username, password) {
        let user, accessToken, refreshToken;
        const res = await axios.post('http://localhost:8000/api/auth/login/', {
            username: username,
            password: password,
        });
        const { data } = await res;
        user = data.user;
        accessToken = data.access_token;
        refreshToken = data.refresh_token;
        console.log(data);
        return { "accessToken": accessToken, "refreshToken": refreshToken, "user": user }
    },
    async signUp(email, username, password) {
        let user, accessToken, refreshToken;

        await axios.post('http://localhost:8000/api/auth/registration/', {
            username: username,
            password1: password,
            password2: password,
            email: email,
        })
            .then(resp => {
                user = resp.data.user;
                accessToken = resp.data.access_token;
                refreshToken = resp.data.refresh_token;
            })
            .catch(err => {
                console.log(err.response);
            })
        return { "accessToken": accessToken, "refreshToken": refreshToken, "user": user }
    },
    async getReviews() {
        let items;
        await axios.get('http://localhost:8000/api/reviews/').
        then(resp => {
            items = resp.data.reviews;
        }).catch(err => {
            console.log(err.response);
        });
        return items.map((item) => Review.createFrom(item));
    },
    async getUsers() {
        let items;
        await axios.get('http://localhost:8000/api/users/').
        then(resp => {
            items = [...resp.data];
        }).catch(err => {
            console.log(err.response);
        });

        return items.map((item) => User.createFrom(item));
    },
    async getCats() {
        let items;
        await axios.get('http://localhost:8000/api/cats/').
        then(resp => {
            items = [...resp.data];
        }).catch(err => {
            console.log(err.response);
        });

        return items.map((item) => Cat.createFrom(item));
    },
    // getReview(id) {
    //
    // },
    // getCat(id) {
    //
    // },
    // getUser(id) {
    //
    // },
    // addReview() {
    //
    // },
    // updateReview(id, review) {
    //
    // },
    // deleteReview(id) {
    //
    // }
}