<template>
  <div class="chartt">
    <!-- <Header /> -->
    <div class="relative">
      <div
        class="relative max-w-7xl mx-auto px-2 pt-6 sm:px-6 lg:px-4 lg:pt-20"
      >
        <div
          class="mx-auto grid max-w-[40rem] grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3"
        >
          <div class="flex flex-col lg:pb-6">
            <h1
              class="mt-4 text-4xl font-extrabold leading-none tracking-tight text-slate-900 sm:text-5xl sm:leading-[3.5rem]"
            >
              Finance Tracker
            </h1>
            <div class="order-first flex items-center gap-2">
              <p class="text-base font-semibold leading-7 text-slate-500">
                Kirim-chiqim hisoboti
              </p>
            </div>
            <p class="mt-6 text-base leading-7 text-slate-700">
              FinTrack Uz sizning xarajatlaringizni, daromadlaringizni,
              qarzlaringizni va boshqa moliyaviy ma'lumotlaringizni bir joyda
              saqlash va ularni samarali boshqarish imkonini beradi.
            </p>
            <div class="flex flex-wrap gap-6 mt-6">
              <div class="flex items-center text-sm font-medium text-slate-500">
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
                    d="M2.25 18.75a60.07 60.07 0 0 1 15.797 2.101c.727.198 1.453-.342 1.453-1.096V18.75M3.75 4.5v.75A.75.75 0 0 1 3 6h-.75m0 0v-.375c0-.621.504-1.125 1.125-1.125H20.25M2.25 6v9m18-10.5v.75c0 .414.336.75.75.75h.75m-1.5-1.5h.375c.621 0 1.125.504 1.125 1.125v9.75c0 .621-.504 1.125-1.125 1.125h-.375m1.5-1.5H21a.75.75 0 0 0-.75.75v.75m0 0H3.75m0 0h-.375a1.125 1.125 0 0 1-1.125-1.125V15m1.5 1.5v-.75A.75.75 0 0 0 3 15h-.75M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Zm3 0h.008v.008H18V10.5Zm-12 0h.008v.008H6V10.5Z"
                  />
                </svg>
                <span class="ml-2.5">Xarajatlar</span>
              </div>
              <div class="flex items-center text-sm font-medium text-slate-500">
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
                    d="M21 12a2.25 2.25 0 0 0-2.25-2.25H15a3 3 0 1 1-6 0H5.25A2.25 2.25 0 0 0 3 12m18 0v6a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 18v-6m18 0V9M3 12V9m18 0a2.25 2.25 0 0 0-2.25-2.25H5.25A2.25 2.25 0 0 0 3 9m18 0V6a2.25 2.25 0 0 0-2.25-2.25H5.25A2.25 2.25 0 0 0 3 6v3"
                  />
                </svg>
                <span class="ml-2.5">Daromadlar</span>
              </div>
              <div class="flex items-center text-sm font-medium text-slate-500">
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

                <span class="ml-2.5">Kreditlar</span>
              </div>
            </div>
            <div class="mt-10 flex flex-wrap gap-4">
              <router-link
                to="/calculate"
                class="inline-flex justify-center rounded-lg text-sm font-semibold py-3 px-4 bg-slate-900 text-white hover:bg-slate-700"
              >
                <span
                  ><span class="inline-flex items-center whitespace-nowrap"
                    ><span class="mr-2">Hisob-kitob</span>
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
                    </svg> </span></span
              ></router-link>
              <!-- <a href="https://catalyst.tailwindui.com/docs" class="inline-flex justify-center rounded-lg text-sm font-semibold py-3 px-4 bg-white/0 text-slate-900 ring-1 ring-slate-900/10 hover:bg-white/25 hover:ring-slate-900/15 whitespace-nowrap" target="_blank">
                  <span>Xarajatlar<span aria-hidden="true" class="text-black/25">→</span></span></a> -->
            </div>
          </div>
          <div class="relative lg:col-span-2 border-2 rounded-md p-4">
            <div class="z-0 hidden md:block">
              <ul class="flex mb-0 list-none flex-wrap pt-3 pb-4 flex-row">
                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                  <a
                    class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal"
                    v-on:click="toggleTabs(1)"
                    v-bind:class="{
                      'text-pink-600 bg-white': openTab !== 1,
                      'text-white bg-pink-600': openTab === 1,
                    }"
                  >
                    Kunlik
                  </a>
                </li>
                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                  <a
                    class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal"
                    v-on:click="toggleTabs(2)"
                    v-bind:class="{
                      'text-pink-600 bg-white': openTab !== 2,
                      'text-white bg-pink-600': openTab === 2,
                    }"
                  >
                    Haftalik
                  </a>
                </li>
                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                  <a
                    class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal"
                    v-on:click="toggleTabs(3)"
                    v-bind:class="{
                      'text-pink-600 bg-white': openTab !== 3,
                      'text-white bg-pink-600': openTab === 3,
                    }"
                  >
                    Oylik
                  </a>
                </li>
                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                  <a
                    class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal"
                    v-on:click="toggleTabs(4)"
                    v-bind:class="{
                      'text-pink-600 bg-white': openTab !== 4,
                      'text-white bg-pink-600': openTab === 4,
                    }"
                  >
                    Yillik
                  </a>
                </li>
              </ul>
              <FinanceChart
                v-if="chartData"
                :chartData="chartData"
                :chartOptions="chartOptions"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "../components/Header/Header.vue";
