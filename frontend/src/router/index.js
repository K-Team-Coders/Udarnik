import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    
    component: () => import(/* webpackChunkName: "about" */ '../views/MainPage.vue')
  },
  {
    path: '/mnemonic1/',
    name: 'mnemonic1',
    
    component: () => import(/* webpackChunkName: "about" */ '../views/Mnemonicscheme.vue')
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
