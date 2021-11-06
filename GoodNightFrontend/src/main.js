import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { VueClipboard } from '@soerenmartius/vue3-clipboard'

// createApp(App).mount('#app')
const app = createApp(App)
app.use(router)
app.use(VueClipboard)
app.mount('#app')
