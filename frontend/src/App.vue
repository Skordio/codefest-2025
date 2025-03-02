<template>
  <v-app>
    <v-layout>
      <v-app-bar class="bg-surface" dark>
        <v-container fluid class="d-flex justify-center ga-2">
          <v-icon class="pt-1 mt-1">mdi-lock</v-icon>
          <h2>{{ title }}</h2>
        </v-container>
      </v-app-bar>

      <v-main class="bg-background">
        <v-card color="background" :class="vCardClass">
          <template #image>
            <v-img alt="turtle" class="bg-background h-100" :src="`/images/${imgForBp}`" cover />
          </template>
          <v-row class="d-flex" :class="vRowClass">
            <v-col lg="6" md="4" cols="2"/>
            <v-col lg="4" md="6" cols="8">
              <file-upload />
            </v-col>
            <v-col lg="2" md="2" cols="2"/>
          </v-row>
        </v-card>
      </v-main>
    </v-layout>
  </v-app>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue';
import { getImgSrc } from './utils';
import { RouterLink, RouterView } from 'vue-router'
import fileUpload from './components/fileUpload.vue';
import { useDisplay } from 'vuetify';
import { onMounted } from "vue";

const title = ref("Lock In SG")

let audio: HTMLAudioElement | null = null;  // Explicitly typing the audio variable
const song = "/mii.mp3";  // Your audio file

const playAudio = () => {
  if (!audio) {
    audio = new Audio(song);
    audio.loop = false;
    audio.play().catch((error) => console.error("Error playing audio:", error));
  }
};

onMounted(() => {
  // Force playback after user interaction
  document.addEventListener("click", playAudio, { once: true });
});

const { mdAndUp } = useDisplay();

const imgForBp = computed(() => {
  if (mdAndUp.value) {
    return 'turtle_desktop.png';
  } else {
    return 'turtle_mobile.png';
  }
})

const vCardClass = computed(() => {
  if (mdAndUp.value) {
    return 'd-flex justify-center align-center h-100 w-100';
  } else {
    return 'd-flex flex-column justify-center h-100 w-100';
  }
})

const vRowClass = computed(() => {
  if (!mdAndUp.value) {
    return 'mt-15';
  } else {
    return '';
  }
})

</script>

<style>
html, body {
  overscroll-behavior: none;
}
</style>
