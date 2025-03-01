<template>      
    <v-card class="bg-primary elevation-8">
      <v-card-title>Upload</v-card-title>
      <v-card-text>
        <p>
          Upload a video or an audio file about something you want to study:
        </p>
      </v-card-text>
      <v-container fluid class="d-flex flex-column mt-n5">
        <v-file-input v-model="file" label="File input" variant="outlined" :multiple="false"></v-file-input>
        <v-btn color="secondary" @click="transcribe()">Upload</v-btn>
      </v-container>
    </v-card>
</template>

<script setup lang="ts">
// @ts-nocheck
import * as fs from "fs"
import { ref } from 'vue'


const file = ref < File > ();




</script>