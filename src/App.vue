<template>
<!-- <v-toolbar :elevation="8" title="Application"></v-toolbar> -->
<v-card class="mx-auto" color="grey-lighten-3">
    <v-layout>
      <v-app-bar
        scroll-behavior="elevate hide"
        color="teal-darken-4"
        image="https://picsum.photos/1920/1080?random"
      >
        <template #image>
          <v-img
            gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"
          ></v-img>
        </template>
        <v-app-bar-title class="text-left" @click="goToHome">
          <v-btn  @click="goToCart">
            Webshop App
          </v-btn>
          </v-app-bar-title>
        <v-spacer></v-spacer>
        <v-badge
          :content="cartItemCount"
          color="red"
          overlap
          offset-x="12"
          offset-y="12"
        >
          <v-btn icon @click="goToCart">
            <v-icon>mdi-cart</v-icon>
          </v-btn>
        </v-badge>
      </v-app-bar>
      <v-main>
        <router-view />
      </v-main>
    </v-layout>
  </v-card>

</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: 'NavBar',
  setup() {
    const cartItemCount = ref(0);
    const router = useRouter();

    const loadCart = () => {
      const cart = JSON.parse(localStorage.getItem('cart')) || [];
      cartItemCount.value = cart.reduce((total, item) => total + item.quantity, 0);
    };

    const goToCart = () => {
      router.push('/cart');
    };
    const goToHome = () => {
      router.push('/');
    };

    onMounted(() => {
      loadCart();
    });

    return {
      cartItemCount,
      goToCart,
      goToHome
    };
  },
};
</script>
  <style lang="scss">
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  
  #nav {
    padding: 30px;
  
    a {
      font-weight: bold;
      color: #2c3e50;
  
      &.router-link-exact-active {
        color: #42b983;
      }
    }
  }
  </style>
  