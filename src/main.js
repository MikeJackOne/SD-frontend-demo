import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import Toast from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';

createApp(App).use(Toast).mount('#app')
