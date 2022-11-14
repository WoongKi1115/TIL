<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click="pickMenu">Pick Lunch</button>
    <p>{{pick}}</p>
    <br>
    <br>
    <h3>로또를 뽑아보자</h3>
    <button @click="tolotto">Pick Lotto</button>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
    name:"TheLunchView",
    data() {
        return {
            lunchMenu:['비빔밥', '육개장', '햄버거', '버섯훠거'],
            pick:''
        }
    },
    methods: {
        pickMenu() {
            this.pick= _.sample(this.lunchMenu)
            
        },
        tolunch() {
      this.$router.push({ name: 'lunch'})
    },
    }
}
</script>

<style>

</style>