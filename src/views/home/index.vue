<template>
  <div class="home">
    <v-container>
      <v-row>
        <v-col cols="6" xs="12" md="6">
          <v-text-field v-model="searchQuery" label="Search" />
        </v-col>
        <v-spacer></v-spacer>
        <v-col cols="4" xs="12" md="4" class="text-right">
          <v-btn @click="toggleSortOrder" color="primary" :prepend-icon="sortOrder == 'asc' ? 'mdi-sort-ascending' : 'mdi-sort-descending'">Sort By Price</v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-row>
            <v-col v-for="product in filteredProducts" :key="product.id" xs="12" md="4">
              <v-card>
                <!-- <v-img :src="product.product_image_url" class="white--text align-end" height="300px" cover> -->
                <v-img :src="product.product_image_url" class="w-100" height="200px" cover=""></v-img>
                <v-card-title>{{ product.name }}</v-card-title>
                <v-card-subtitle>${{ product.price }}</v-card-subtitle>
                <v-card-actions class="w-100">
                  <v-btn depressed small color="primary" @click="addToCart(product)">Add to cart</v-btn>
                  <v-spacer></v-spacer>
                  <v-btn depressed small color="primary" @click="viewDetails(product)">View details</v-btn>
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