import axios from "axios";
import FinanceChart from "../components/charts/FinanceChart.vue";

export default {
  name: "Home",
  components: {
    FinanceChart,
    Header,
  },
  data() {
    return {
      chartData: null,
      chartOptions: null,
      openTab: 1,
      currentDate: ''
    };
  },
  methods: {
    async fetchChartData(start_date, end_date) {
      try {
        const response = await axios.get(
          `/finance-data.json`
        );
        if (response.data) {
          const financeData = response.data;
          console.log(financeData.labels);

          const totalIncome = financeData.incomes.reduce((a, b) => a + b, 0);
          const totalExpenses = financeData.expenses.reduce((a, b) => a + b, 0);

          this.chartData = {
            labels: financeData.labels,
            datasets: [
              {
                label: "Kirimlar",
                backgroundColor: "#42A5F5",
                data: financeData.incomes,
              },
              {
                label: "Chiqimlar",
                backgroundColor: "#FF6384",
                data: financeData.expenses,
              },
            ],
          };

          this.chartOptions = {
            responsive: true,
            maintainAspectRatio: false,
            cutout: "50%", // Ichi bo'sh qilish uchun kesim foizini belgilaysiz
            plugins: {
              legend: {
                position: "top",
              },
              tooltip: {
                callbacks: {
                  label: function (tooltipItem) {
                    return tooltipItem.label + ": " + tooltipItem.raw;
                  },
                },
              },
              centerText: {
                text1: `Daromadlar: ${totalIncome}`,
                text2: `Xarajatlar: ${totalExpenses}`,
                fontStyle: "Arial",
                color1: "#42A5F5",
                color2: "#FF6384",
                sidePadding: 20,
              },
            },
          };

          console.log(this.chartData); // chartData ni konsolda ko'rsatish
        } else {
          console.error("Ma'lumotlar yuklanmadi");
        }
      } catch (error) {
        console.error("Ma'lumotlarni olishda xatolik:", error);
      }
    },
    toggleTabs(tab) {
      this.openTab = tab;
      let period;
      switch (tab) {
        case 1:
          period = "daily";
          break;
        case 2:
          period = "weekly";
          break;
        case 3:
          period = "monthly";
          break;
        case 4:
          period = "yearly";
          break;
        default:
          period = "daily";
      }
      this.fetchChartData(period);
    },
    getCurrentDate() {
      const date = new Date();
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0'); // 0-based month, so add 1
      const day = String(date.getDate()).padStart(2, '0');
      this.currentDate = `${year}-${month}-${day}`; // YYYY-MM-DD format
    }
  },
  mounted() {
    this.getCurrentDate();
  },
  async created() {
    this.fetchChartData("daily");
  },
};
</script>

<style>
.chartt {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
