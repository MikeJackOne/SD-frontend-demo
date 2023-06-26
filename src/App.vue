<template>
  <div class="flex h-screen bg-gray-200">

    <!-- Sidebar -->
    <div class="p-4 space-y-4 overflow-auto w-60 bg-blue-500 text-white">
      <h2 class="text-2xl font-semibold">自动室内设计</h2>
      <p>轻松将您的房间转变成精美的设计空间！</p>
      <nav>
        <h2 class="text-lg font-semibold">使用说明</h2>
        <ul class="space-y-2 text-sm">
          <!-- List your instructions here -->
          <li>1. 准备您想重新设计的房间的清晰照片。</li>
          <li>2. 点击'上传图片'按钮，并从您的设备中选择照片。</li>
          <li>3. 在提供的文本框中输入描述，说明您希望如何设计您的房间。</li>
          <li>4. 点击“提交”按钮提交您的图像和提示。</li>
          <li>5. 请稍等片刻（大约一分钟，我们的AI将根据您的提示创建一个漂亮的室内设计。</li>
          <li>6. 结果将在上方显示。您可以保存图像或重新开始新的设计。</li>
        </ul>
      </nav>
    </div>

    <!-- Main Content and Result -->
    <div class="flex-1 flex flex-col p-10 overflow-auto">
      
      <!-- Main Content -->
      <main class="mb-10 flex-grow">
        <header>
          <h1 class="text-5xl font-bold text-center mb-4">欢迎来到我们的自动室内设计网站</h1>
          <p class="text-center text-lg text-gray-700 mb-4 bg-blue-100 p-4 rounded shadow">上传您的图片并输入提示开始设计！</p>
        </header>

        <!-- Result Image -->
        <div v-if="notifyMessage" class="p-3 rounded-md shadow-lg bg-white mb-4 mx-auto" style="max-width: 400px;">
          <h2 class="text-xl font-semibold mb-3">结果:</h2>
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
