<template>
  <div>
    <h1>App Parent</h1>
    <input type="text" v-model="parentData" @input="fromParent">
    <h3>App : {{appData}}</h3>
    <h3>Parent : {{parentData}}</h3>
    <h3>Child : {{childData}}</h3>
    <AppChild :app-data="appData" :parent-data="parentData" @from-child="fromChild"/>
  </div>
</template>

<script>
import AppChild from './AppChild.vue';
export default {
    components:{
        AppChild,
    },
    props:{
        appData: String
    },
    data() {
        return {
            parentData: "",
            childData: ""
        }
    },
    methods :{
        fromParent() {
            this.$emit("from-parent", this.parentData)
        },
        fromChild(cd) {
            this.childData = cd
            this.$emit("from-child", cd)
        }
    },
    name:"AppParent",
}
</script>

<style>

</style>