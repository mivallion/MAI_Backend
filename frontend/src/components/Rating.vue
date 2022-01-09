<template>
  <div class="mt-5 d-flex justify-content-between align-items-center">
    <h5 class="review-stat">{{ property }}</h5>
    <br>
    <div v-if="rating >= 5" class="small-ratings"> <i class="fa fa-star rating-color"></i> <i class="fa fa-star rating-color"></i> <i class="fa fa-star rating-color"></i> <i class="fa fa-star rating-color"></i> <i class="fa fa-star rating-color"></i></div>
    <div v-else-if="rating >= 4" class="small-ratings"> <i class="fa fa-star rating-color"></i> <i class="fa fa-star rating-color"></i> <i class="fa fa-star rating-color"></i> <i class="fa fa-star rating-color"></i> <i class="fa fa-star"></i></div>
    <div v-else-if="rating >= 3" class="small-ratings"> <i class="fa fa-star rating-color"></i> <i class="fa fa-star rating-color"></i> <i class="fa fa-star rating-color"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i></div>
    <div v-else-if="rating >= 2" class="small-ratings"> <i class="fa fa-star rating-color"></i> <i class="fa fa-star rating-color"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i></div>
    <div v-else-if="rating >= 1" class="small-ratings"> <i class="fa fa-star rating-color"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i></div>
    <div v-else class="small-ratings"> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i></div>
  </div>
</template>

<script>
export default {
  name: "Rating",
  props: {
    property: String,
    rating: Number,
  }
}
</script>

<style scoped>
body {
  background-color: #eef3f4
}

.height-100 {
  height: 100vh
}

.card {
  width: 380px;
  border: none;
  height: 280px
}

.ratings {
  margin-right: 10px
}

.ratings i {
  color: #cecece;
  font-size: 32px
}

.rating-color {
  color: #fbc634 !important
}

.review-count {
  font-weight: 400;
  margin-bottom: 2px;
  font-size: 24px !important
}

.small-ratings i {
  color: #cecece
}

.review-stat {
  font-weight: 300;
  font-size: 18px;
  margin-bottom: 2px
}
</style>