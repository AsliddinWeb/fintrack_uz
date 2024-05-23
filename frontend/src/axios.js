import axios from 'axios';
import { useAuthStore } from './stores/auth';

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/v1',
});

axiosInstance.interceptors.request.use(
  (config) => {
    const authStore = useAuthStore();
    if (authStore.accessToken) {
      config.headers['Authorization'] = `Bearer ${authStore.accessToken}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default axiosInstance;
