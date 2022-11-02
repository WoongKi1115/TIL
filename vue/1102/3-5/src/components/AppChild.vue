<template>
  <div>
    <h1>AppChild</h1>
    <input type="text" v-model="childData" @input="fromChild">
    <h3>app: {{ appData }}</h3>
    <h3>parent: {{ parentData }}</h3>
    <h3>child: {{ childData }}</h3>
  </div>
</template>

<script>
export default {
    name:"AppChild",
    data() {
        return {
            childData:''
        }
    },
    props:{
        appData: String,
        parentData: String
    },
    methods: {
        fromChild() {
            this.$emit("from-child", this.childData)
        }
    }
}

</script>

<style>

</style>