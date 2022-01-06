<template>
  <div id="app">
    <div class="container">
      <div class="columns" style="margin-top: 100px;">
        <div class="column col-2 centered">
          <!-- Если user - пустой объект, то отображаем кнопку
          входа через Google -->
          <g-signin-button
            v-if="isEmpty(user)"
            :params="googleSignInParams"
            @success="onGoogleSignInSuccess"
            @error="onGoogleSignInError"
          >
            <button class="btn btn-block btn-success">
              Google Signin
            </button>
          </g-signin-button>
          <user-panel v-else :user="user"></user-panel>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import UserPanel from '@/components/UserPanel'

axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

export default {
  name: 'App',
  components: {
    UserPanel
  },
  data () {
    return {
      user: {},
      googleSignInParams: {
        client_id: '69737495708-a6v5s6tjarn07abnv0mggpsjj3kq2khu.apps.googleusercontent.com'
      }
    }
  },
  methods: {
    onGoogleSignInSuccess (resp) {
      console.log(resp)
      const token = resp.vc.access_token
      // После успешного входа через Google,
      // отправляем токен доступа на бэкэнд и получаем взамен
      // пользователя и JWT токен
      // P.S. JWT токен в нашем примере не нужен, поэтому его не сохраняем
      axios.post('http://localhost:8000/api/auth/login/google/', {
        access_token: token
      })
        .then(resp => {
          this.user = resp.data.user
          localStorage.access_token = resp.data.access_token
          localStorage.refresh_token = resp.data.refresh_token
        })
        .catch(err => {
          console.log(err.response)
        })
    },
    onGoogleSignInError (error) {
      console.log('OH NOES', error)
    },
    isEmpty (obj) {
      return Object.keys(obj).length === 0
    }
  }
}
</script>
