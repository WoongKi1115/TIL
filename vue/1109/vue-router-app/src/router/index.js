import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView'
import LoginView from '@/views/LoginView'
import NotFound404View from '@/views/NotFound404View'
import DogView from '@/views/DogView'
Vue.use(VueRouter)

const isLoggedIn = false

const routes = [
  {
    path: '/',
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
    path: '/hello/:userName', //userName이 동적 인자
    name: 'hello',
    component: HelloView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인 되어있음')
        next({name: 'home'})
      } else {
        next()
      }
    }
  },
  {
    path:'/404',
    name:'NotFound404View',
    component: NotFound404View
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView
  },
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
// router.beforeEach((to, from, next)=> {
//   // 로그인 여부
//   const isLoggedIn = false
//   // 로그인이 필요한 페이지
//   const authPages = ['hello', 'home', 'about']
//   //앞으로 이동할 페이지(to)가
//   //로그인이 필요한 사이트인지 확인
//   const isAuthRequired = authPages.includes(to.name)
//   if (isAuthRequired && !isLoggedIn) {
//     console.log('Login으로 이동')
//     next({name: 'login'})
//   } else {
//     // next인자가 없다면 to로 이동
//     console.log('to로 이동')
//     next()
//   }
// })


export default router
