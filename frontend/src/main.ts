import 'vite/modulepreload-polyfill'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import Toast, {
    type PluginOptions,
    POSITION,
} from 'vue-toastification'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { awesomeIcons } from './icons'

import App from './App.vue'
import router from './router'

import './assets/main.css'
import './index.css'
import 'vue-toastification/dist/index.css'

const app = createApp(App)

const defToastOptions: PluginOptions = {
    position: POSITION.TOP_RIGHT,
    closeOnClick: true,
    pauseOnHover: true,
    maxToasts: 5,
}
awesomeIcons.forEach(icon => library.add(icon))

app.use(createPinia())
app.use(router)
app.use(Toast, defToastOptions)
app.component('FontAwesomeIcon', FontAwesomeIcon)

app.mount('#app')
