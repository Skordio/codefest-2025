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

        <v-card v-if="showTranscription">
          <v-skeleton-loader v-if="loading" type="text"  />
          <div v-else>
            {{ transcription }}
          </div>
        </v-card>
      </v-container>
    </v-card>
</template>

<script setup lang="ts">
// @ts-nocheck
import * as fs from "fs"
import { ref } from 'vue'
import api from '@/api'

const showTranscription = ref(false);
const transcription = ref('');
const loading = ref(false);
const file = ref<File>();

const transcribe = async () => {
  const formData = new FormData();
  formData.append('file', file.value);
  const response = await api.post('/transcribe', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  });
  console.log(response.data);
}

</script>