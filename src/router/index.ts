import { RouteRecordRaw, createRouter, createWebHashHistory } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "home" */ '../views/home/index.vue'),
  },
  {
    path: '/details/:id',
    name: 'Product Details',
    component: () => import(/* webpackChunkName: "home" */ '../views/details/index.vue'),
  },
  {
    path: '/cart',
    name: 'Cart Details',
    component: () => import(/* webpackChunkName: "cart" */ '../views/cart/index.vue'),
  },
  {
    path: '/checkout',
    name: 'Checkout',
    component: () => import(/* webpackChunkName: "checkout" */ '../views/checkout/index.vue'),
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
