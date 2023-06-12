<template>
  <div class="flex h-screen bg-gray-200">

    <!-- Sidebar -->
    <div class="p-4 space-y-4 overflow-auto w-60 bg-blue-500 text-white">
      <h2 class="text-2xl font-semibold">Project Title</h2>
      <p>A brief description of your project...</p>
      <nav>
        <h2 class="text-lg font-semibold">Instructions</h2>
        <ul class="space-y-2 text-sm">
          <!-- List your instructions here -->
          <!-- ... -->
        </ul>
      </nav>
    </div>

    <!-- Main Content and Result -->
    <div class="flex-1 flex flex-col p-10 overflow-auto">
      
      <!-- Main Content -->
      <main class="mb-10 flex-grow">
        <header>
          <h1 class="text-5xl font-bold text-center mb-4">Welcome to our Image Processing Website</h1>
          <p class="text-center text-lg text-gray-700 mb-4 bg-blue-100 p-4 rounded shadow">Upload your image and enter a prompt to get started!</p>
        </header>

        <!-- Result Image -->
        <div v-if="notifyMessage" class="p-3 rounded-md shadow-lg bg-white mb-4 mx-auto" style="max-width: 400px;">
          <h2 class="text-xl font-semibold mb-3">Result:</h2>
          <div class="flex justify-center">
            <img :src="'data:image/png;base64,' + notifyMessage" alt="Result Image" class="rounded-lg shadow-md max-w-full h-auto" style="width: 300px; height: 300px;" />
          </div>
        </div>

        <image-upload @uploadSuccess="notifyMessage = $event"></image-upload>
      </main>

    </div>

  </div>
</template>



<script>
import ImageUpload from './components/ImageUpload.vue'

export default {
  components: {
    'image-upload': ImageUpload,
  },
  data() {
    return {
      notifyMessage: null,
    }
  }
}
</script>
