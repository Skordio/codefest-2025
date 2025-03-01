<template>
  <v-app>
    <v-layout>
      <v-app-bar class="bg-surface" dark>
        <v-container fluid class="d-flex justify-center">
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
            <v-col cols="4">
              <v-card class="bg-secondary elevation-8">
                <v-card-title>Upload</v-card-title>
                <v-card-text>
                  <p>
                    Upload a video or an audio file about something you want to study:
                  </p>
                </v-card-text>
                <v-container fluid class="d-flex">
                  <v-file-input label="File input" variant="outlined"></v-file-input>
                </v-container>
              </v-card>
            </v-col>
          </v-row>
          <!-- <v-row class="d-flex" justify="center">
            <v-col cols="4">
              <v-file-input label="File input" variant="solo-filled"></v-file-input>
            </v-col>
          </v-row> -->
        </v-container>
      </v-main>
    </v-layout>
  </v-app>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router'

const title = ref("Lock In SG")


</script>
