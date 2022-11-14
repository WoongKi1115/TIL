import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TheLunchView from '@/views/TheLunchView'
import TheLottoView from '@/views/TheLottoView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/lunch',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/lunch',
    name: 'lunch',
    component: TheLunchView
  },
  {
    path: '/lotto/:num',
    name: 'lotto',
    component: TheLottoView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
