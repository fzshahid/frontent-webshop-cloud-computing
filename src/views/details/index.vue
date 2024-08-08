<template>
  <div class="home">
    <ProductDetails msg="" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import ProductDetails from './components/productdetails.vue'

export default defineComponent({
  name: 'DetailsPage',
  components: { ProductDetails },
})
</script>
