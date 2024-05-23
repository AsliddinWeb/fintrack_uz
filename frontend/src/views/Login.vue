<template lang="">
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <h2
        class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900"
      >
        Kirish
      </h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" @submit.prevent="login">
        <div>
          <label
            for="text"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Foydalanuvchi nomi</label
          >
          <div class="mt-2">
            <input
              id="text"
              name="username"
              type="text"
              autocomplete="text"
              v-model="username"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label
              for="password"
              class="block text-sm font-medium leading-6 text-gray-900"
              >Parol</label
            >
          </div>
          <div class="mt-2">
            <input
              id="password"
              name="password"
              type="password"
              autocomplete="current-password"
              v-model="password"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
          <!-- <div class="text-sm py-2">
            <a
              href="#"
              class="font-semibold text-indigo-600 hover:text-indigo-500"
              >Parolni tiklash</a
            >
          </div> -->
        </div>

        <div>
          <button
            type="submit"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Tizimga kirish
          </button>
        </div>
        <div v-if="loginError" class="mt-4 text-red-500">
          {{ loginError }}
        </div>
      </form>

      <p class="mt-10 text-center text-sm text-gray-500">
        Sizda profil yo'qmi?
        <router-link
          to="/register"
          class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500"
          >Ro'yhatdan o'tish</router-link
        >
      </p>
    </div>
  </div>
</template>
<script>
import { useAuthStore } from '../stores/auth';

export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  computed: {
    loginError() {
      const authStore = useAuthStore();
      return authStore.loginError;
    }
  },
  methods: {
    async login() {
      const authStore = useAuthStore();
      const loginSuccessful = await authStore.login(this.username, this.password);
      if (loginSuccessful) {
        this.$router.push('/');
      }
    }
  }
};
</script>
<style lang=""></style>
