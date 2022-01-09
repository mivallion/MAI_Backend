<template>
  <div>
    <div v-if="cat">
      <CatItem :item="cat"/>
      <ReviewItems :items="reviews" :cols="2"></ReviewItems>
    </div>
    <div v-else>
      Кот не найден
    </div>
  </div>
</template>

<script>
import ReviewItems from '@/components/ReviewItems.vue'
import CatItem from "@/components/CatItem";
import {
  mapActions,
} from 'vuex'
export default {
  name: 'Cat',
  components: {
    ReviewItems,
    CatItem,
  },
  computed: {
    catId() {
      return this.$route.params['cat_id'] || null;
    },
    cat() {
      return this.$store.state.review.activeCat;
    },
    reviews() {
      return this.$store.getters.activeCatReviews;
    },
  },
  methods: {
    ...mapActions([
      'loadActiveCat',
    ]),
  },
  mounted() {
    this.loadActiveCat(this.catId);
  },
}
</script>