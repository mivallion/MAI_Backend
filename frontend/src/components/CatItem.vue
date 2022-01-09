<template>
  <div class="CatInfo">
    <h1>{{ item.name }}</h1>
    <h2>#{{ item.id }}</h2>
    <p>Год рождения: {{ item.birthYear }}</p>
  </div>
</template>

<script>
import Cat from '@/models/Cat';

export default {
  name: "Cat",
  props: {
    item: Cat,
  }
}
</script>

<style scoped>
</style>