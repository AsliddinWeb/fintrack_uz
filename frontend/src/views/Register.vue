<template lang="">
    <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <h2
        class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900"
      >
        Ro'yhatdan o'tish
      </h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" @submit.prevent="register">
        <div>
          <label
            for="text"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Ism</label
          >
          <div class="mt-2">
            <input
              type="text"
              placeholder="Ism"
              v-model="first_name"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>
        <div>
          <label
            for="text"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Familiya</label
          >
          <div class="mt-2">
            <input
              type="text"
              placeholder="Familiya"
              v-model="last_name"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>
        <div>
          <label
            for="username"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Username</label
          >
          <div class="mt-2">
            <input
              type="text"
              placeholder="username"
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
              type="password"
              v-model="password"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Davom etish
          </button>
        </div>
      </form>

      <p class="mt-10 text-center text-sm text-gray-500">
        Davom etish tugmasini bosish orqali siz 
        <a
          href="#"
          class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500"
          >ma'lumotlarni qayta ishlash shartlariga rozilik bildirasiz </a
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
      first_name:"",
      last_name:"",
      username: '',
      password: ''
    };
  },
  methods: {
    async register() {
      const authStore = useAuthStore();
      await authStore.register(this.username, this.password);
      if (authStore.accessToken) {
        this.$router.push('/');
      }
    }
  }
};
</script>
<style lang="">
    
</style>