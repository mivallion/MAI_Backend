<template>
  <div class="row">
    <h3>Последние отзывы</h3>
    <div class="col col-md-8 lg-9">
      <ReviewItems :items="lastReviews"/>
    </div>
    <div class="col col-md-4 col-lg-3">
      <h3>Лучшие коты:</h3>
      <ListItems :items="popularCats" v-slot="props">
        <router-link :to="getCatRoute(props.item)" class="link-primary">
          <p class="lead">{{ props.item.name }}</p>
        </router-link>
      </ListItems>
    </div>
  </div>
</template>

<script>
import ListItems from '@/components/ListItems.vue'
import {
  mapGetters,
} from 'vuex'
import ReviewItems from "@/components/ReviewItems";

export default {
  name: 'Index',
  components: {
    ReviewItems,
    ListItems,
  },
  data() {
    return {};
  },
  methods: {
    getCatRoute(item) {
      return {
        name: 'Cat',
        params: {
          cat_id: item.id,
        },
      };
    },
  },
  computed: {
    ...mapGetters([
        'popularCats',
        'lastReviews'
    ]),
  },
  created() {
    this.$store.dispatch('loadReviews');
    this.$store.dispatch('loadCats');
  },
}
</script>