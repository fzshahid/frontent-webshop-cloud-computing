<template>
  <div class="home">
    <CartDetails msg="" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import CartDetails from './components/cartdetails.vue'

export default defineComponent({
  name: 'CartPage',
  components: { CartDetails },
})
</script>
