<template>
  <main class="form-signin">
    <button @click="onClick" class="btn btn-social-icon btn-google" type="button">
      <span class="fa fa-google"></span>
    </button>
  </main>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "GoogleSignInButton",
  methods: {
    ...mapActions([
      'signInGoogle',
    ]),
    async onClick () {
      const user = await this.$gAuth.signIn();
      const token = user.vc.access_token;
      await this.signInGoogle(token);
      if (this.$store.state.review.currentUserId != null)
        await this.$router.push({ name: 'Index' });
    },
  },
}
</script>

<style scoped>
</style>