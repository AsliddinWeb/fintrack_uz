<template>
  <div class="max-w-7xl mx-auto px-2 pt-5 sm:px-6 lg:px-4 lg:pt-20">
    <div class="flex flex-wrap">
      <div class="w-full">
        <ul class="flex mb-0 list-none flex-wrap pt-3 pb-4 flex-row">
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
            <a
              class="text-xs font-bold uppercase cursor-pointer px-5 py-3 shadow-lg rounded flex items-center justify-center leading-normal"
              v-on:click="toggleTabs(1)"
              v-bind:class="{
                'text-gray-800 bg-white': openTab !== 1,
                'text-white bg-gray-800': openTab === 1,
              }"
            >
              Harajatlar
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M15.75 15.75V18m-7.5-6.75h.008v.008H8.25v-.008Zm0 2.25h.008v.008H8.25V13.5Zm0 2.25h.008v.008H8.25v-.008Zm0 2.25h.008v.008H8.25V18Zm2.498-6.75h.007v.008h-.007v-.008Zm0 2.25h.007v.008h-.007V13.5Zm0 2.25h.007v.008h-.007v-.008Zm0 2.25h.007v.008h-.007V18Zm2.504-6.75h.008v.008h-.008v-.008Zm0 2.25h.008v.008h-.008V13.5Zm0 2.25h.008v.008h-.008v-.008Zm0 2.25h.008v.008h-.008V18Zm2.498-6.75h.008v.008h-.008v-.008Zm0 2.25h.008v.008h-.008V13.5ZM8.25 6h7.5v2.25h-7.5V6ZM12 2.25c-1.892 0-3.758.11-5.593.322C5.307 2.7 4.5 3.65 4.5 4.757V19.5a2.25 2.25 0 0 0 2.25 2.25h10.5a2.25 2.25 0 0 0 2.25-2.25V4.757c0-1.108-.806-2.057-1.907-2.185A48.507 48.507 0 0 0 12 2.25Z"
                />
              </svg>
            </a>
          </li>
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
            <a
              class="text-xs flex font-bold cursor-pointer uppercase px-5 py-3 shadow-lg rounded items-center justify-center leading-normal"
              v-on:click="toggleTabs(3)"
              v-bind:class="{
                'text-gray-800 bg-white': openTab !== 3,
                'text-white bg-gray-800': openTab === 3,
              }"
            >
              Daromadlar
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M15.75 15.75V18m-7.5-6.75h.008v.008H8.25v-.008Zm0 2.25h.008v.008H8.25V13.5Zm0 2.25h.008v.008H8.25v-.008Zm0 2.25h.008v.008H8.25V18Zm2.498-6.75h.007v.008h-.007v-.008Zm0 2.25h.007v.008h-.007V13.5Zm0 2.25h.007v.008h-.007v-.008Zm0 2.25h.007v.008h-.007V18Zm2.504-6.75h.008v.008h-.008v-.008Zm0 2.25h.008v.008h-.008V13.5Zm0 2.25h.008v.008h-.008v-.008Zm0 2.25h.008v.008h-.008V18Zm2.498-6.75h.008v.008h-.008v-.008Zm0 2.25h.008v.008h-.008V13.5ZM8.25 6h7.5v2.25h-7.5V6ZM12 2.25c-1.892 0-3.758.11-5.593.322C5.307 2.7 4.5 3.65 4.5 4.757V19.5a2.25 2.25 0 0 0 2.25 2.25h10.5a2.25 2.25 0 0 0 2.25-2.25V4.757c0-1.108-.806-2.057-1.907-2.185A48.507 48.507 0 0 0 12 2.25Z"
                />
              </svg>
            </a>
          </li>
        </ul>
        <div
          class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded"
        >
          <div class="px-4 py-5 flex-auto">
            <div class="tab-content tab-space">
              <div
                v-bind:class="{ hidden: openTab !== 1, block: openTab === 1 }"
              >
                <div
                  class="max-w-sm mx-auto bg-white rounded-xl shadow-md overflow-hidden"
                >
                  <div class="md:flex">
                    <div class="p-8">
                      <h2
                        class="uppercase tracking-wide text-lg text-indigo-500 font-semibold"
                      >
                        Yangi Xarajatlarni Qo'shish
                      </h2>
                      <form @submit.prevent="submitExpense">
                        <div class="mt-4">
                          <label
                            for="category"
                            class="block text-sm font-medium text-gray-700"
                            >Kategoriya</label
                          >
                          <select
                            v-model="categoryEx"
                            id="category"
                            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                          >
                            <option value="">Kategoriya tanlang</option>
                            <option
                              v-for="cat in categories"
                              :key="cat.id"
                              :value="cat.id"
                            >
                              {{ cat.name }}
                            </option>
                          </select>
                        </div>
                        <div class="mt-4">
                          <label
                            for="amount"
                            class="block text-sm font-medium text-gray-700"
                            >Summa</label
                          >
                          <input
                            type="number"
                            v-model="amount"
                            id="amount"
                            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                            required
                          />
                        </div>
                        <div class="mt-4">
                          <label
                            for="description"
                            class="block text-sm font-medium text-gray-700"
                            >Izoh</label
                          >
                          <textarea
                            v-model="description"
                            id="description"
                            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                          ></textarea>
                        </div>
                        <div class="mt-4">
                          <label
                            for="date"
                            class="block text-sm font-medium text-gray-700"
                            >Sana</label
                          >
                          <input
                            type="date"
                            v-model="date"
                            id="date"
                            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                            required
                          />
                        </div>
                        <div class="mt-4">
                          <button
                            type="submit"
                            class="w-full py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                          >
                            Qo'shish
                          </button>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
              <div
                v-bind:class="{ hidden: openTab !== 3, block: openTab === 3 }"
              >
                <div
                  class="max-w-sm mx-auto bg-white rounded-xl shadow-md overflow-hidden"
                >
                  <div class="md:flex">
                    <div class="p-8">
                      <h2
                        class="uppercase tracking-wide text-lg text-indigo-500 font-semibold"
                      >
                        Yangi Daromadlarni Qo'shish
                      </h2>
                      <form @submit.prevent="submitIncome">
                        <div class="mt-4">
                          <label
                            for="category"
                            class="block text-sm font-medium text-gray-700"
                            >Kategoriya</label
                          >
                          <select
                            v-model="categoryIn"
                            id="category"
                            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                          >
                            <option value="">Kategoriya tanlang</option>
                            <option
                              v-for="cat in incomeCategories"
                              :key="cat.id"
                              :value="cat.id"
                            >
                              {{ cat.name }}
                            </option>
                          </select>
                        </div>
                        <div class="mt-4">
                          <label
                            for="amount"
                            class="block text-sm font-medium text-gray-700"
                            >Summa</label
                          >
                          <input
                            type="number"
                            v-model="amount"
                            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                            required
                          />
                        </div>
                        <div class="mt-4">
                          <label
                            for="description"
                            class="block text-sm font-medium text-gray-700"
                            >Izoh</label
                          >
                          <textarea
                            v-model="description"
                            id="description"
                            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                          ></textarea>
                        </div>
                        <div class="mt-4">
                          <label
                            for="date"
                            class="block text-sm font-medium text-gray-700"
                            >Sana</label
                          >
                          <input
                            type="date"
                            v-model="date"
                            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                            required
                          />
                        </div>
                        <div class="mt-4">
                          <button
                            type="submit"
                            class="w-full py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                          >
                            Qo'shish
                          </button>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import axiosInstance from "../axios";

