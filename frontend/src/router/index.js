import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores/auth';
import Home from '../views/Home.vue'
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import DefaultLayout from "../layouts/DefaultLayout.vue";
import GuestLayout from "../layouts/GueastLayout.vue";
import Calculation from "../pages/Calculation.vue"

const routes = [
  {
    path: "/",
    component: DefaultLayout,
    children: [
      {
        path: "/",
        name: "home",
        component: Home,
        meta: { requiresAuth: true }
      },
      {
        path: "/calculate",
        name: "calculation",
        component: Calculation,
      },
    ],
  },
  {
    path: "/guest",
    component: GuestLayout,
    children: [
      {
        path: "/login",
        name: "login",
        component: Login,
      },
      {
        path: "/register",
        name: "register",
        component: Register,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// router.beforeEach((to, from, next) => {
//   const authStore = useAuthStore();
//   if (to.matched.some(record => record.meta.requiresAuth) && !authStore.accessToken) {
//     next('/login');
//   } else {
//     next();
//   }
// });

export default router
