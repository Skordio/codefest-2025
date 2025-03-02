<template>      
    <v-card class="bg-primary elevation-8">
      <v-card-title>Upload</v-card-title>
      <v-card-text>
        <p>
          Upload an audio file containing something you want to study:
        </p>
      </v-card-text>
      <v-container fluid class="d-flex flex-column mt-n5">
        <v-file-input v-model="file" label="File input" variant="outlined" :multiple="false"></v-file-input>
        <div class="d-flex">
          <v-checkbox v-model="studyGuide" label="Study Guide"></v-checkbox>
          <v-checkbox v-model="quiz" label="Quiz"></v-checkbox>
          <v-checkbox v-model="flashcards" label="Flashcards"></v-checkbox>
        </div>
        <v-btn color="secondary" @click="transcribe()">Upload</v-btn>

        <v-progress-circular v-if="loading" indeterminate class="mx-auto mt-5"/>
      </v-container>
    </v-card>
</template>

<script setup lang="ts">
// @ts-nocheck
import * as fs from "fs"
import { ref } from 'vue'
import api from '@/api'

const loading = ref(false);
const file = ref<File>();
const errorMessage = ref('');

const studyGuide = ref(true);
const quiz = ref(false);
const flashcards = ref(false);

const studyMaterialsBlob = ref(null);

const transcribe = async () => {
  console.log(file.value);
  const formData = new FormData();
  formData.append('file', new Blob([file.value], { type: file.value.type }), file.value.name);

  loading.value = true;

  try {
    const response = await api.post(`/create?study_guide=${studyGuide.value}&quiz=${quiz.value}&flash_cards=${flashcards.value}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      responseType: 'blob'
    });

    // Create a Blob from the response data
    const studyMaterialsBlob = new Blob([response.data], { type: 'application/zip' });

    // Generate a URL and trigger the download
    const url = window.URL.createObjectURL(studyMaterialsBlob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'study_materials.zip';
    document.body.appendChild(a);  // Append to body for Firefox support
    a.click();
    document.body.removeChild(a);  // Remove after clicking
    window.URL.revokeObjectURL(url);

  } catch (error) {
    console.error(error);
    errorMessage.value = error.message;
  } finally {
    loading.value = false;
  }

}


</script>