<template>
  <div>
    <div v-if="user">
      <UserItem :item="user"/>
      <ReviewItems :items="reviews" :cols="2"></ReviewItems>
    </div>
    <div v-else>
      Пользователь не найден
    </div>
  </div>
</template>

<script>
import ReviewItems from '@/components/ReviewItems.vue'
import UserItem from "@/components/UserItem";
import {
  mapActions,
} from 'vuex'
export default {
  name: 'User',
  components: {
    ReviewItems,
    UserItem,
  },
  computed: {
    userId() {
      return this.$route.params['user_id'] || null;
    },
    user() {
      return this.$store.state.review.activeUser;
    },
    reviews() {
      return this.$store.getters.activeUserReviews;
    },
  },
  methods: {
    ...mapActions([
      'loadActiveUser',
    ]),
  },
  mounted() {
    this.loadActiveUser(this.userId);
  },
}
</script>