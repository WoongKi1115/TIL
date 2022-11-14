<template>
  <div class="about">
    <h1>This is an about page</h1>
    <!-- 선언적 방식 -->
    <router-link :to="{ name:'home'}">Home</router-link> 
    <!-- 프로그래밍 방식 -->
    <button @click="tohome">홈으로!</button>
    <input type="text"
    v-model="inputData"
    @keyup.enter="goToHello">
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  methods: {
    tohome() {
      this.$router.push({ name: 'home'})
    },
    goToHello() {
      this.$router.push({name:'hello', params: {userName:this.inputData}})
    }
  },
  data() {
    return {
      inputData: null
    }
  },
  

}
</script>