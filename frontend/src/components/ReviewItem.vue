<template>
  <div class="card review-item-card" :title="item.title">
    <p class="review-title"><b>{{ item.title }}</b></p>
    <p class="review-content">{{ item.content }}</p>
    <Rating :property="'Общая оценка'" :rating="item.generalRating"/>
    <router-link :to="getReviewRoute" class="card-link">
      Подробнее
    </router-link>
  </div>
</template>

<script>
import Review from '@/models/Review';
import Rating from "@/components/Rating";

export default {
  name: "ReviewItem",
  components: {
    Rating
  },
  props: {
    item: Review,
  },
  computed: {
    getReviewRoute() {
      return {
        name: 'Review',
        params: {
          review_id: this.item.id,
        },
      };
    },
  }
}
</script>

<style scoped>
.review-title {
  font-weight: 300;
  font-size: 18px;
  margin-bottom: 2px
}
.review-content {
  font-weight: 300;
  font-size: 18px;
  margin-bottom: 2px
}
.card {
  width: 18rem;
  margin-bottom: 1rem;
  padding: 1rem;
}
</style>