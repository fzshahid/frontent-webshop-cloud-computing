<template>
  <div class="home">
    <v-container>
    <v-row>
      <v-col
        v-for="card in cards"
        :key="card.id"
        cols="12"
        sm="6"
        md="4"
        lg="3"
      >
        <v-card>
          <v-img
            :src="card.src"
            height="200px"
          ></v-img>
          <v-card-title>{{ card.title }}</v-card-title>
          <v-card-subtitle>{{ card.subtitle }}</v-card-subtitle>
          <v-card-text>
            {{ card.description }}
          </v-card-text>
          <v-card-actions>
            <v-btn>Learn More</v-btn>
          </v-card-actions>
        </v-card>
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
      cards: [
      { id: 1,subtitle: 'qwe', description: 'qwe', title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12, url: 'https://www.yahoo.com' },
      { id: 2,subtitle: 'qwe', description: 'qwe', title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6, url: 'https://www.google.com' },
      { id: 3,subtitle: 'qwe', description: 'qwe', title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 6, url: 'https://www.iwebarea.com' },
      { id: 4,subtitle: 'qwe', description: 'qwe', title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 6, url: 'https://www.goechkey.com' },     
      { id: 5,subtitle: 'qwe', description: 'qwe', title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 6, url: 'https://www.otg.com' }
    ]
    };
  },
  mounted() {
    this.getProducts();
  },
  methods: {
    getProducts() {
      // webService.get('http://54.158.39.27/products').then((response)=>{
      webService.get('http://ec2-16-171-199-141.eu-north-1.compute.amazonaws.com/api/products').then((response)=>{
        this.cards = response.data;
      });
    }
  }
})
</script>
