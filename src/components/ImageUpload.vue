<template>
    <div class="flex justify-center">
      <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col">
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2">上传文件:</label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700" @change="onFileChange" type="file">
        </div>
  
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2">输入提示语:</label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700" type="text" v-model="promptText">
        </div>
  
        <div class="flex items-center justify-between">
          <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" @click="uploadImage">提交</button>
        </div>
      </div>
    </div>
  </template>
  

  <script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedFile: null,
      base64img:"",
      promptText: ''
    }
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files || e.dataTransfer.files;
      if (!files.length)
        return;
      this.createImage(files[0]);
    },
    createImage(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.selectedFile = e.target.result;
        this.base64img = this.selectedFile.split(",")[1]; 
      };
      reader.readAsDataURL(file);
    },
    async postData() {
      try {
        const response = await axios.post('http://localhost:6006/transform_image', {
          // Request body data
          // Add any necessary data or parameters for the POST request
          image_base64:this.base64img,
          prompt:this.promptText
        });
        
        console.log(response.data);
        // Handle the response from the backend
        this.$emit('uploadSuccess', response.data["images"][0]);
      } catch (error) {
        console.error(error); // Handle any error that occurs during the request
      }
    },
    uploadImage() {
      console.log(this.selectedFile);
      // Here you can use the base64 string with your API request
      if(this.selectedFile) {
        console.log(this.selectedFile);
        // Here you can use the base64 string with your API request
      } else {
        alert("请选择文件");
      }
      if(!this.promptText){
        alert("请输入提示语")
      }
      this.postData()
      this.$toast.open({
        message: '图片生成中，请稍等，大约需要1分钟',
        type: 'success',
        position: 'top-right',
        duration: 5000
      });
    },
  }
}
</script>