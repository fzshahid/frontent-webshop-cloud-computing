// import { createApp } from 'vue'
// import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'

// createApp(App).use(router).use(createPinia()).mount('#app')
import '@mdi/font/css/materialdesignicons.css'


import { createApp } from 'vue'
// import SvgIcon from '@jamescoyle/vue-icon'
// import { mdi } from '@mdi/js';

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// Components
import App from './App.vue'

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: "mdi",
  },
})

createApp(App).use(router).use(createPinia()).use(vuetify).mount('#app')