export default {
  name: "pink-tabs",
  data() {
    return {
      openTab: 1,
      categoryEx: "",
      categoryIn: "",
      amount: "",
      description: "",
      date: "",
      categories: [],
      incomeCategories: []
    };
  },
  async created() {
    await this.loadCategories();
    await this.loadIncomeCategories();
  },
  methods: {
    toggleTabs: function (tabNumber) {
      this.openTab = tabNumber;
    },
    async loadCategories() {
      try {
        const response = await axiosInstance.get('/expense/categories/');
        this.categories = response.data;
      } catch (error) {
        console.error('Kategoriyalarni yuklashda xatolik:', error);
      }
    },
    async loadIncomeCategories() {
      try {
        const response = await axiosInstance.get('/income/categories/');
        this.incomeCategories = response.data;
      } catch (error) {
        console.error('Kategoriyalarni yuklashda xatolik:', error);
      }
    },
    async submitExpense() {
      try {
        const expenseData = {
          category: this.categoryEx,
          amount: this.amount,
          description: this.description,
          date: this.date
        };
        const response = await axiosInstance.post('/expense/', expenseData);
        console.log('Xarajat muvaffaqiyatli qo\'shildi:', response.data);
        // Clear form
        this.category = '';
        this.amount = '';
        this.description = '';
        this.date = '';
        this.$router.push('/');

      } catch (error) {
        console.error('Xarajat qo\'shishda xatolik:', error);
      }
    },
    async submitIncome() {
      try {
        const incomeData = {
          category: this.categoryIn,
          amount: this.amount,
          description: this.description,
          date: this.date
        };
        const response = await axiosInstance.post('/income/', incomeData);
        console.log('Xarajat muvaffaqiyatli qo\'shildi:', response.data);
        // Clear form
        this.category = '';
        this.amount = '';
        this.description = '';
        this.date = '';
        this.$router.push('/');

      } catch (error) {
        console.error('Xarajat qo\'shishda xatolik:', error);
      }
    }
  },
};
</script>
