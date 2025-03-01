import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.min.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

// Vuetify
import 'vuetify/styles'
import colors from 'vuetify/util/colors'
import { aliases, mdi } from "vuetify/iconsets/mdi"
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// let colorChoices = {
//   primary: '#033F63', // #033F63
//   secondary: '#28666E', // #28666E
//   accent: '#FEDC97', // #FEDC97
//   surface: '#B5B682', // #B5B682
//   background: '#7C9885', // #7C9885
// }

// colorChoices = {
//   primary: '#a3b18a', // #a3b18a
//   secondary: '#588157', // #588157
//   accent: '#dad7cd', // #dad7cd
//   surface: '#3a5a40', // #3a5a40
//   background: '#344e41', // #344e41
// }

let colorChoices = {
  primary: '#457b9d', // #457b9d
  secondary: '#1d3557', // #1d3557
  accent: '#e63946', // #e63946
  surface: '#f1faee', // #f1faee
  background: '#a8dadc', // #a8dadc
}


const vuetify = createVuetify({
	icons: {
		defaultSet: "mdi",
		aliases,
		sets: {
			mdi,
		},
	},
  theme: {
    themes: {
      light: {
        dark: false,
        colors: {
          ...colorChoices,
          error: colors.red.accent1,
          info: colors.lightBlue.base,
          success: colors.green.base,
          warning: colors.amber.base,
        }
      },
    },
  },
  components,
  directives,
})

import App from './App.vue'
import router from './router'

const app = createApp(App).use(vuetify)

app.use(createPinia())
app.use(router)

app.mount('#app')
