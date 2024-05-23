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
                <div>
                    <div class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl">
    <div class="md:flex">
      <div class="p-8">
        <h2 class="uppercase tracking-wide text-lg text-indigo-500 font-semibold">Yangi Xarajat/Daromad Qo'shish</h2>
        <form @submit.prevent="submitExpense">
          <div class="mt-4">
            <label for="category" class="block text-sm font-medium text-gray-700">Kategoriya</label>
            <select v-model="category" id="category" class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md">
              <option value="">Kategoriya tanlang</option>
              <option value="sport">Sport</option>
              <option value="ovqatlanish">Ovqatlanish</option>
              <option value="transport">Transport</option>
              <option value="boshqa">Boshqa</option>
            </select>
          </div>
          <div class="mt-4">
            <label for="amount" class="block text-sm font-medium text-gray-700">Summa</label>
            <input type="number" v-model="amount" id="amount" class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md" required>
          </div>
          <div class="mt-4">
            <label for="description" class="block text-sm font-medium text-gray-700">Izoh</label>
            <textarea v-model="description" id="description" class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"></textarea>
          </div>
          <div class="mt-4">
            <label for="date" class="block text-sm font-medium text-gray-700">Sana</label>
            <input type="date" v-model="date" id="date" class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md" required>
          </div>
          <div class="mt-4">
            <button type="submit" class="w-full py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
              Qo'shish
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
                  <!-- <div
                    class="block border-4 w-64 rounded-lg bg-white text-center shadow-secondary-1 dark:bg-surface-dark dark:text-white text-surface"
                  >
                    <div
                      class="border-b-2 border-neutral-100 px-6 py-3 dark:border-white/10"
                    >
                      Xarajatlar
                    </div>
                    <div class="p-6">
                      <h5 class="mb-2 text-xl font-medium leading-tight">
                        Special title treatment
                      </h5>
                      <p class="mb-4 text-base">
                        With supporting text below as a natural lead-in to
                        additional content.
                      </p>
                      <button
                        type="button"
                        href="#"
                        class="inline-block rounded bg-primary px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-white shadow-primary-3 transition duration-150 ease-in-out hover:bg-primary-accent-300 hover:shadow-primary-2 focus:bg-primary-accent-300 focus:shadow-primary-2 focus:outline-none focus:ring-0 active:bg-primary-600 active:shadow-primary-2 dark:shadow-black/30 dark:hover:shadow-dark-strong dark:focus:shadow-dark-strong dark:active:shadow-dark-strong"
                        data-twe-ripple-init
                        data-twe-ripple-color="light"
                      >
                        Go somewhere
                      </button>
                    </div>
                    <div
                      class="border-t-2 border-neutral-100 px-6 py-3 dark:border-white/10 text-surface/75 dark:text-neutral-300"
                    >
                      Har bir xarajatlaringizni kiritib boring
                    </div>
                  </div> -->
                </div>
              </div>
              <div
                v-bind:class="{ hidden: openTab !== 2, block: openTab === 2 }"
              >
                <p>
                  Completely synergize resource taxing relationships via premier
                  niche markets. Professionally cultivate one-to-one customer
                  service with robust ideas.
                  <br />
                  <br />
                  Dynamically innovate resource-leveling customer service for
                  state of the art customer service.
                </p>
              </div>
              <div
                v-bind:class="{ hidden: openTab !== 3, block: openTab === 3 }"
              >
                <p>
                  Efficiently unleash cross-media information without
                  cross-media value. Quickly maximize timely deliverables for
                  real-time schemas.
                  <br />
                  <br />
                  Dramatically maintain clicks-and-mortar solutions without
                  functional solutions.
                </p>
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
export default {
  name: "pink-tabs",
  data() {
    return {
      openTab: 1,
      category: '',
      amount: '',
      description: '',
      date: ''
    };
  },
  methods: {
    toggleTabs: function (tabNumber) {
      this.openTab = tabNumber;
    },
    async submitExpense() {
      try {
        const expenseData = {
          category: this.category,
          amount: this.amount,
          description: this.description,
          date: this.date
        };
        const response = await axios.post('http://127.0.0.1:8000/api/v1/expense/', expenseData);
        console.log('Xarajat muvaffaqiyatli qo\'shildi:', response.data);
        // Clear form
        this.category = '';
        this.amount = '';
        this.description = '';
        this.date = '';
      } catch (error) {
        console.error('Xarajat qo\'shishda xatolik:', error);
      }
    }
  },
};
</script>
