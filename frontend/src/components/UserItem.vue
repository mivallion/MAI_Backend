<template>
  <div>
    <h1>{{ item.username }}</h1>
    <h2>#{{ item.id }}</h2>
    <p>Имя: {{ item.firstName }}</p>
    <p>Фамилия: {{ item.lastName }}</p>
    <p>Электронная почта: {{ item.email }}</p>
  </div>
</template>

<script>
import User from '@/models/User';

export default {
  name: "User",
  props: {
    item: User
  }
}
</script>

<style scoped>

</style>