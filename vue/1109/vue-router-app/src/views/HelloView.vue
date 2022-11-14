<template>
  <div>
    <!-- userName는 router에 입력한 변수 명 -->
    <h1>hello, {{ userName }}</h1>
  </div>
</template>

<script>
export default {
    name: 'HelloView',
    data() {
        return {
            userName: this.$route.params.userName
        }
    },
    beforeRouteUpdate(to, from, next) {
      this.userName = to.params.userName
      next()
    }
}
</script>

<style>

</style>