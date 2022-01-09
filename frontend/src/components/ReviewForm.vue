<template>
  <form @submit.prevent="onSubmit">
    <textarea class="form-control" v-model="content"></textarea>
    <br>
    <button type='submit' class='btn btn-primary'>Сохранить</button>
  </form>
</template>

<script>
export default {
  name: "ReviewForm",
  props: {
    reviewId: Number,
  },
  data() {
    return {
      content: '',
    };
  },
  methods: {
    onSubmit() {
      if (this.content) {
        this.$store.dispatch('signInGoogleSuccess', {
          content: this.content,
          review_id: this.reviewId
        });
        this.content = '';
      }
    }
  }
}
</script>

<style scoped>

</style>