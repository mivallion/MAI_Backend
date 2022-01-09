<template>
  <ListItems :items="items" class="row">
    <template v-slot:default="props">
        <div class="col" :cols="itemCols">
          <ReviewItem :item="props.item"></ReviewItem>
        </div>
    </template>
  </ListItems>
</template>

<script>
import ListItems from "@/components/ListItems";
import ReviewItem from "@/components/ReviewItem";

export default {
  name: "ReviewItems",
  components: {
    ListItems,
    ReviewItem,
  },
  extends: ListItems,
  props: {
    cols: {
      type: Number,
      default: 1,
    },
  },
  computed: {
    itemCols() {
      return 12 / this.cols;
    },
  },
}
</script>

<style scoped>
</style>