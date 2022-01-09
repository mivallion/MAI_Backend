<template>
  <main class="form-signin">
    <form>
      <img class="mb-4 img-responsive center-block" src="@/assets/logo.png">
      <h1 class="h3 mb-3 fw-normal">Вход</h1>
      <div class="form-floating">
        <input type="text" class="form-control" id="floatingInput" v-model="username">
        <label for="floatingInput">Имя пользователя</label>
      </div>
      <div class="form-floating">
        <input type="password" class="form-control" id="floatingPassword" v-model="password">
        <label for="floatingPassword">Пароль</label>
      </div>
      <button class="w-100 btn btn-lg btn-primary" type="submit" @click="onSubmit">Вход</button>
      <GoogleSignInButton/>
      <button class="btn btn-social-icon btn-github" type="button">
        <span class="fa fa-github"></span>
      </button>
    </form>
  </main>
</template>

<script>
import GoogleSignInButton from "@/components/GoogleSignInButton";
import {mapActions} from "vuex";

export default {
  name: "SignIn",
  data() {
    return {
      username: '',
      password: ''
    };
  },
  components: {
    GoogleSignInButton,
  },
  methods: {
    ...mapActions([
      'signIn',
    ]),
    async onSubmit() {
      await this.signIn({username: this.username, password: this.password});
      this.username = '';
      this.password = '';
      if (this.$store.state.review.currentUserId != null)
        await this.$router.push({ name: 'Index' });
    }
  }
}
</script>

<style scoped>
.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

.form-signin .checkbox {
  font-weight: 400;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
.bd-placeholder-img {
  font-size: 1.125rem;
  text-anchor: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
}

@media (min-width: 768px) {
  .bd-placeholder-img-lg {
    font-size: 3.5rem;
  }
}
</style>