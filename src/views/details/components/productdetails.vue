<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="6">
        <v-img :src="product.product_image_url" height="400px"></v-img>
      </v-col>
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title class="text-left">{{ product.name }}</v-card-title>
          <v-card-subtitle class="text-left">Price: €{{ product.price }}</v-card-subtitle>
          <v-card-text class="text-left">
            <p>{{ product.description }}</p>
            <p>Stock: {{ product.stock }}</p>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click="addToCart(product)">Add to Cart</v-btn>
            <v-btn text @click="goBack">Go Back</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import webService from "./../../../webservice";

export default defineComponent({
  name: 'ProductDetails',
  setup() {
    const route = useRoute()
    const router = useRouter()
    const product = ref({
      category_id: 1,
      description: '',
      id: 0,
      name: '',
      price: 0.0,
      product_image_url: '',
      stock: 0,
    })

    const getProductDetails = () => {
      const productId = parseInt(route.params.id, 10)
      webService.get(`/products/${productId}`).then((response) => {
      // webService.get(`/products/2`).then((response) => {
        // products.value = response.data
        // if (foundProduct) {
          product.value = response.data;
        // } else {
        // }
      }).catch((error) => {
        console.error(error)
        router.push('/');
      });
    }
    const fetchProduct = () => {
      // Dummy data to simulate fetching product details
      // const products = [
      //   {
      //     category_id: 1,
      //     description: 'Comfortable and stylish chair.',
      //     id: 2,
      //     name: 'chair1',
      //     price: 100.0,
      //     product_image_url: 'https://cdn.vuetifyjs.com/images/cards/house.jpg',
      //     stock: 22,
      //   },
        // Add other products here
      // ]

      // const productId = parseInt(route.params.id, 10);
      // const foundProduct = products.find((p) => p.id === productId);
      // if (foundProduct) {
      //   product.value = foundProduct;
      // } else {
      //   router.push('/'); // Redirect to home if product not found
      // }

      getProductDetails();
    }

    const addToCart = (product) => {
      const cart = JSON.parse(localStorage.getItem('cart')) || []
      const productInCart = cart.find((item) => item.id === product.id)
      if (productInCart) {
        productInCart.quantity += 1
      } else {
        cart.push({ ...product, quantity: 1 })
      }
      localStorage.setItem('cart', JSON.stringify(cart))
    }

    const goBack = () => {
      router.push('/')
    }

    onMounted(() => {
      fetchProduct()
    })

    return {
      product,
      addToCart,
      goBack,
    }
  },
})
</script>

<style scoped>
.v-card-title {
  font-size: 1.5rem;
}
.v-card-subtitle {
  font-size: 1.2rem;
  margin-bottom: 1rem;
}
</style>
