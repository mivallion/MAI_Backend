<template>
  <div class="row" v-if="review">
    <div class="col col-md-8 col-lg-9">
      <h1>
        {{ review.title }}
      </h1>
      <p class="mb-4">
        {{ review.content }}
      </p>
      <Rating :property="'Общая оценка'" :rating="review.generalRating"/>
      <Rating :property="'Общительность'" :rating="review.sociability"/>
      <Rating :property="'Привлекательность'" :rating="review.attractiveness"/>
      <Rating :property="'Игривость'" :rating="review.playfulness"/>
    </div>
  </div>
</template>

<script>
import {
  mapActions,
  mapGetters,
} from 'vuex'
import Rating from "@/components/Rating";
export default {
  name: 'Review',
  components: {
    Rating
  },
  computed: {
    ...mapGetters([
      'nextReview',
      'prevReview',
    ]),
    reviewId() {
      return this.$route.params['review_id'] || null;
    },
    review() {
      return this.$store.state.review.activeReview;
    },
  },
  methods: {
    ...mapActions([
      'loadActiveReview',
    ]),
    getReviewRoute(item) {
      return {
        name: 'Review',
        params: {
          post_id: item.id,
        },
      };
    },
  },
  mounted() {
    this.loadActiveReview(this.reviewId);
  },
  watch: {
    reviewId(value) {
      this.loadActiveReview(value);
    },
  },
}
</script>