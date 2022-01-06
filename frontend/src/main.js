import Vue from 'vue'
import GSignInButton from 'vue-google-signin-button'
import App from './App'

Vue.config.productionTip = false

Vue.use(GSignInButton)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
