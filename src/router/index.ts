import { RouteRecordRaw, createRouter, createWebHashHistory } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "home" */ '../views/home/index.vue'),
  },
  {
    path: '/details',
    name: 'Product Details',
    component: () => import(/* webpackChunkName: "home" */ '../views/home/index.vue'),
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/about/index.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import(/* webpackChunkName: "login" */ '../views/login/index.vue'), // Ensure this matches the actual casing
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router
