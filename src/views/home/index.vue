<template>
  <div class="home">
    <v-container>
    <v-row>
      <v-col cols="12" md="4">
        <v-text-field
          v-model="searchQuery"
          label="Search"
        />
      </v-col>

      <v-col cols="12" md="8">
        <v-row>
          <v-col
            v-for="product in filteredProducts"
            :key="product.id"
            cols="12"
            md="4"
          >
            <v-card>
              <v-img
                :src="product.src"
                height="200px"
              ></v-img>
              <v-card-title>{{ product.name }}</v-card-title>
              <v-card-subtitle>${{ product.price }}</v-card-subtitle>
              <v-card-actions>
                <v-btn @click="addToCart(product)">Add to Cart</v-btn>
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

import { defineComponent } from 'vue'
export default defineComponent({
  name: 'HomePage',
  components: { },
  data() {
    return {
      searchQuery: '',
      products: [
        { id: 1, price:10,  description: 'qwe', name: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12, url: 'https://www.yahoo.com' },
        { id: 2, price:10,  description: 'qwe', name: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6, url: 'https://www.google.com' },
        { id: 3, price:10,  description: 'qwe', name: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 6, url: 'https://www.iwebarea.com' },
        { id: 4, price:10,  description: 'qwe', name: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 6, url: 'https://www.goechkey.com' },     
        { id: 5, price:10,  description: 'qwe', name: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 6, url: 'https://www.otg.com' }
      ]
    };
  },
  computed: {
    filteredProducts() {
      return this.products.filter((x) =>  x.name.toLowerCase().indexOf(this.searchQuery.toLowerCase()) > -1 );
    }
  },
  mounted() {
    this.getProducts();
  },
  methods: {
    addToCart(product) {
      console.log(product);
    },
    getProducts() {
        webService.get('/products').then((response)=>{
          this.products = response.data;
        });
    }
  }
})
</script>
