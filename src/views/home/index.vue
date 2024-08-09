<template>
  <div class="home">
    <v-container>
      <v-row>
        <v-col sm="12" xs="12" md="6">
          <v-text-field v-model="searchQuery" label="Search" />
        </v-col>
        <v-spacer></v-spacer>
        <v-col sm="12" xs="12" md="6" class="text-right">
          <v-btn color="primary" :prepend-icon="sortOrder == 'asc' ? 'mdi-sort-ascending' : 'mdi-sort-descending'" @click="toggleSortOrder">Sort By Price</v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-row>
            <v-col v-for="product in filteredProducts" :key="product.id" xs="12" md="4">
              <v-card
                class="mx-auto"
                max-width="400"
              >
                <!-- :src="product.product_image_url" -->
                <v-img
                  class="align-end text-white"
                  height="200"
                  :src="product.product_image_url"
                  cover
                >
                  <div class="overlay">
                    <v-card-title class="text-left">{{ product.name }}</v-card-title>
                  </div>
                  <!-- <v-card-title class="text-left">{{product.name}}</v-card-title> -->
                </v-img>

                <v-card-subtitle class="pt-4 text-left">
                  <span class="font-weight-medium">Price: ${{ product.price }}</span>
                </v-card-subtitle>

                <v-card-text class="text-left">
                  <div>{{ product.description }}</div>

                </v-card-text>

                <v-card-actions>
                  <v-btn color="primary" text="Add to cart" @click="addToCart(product)"></v-btn>

                  <v-btn color="orange" text="Details" @click="viewDetails(product)"></v-btn>
                </v-card-actions>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script lang="ts">
import webService from "./../../webservice";
import { defineComponent, ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'HomePage',
  setup() {
    const router = useRouter();
    const searchQuery = ref('');
    const sortOrder = ref('asc');
    const cart = ref([]);

    const products = ref([
      {
        category_id: 1,
        description: '',
        id: 2,
        name: 'chair1',
        price: 100.0,
        product_image_url: 'https://cdn.vuetifyjs.com/images/cards/house.jpg',
        stock: 22,
      },
      {
        category_id: 1,
        description: '',
        id: 3,
        name: 'chair2',
        price: 100.0,
        product_image_url: 'https://cdn.vuetifyjs.com/images/cards/house.jpg',
        stock: 19,
      },
      {
        category_id: 1,
        description: '',
        id: 4,
        name: 'chair3',
        price: 100.0,
        product_image_url: 'https://cdn.vuetifyjs.com/images/cards/house.jpg',
        stock: 50,
      },
      {
        category_id: 1,
        description: '',
        id: 5,
        name: 'chair4',
        price: 1000.0,
        product_image_url: 'https://cdn.vuetifyjs.com/images/cards/house.jpg',
        stock: 14,
      },
      {
        category_id: 1,
        description: 'Product Description',
        id: 6,
        name: 'Product Name',
        price: 20.0,
        product_image_url: 'https://cdn.vuetifyjs.com/images/cards/house.jpg',
        stock: 100,
      },
    ]);

    const filteredProducts = computed(() =>
      products.value.filter((x) =>
        x.name.toLowerCase().includes(searchQuery.value.toLowerCase())
      ).sort((a, b) => {
          if (sortOrder.value === 'asc') {
            return a.price - b.price;
          } else {
            return b.price - a.price;
          }
        })
    );

    const addToCart = (product) => {
      const productInCart = cart.value.find((item) => item.id === product.id);
      if (productInCart) {
        productInCart.quantity += 1;
      } else {
        cart.value.push({ ...product, quantity: 1 });
      }

      saveCart();
    };

    const saveCart = () => {
      localStorage.setItem('cart', JSON.stringify(cart.value));
    };

    const loadCart = () => {
      const savedCart = localStorage.getItem('cart');
      if (savedCart) {
        cart.value = JSON.parse(savedCart);
      }
    };

    const getProducts = () => {
      webService.get('/products').then((response)=>{
        products.value = response.data;
      });
    };

    const viewDetails = (product) => {
      router.push(`/details/${product.id}`);
    };

    const toggleSortOrder = () => {
      sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc';
    };

    onMounted(() => {
      loadCart();
      getProducts();
    });

    return {
      toggleSortOrder,
      sortOrder,
      searchQuery,
      products,
      filteredProducts,
      addToCart,
      viewDetails,
    };
  },
});
</script>
<style scoped>
.overlay {
  background: rgba(0, 0, 0, 0.5); /* semi-transparent black background */
  padding: 8px;
}
.text-white {
  color: white !important;
}
</style>