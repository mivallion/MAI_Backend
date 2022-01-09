import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'font-awesome/css/font-awesome.min.css'
import 'bootstrap-social/bootstrap-social.css'
import GAuth from 'vue3-google-oauth2'
import App from './App.vue'

import store from './store'
import router from './router'

import { createApp } from "vue";

const gAuthOptions = { clientId: '69737495708-a6v5s6tjarn07abnv0mggpsjj3kq2khu.apps.googleusercontent.com', scope: 'email profile', prompt: 'consent', fetch_basic_profile: false  }
const app = createApp(App).use(router).use(store).use(GAuth, gAuthOptions);

app.config.productionTip = false;
app.mount("#app");
