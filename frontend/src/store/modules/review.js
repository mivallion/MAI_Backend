import Api from "@/api";

export default {
  state: {
    reviews: [],
    cats: [],
    users: [],
    activeReview: null,
    activeCat: null,
    activeUser: null,
    user: null,
    accessToken: null,
    refreshToken: null,
    currentUserId: null,
    currentUserName: null,
  },
  getters: {
    lastReviews(state) {
      return state.reviews.sort((a, b) => b.id - a.id).slice(0, 10);
    },
    popularCats(state) {
      return state.cats.sort((a, b) => b.generalRating - a.generalRating).slice(0, 10);
    },
    activeCatReviews(state) {
      if (!state.activeCat)
        return [];
      return state.reviews.filter((item) => Number(state.activeCat.id) === Number(item.cat));
    },
    activeUserReviews(state) {
      if (!state.activeUser)
        return [];
      return state.reviews.filter((item) => Number(state.activeUser.id) === Number(item.user));
    },
  },
  mutations:  {
    signOut(state) {
      state.accessToken = null;
      state.refreshToken = null;
      state.currentUserId = null;
      state.currentUserName = null;
    },
    setTokens(state, payload) {
      state.accessToken = payload.tokens.accessToken;
      state.refreshToken = payload.tokens.refreshToken;
      state.currentUserId = payload.tokens.user.pk;
      state.currentUserName = payload.tokens.user.username;
    },
    setReviews(state, payload) {
      state.reviews = payload.items;
    },
    setCats(state, payload) {
      state.cats = payload.items;
    },
    setUsers(state, payload) {
      state.users = payload.items;
    },
    setActiveCat(state, payload) {
      state.activeCat = payload;
    },
    setActiveReview(state, payload) {
      state.activeReview = payload;
    },
    setActiveUser(state, payload) {
      state.activeUser = payload;
    },
    // addComment(state, payload) {
    //   state.comments.push(payload);
    //   state.activeArticle.addComment(Comment.createFrom(payload));
    // },
  },
  actions: {
    async loadReviews({ commit }) {

      const items = await Api.getReviews();
      commit ('setReviews', {
        items
      });
      // let data;
      // await axios.get('http://localhost:8000/api/cats/').
      //   then(resp => {
      //     data = resp.data;
      // }).catch(err => {
      //   console.log(err.response);
      // });
      // console.log(data);
      // console.log(commit);
      // console.log(state);
    },
    async loadCats({ commit }) {
      const items = await Api.getCats();
      commit ('setCats', {
        items
      });
    },
    async loadUsers({ commit }) {
      const items = await Api.getUsers();
      commit ('setUsers', {
        items
      });
    },
    async loadActiveCat(context, id) {
      await context.dispatch('loadCats')
      await context.dispatch('loadReviews')

      let cat = context.state.cats.find((item) => {
        return Number(item.id) === Number(id);
      });
      context.commit('setActiveCat', cat);
    },
    async loadActiveReview(context, id) {
      await context.dispatch('loadReviews')

      let review = context.state.reviews.find((item) => {
        return Number(item.id) === Number(id);
      });
      context.commit('setActiveReview', review);
    },
    async loadActiveUser(context, id) {
      await context.dispatch('loadUsers')

      let user = context.state.users.find((item) => {
        return Number(item.id) === Number(id);
      });

      context.commit('setActiveUser', user);
    },
    async signInGoogle({ commit }, token) {
      const tokens = await Api.signInGoogle(token);
      commit ('setTokens', {
        tokens
      });
    },
    async signIn({ commit }, authPayload) {
      const tokens = await Api.signInSimple(authPayload.username, authPayload.password);
      commit ('setTokens', {
        tokens
      });
    },
    async signUp({ commit }, email, login, password) {
      const tokens = await Api.signUp(email, login, password);
      commit ('setTokens', {
        tokens
      });
    },
    async signOut({ commit }) {
      commit ('signOut', {});
    },
  },
}
