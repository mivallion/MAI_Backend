<template>
  <div id="app">
    <template v-if="is404 || isSignIn || isSignUp">
      <router-view></router-view>
    </template>

    <template v-else>
      <Header></Header>
      <main>
        <div class="container">
          <router-view></router-view>
        </div>
      </main>
    </template>
  </div>
</template>

<script>
// import '@/styles/index.scss';
import Header from '@/components/Header.vue';

export default {
  name: 'App',
  components: {
    Header,
  },
  computed: {
    is404() {
      return this.$route.name === '404';
    },
    isSignIn() {
      return this.$route.name === 'SignIn';
    },
    isSignUp() {
      return this.$route.name === 'SignUp';
    },
  },
}
</script>