import { defineStore } from 'pinia';
import axiosInstance from '../axios';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    accessToken: null,
    refreshToken: null,
    loginError: null
  }),
  actions: {
    async login(username, password) {
      try {
        const response = await axiosInstance.post('/auth/login/', {
          username,
          password,
        });
        if (response.status === 200) {
            console.log(response.data);
          this.accessToken = response.data.access;
          this.refreshToken = response.data.refresh;
          this.user = response.data.user;
          axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${this.accessToken}`;
          localStorage.setItem('accessToken', this.accessToken);
          localStorage.setItem('refreshToken', this.refreshToken);
          localStorage.setItem('user', JSON.stringify(this.user));
          this.loginError = null; // Clear any previous login error
          return true; // Return true for successful login
        } else {
          this.loginError = 'Login error';
          return false;
        }
      } catch (error) {
        this.loginError = error.response ? error.response.data.detail : 'Login error';
        console.error('Login error:', error);
        return false; // Return false for failed login
      }
    },
    async register(first_name, last_name, username, password) {
      try {
        const response = await axiosInstance.post('/auth/register/', {
          first_name,
          last_name,
          username,
          password,
        });
        if (response.status === 200) {
          this.accessToken = response.data.accessToken;
          this.refreshToken = response.data.refreshToken;
          this.user = response.data.user;
          axios.defaults.headers.common['Authorization'] = `Bearer ${this.accessToken}`;
          localStorage.setItem('accessToken', this.accessToken);
          localStorage.setItem('refreshToken', this.refreshToken);
          localStorage.setItem('user', JSON.stringify(this.user));
          this.loginError = null; 
        } else {
          console.error('Register error:', response);
        }
      } catch (error) {
        console.error('Register error:', error);
      }
    },
    async refreshToken() {
      try {
        const response = await axiosInstance.post('/refresh-token', {
          refreshToken: this.refreshToken,
        });
        this.accessToken = response.data.accessToken;
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.accessToken}`;
        localStorage.setItem('accessToken', this.accessToken);
      } catch (error) {
        console.error('Refresh token error:', error);
        this.logout();
      }
    },
    logout() {
      this.user = null;
      this.accessToken = null;
      this.refreshToken = null;
      delete axios.defaults.headers.common['Authorization'];
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      localStorage.removeItem('user');
    },
    loadStoredTokens() {
      this.accessToken = localStorage.getItem('accessToken');
      this.refreshToken = localStorage.getItem('refreshToken');
      this.user = JSON.parse(localStorage.getItem('user'));
      if (this.accessToken) {
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.accessToken}`;
      }
    }
  },
});
