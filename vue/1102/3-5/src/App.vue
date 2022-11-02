<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>App</h1>
    <hr>
    <input type="text" v-model="appData">
    <h3>Parent : {{parentData}}</h3>
    <h3>Child : {{childData}}</h3>
    <AppParent :app-data="appData" @from-parent="fromParent" @from-child="fromChild"/>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import AppParent from './components/AppParent.vue';
export default {
  name: 'App',
  components: {
    AppParent,
  },
  data() {
    return {
      appData: '',
      parentData:'',
      childData:'',
    }
  },
  methods: {
    fromParent(pd) {
      this.parentData = pd
    },
    fromChild(cd) {
      this.childData = cd
  
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
