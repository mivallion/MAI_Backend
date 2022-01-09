<template>
  <div class="container">
    <div class="navbar">
      <div class="navbar-brand">
        <img alt="Vue logo" src="@/assets/logo.png" href="/" style="height:50px;">
          Catbase
      </div>
      <div v-if="user" class="col-md-3 text-end">
        <button type="button" class="btn btn-outline-danger me-2" v-on:click="onClickSignOut">Выйти</button>
      </div>
      <div v-else class="col-md-3 text-end">
        <button type="button" class="btn btn-outline-primary me-2" v-on:click="onClickSignIn">Вход</button>
        <button type="button" class="btn btn-primary" v-on:click="onClickSignUp">Регистрация</button>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: 'Header',
  computed: {
    user() {
      return this.$store.state.review.currentUserId;
    },
  },
  methods: {
    ...mapActions([
      'signOut',
    ]),
    async onClickSignIn() {
      await this.$router.push({ name: 'SignIn' });
    },
    onClickSignUp() {
      this.$router.push({ name: 'SignUp' });
    },
    onClickSignOut() {
      this.signOut();
    },
  }
}
</script>