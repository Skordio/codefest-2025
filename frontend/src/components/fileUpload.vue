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
        <div class="d-flex">
          <v-checkbox v-model="studyGuide" label="Study Guide"></v-checkbox>
          <v-checkbox v-model="quiz" label="Quiz"></v-checkbox>
          <v-checkbox v-model="flashcards" label="Flashcards"></v-checkbox>
        </div>
        <v-btn color="secondary" @click="transcribe()">Upload</v-btn>

        <v-card v-if="showTranscription" class="mt-5 pa-3">
          <v-progress-circular v-if="loading" indeterminate class="mx-auto"></v-progress-circular>
          <div class="d-flex ga-2 justify-center" v-else>
            <v-btn v-if="studyGuideBlob" color="primary" @click="download(studyGuideBlob, 'study_guide')">Download Study Guide</v-btn>
            <v-btn v-if="quizBlob" color="primary" @click="download(quizBlob, 'quiz')">Download Quiz</v-btn>
            <v-btn v-if="flashcardsBlob" color="primary" @click="download(flashcardsBlob, 'flashcards')">Download Flashcards</v-btn>
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
import { createStudyGuidePDF, createFlashCardPDF, createQuizPDF } from '@/utils/pdfCreate'

const showTranscription = ref(false);
const transcription = ref('');
const loading = ref(false);
const file = ref<File>();
const errorMessage = ref('');

const studyGuide = ref(true);
const quiz = ref(false);
const flashcards = ref(false);

const studyGuideBlob = ref<Blob>();
const quizBlob = ref<Blob>();
const flashcardsBlob = ref<Blob>();

const transcribe = async () => {
  console.log(file.value);
  const formData = new FormData();
  formData.append('file', new Blob([file.value], { type: file.value.type }), file.value.name);

  showTranscription.value = true;
  loading.value = true;

  try {
    const response = await api.post(`/create?study_guide=${studyGuide.value}&quiz=${quiz.value}&flash_cards=${flashcards.value}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });

    console.log(response.data)


    if (studyGuide.value) {
      studyGuideBlob.value = createStudyGuidePDF(response.data.studyGuide);
    }
    if (quiz.value) {
      quizBlob.value = createQuizPDF(response.data.quiz);
    }
    if (flashcards.value) {
      flashcardsBlob.value = createFlashCardPDF(response.data.flashcards);
    }

    // transcription.value = response.data.transcript;
  } catch (error) {
    console.error(error);
    errorMessage.value = error.message;
    showTranscription.value = false;
  } finally {
    loading.value = false;
  }

}

</script>