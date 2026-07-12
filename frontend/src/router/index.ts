import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Registration from '../views/Registration.vue'
import Login from '../views/Login.vue'
import Donation from '../views/Donation.vue'
import Participant from '../views/Participant.vue'
import PaymentSuccess from '../views/PaymentSuccess.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: Dashboard,
    },
    {
      path: '/registration',
      name: 'registration',
      component: Registration,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/donation',
      name: 'donation',
      component: Donation,
      meta: { requiresAuth: true },
    },
    {
      path: '/participant',
      name: 'participant',
      component: Participant,
      meta: { requiresAuth: true },
    },
    {
      path: '/payment-success',
      name: 'payment-success',
      component: PaymentSuccess,
    },
  ],
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access')

  if (to.meta.requiresAuth && !token) {
    next('/login')
  } else {
    next()
  }
})

export default router
