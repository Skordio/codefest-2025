<template>
  <v-app>
    <v-layout>
      <v-app-bar class="bg-surface" dark>
        <v-container fluid class="d-flex justify-center ga-2">
          <v-icon class="pt-1 mt-1">mdi-lock</v-icon>
          <h2>{{ title }}</h2>
        </v-container>
      </v-app-bar>
      <!-- <v-navigation-drawer expand-on-hover rail>
        <v-list>
          <v-list-item title="Home"></v-list-item>
          <v-list-item title="About"></v-list-item>
        </v-list>
      </v-navigation-drawer> -->

      <v-main class="bg-background">
        <v-container fluid class="d-flex align-center h-100">
          <v-row class="d-flex" justify="center">
            <v-col lg="4" md="6" sm="8" cols="8">
              <file-upload />
            </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-layout>
  </v-app>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import fileUpload from './components/fileUpload.vue';

const title = ref("Lock In SG")

import { onMounted } from "vue";

onMounted(() => {
  const audio = new Audio("/src/frutiger.mp3");
  audio.loop = true;
  audio.volume = 0.5;
  audio.play().catch(() => console.log("Autoplay blocked"));
});

</script>
