<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="8" class="mx-auto">
        <v-card class="pa-4">
          <v-card-title>Your Cart</v-card-title>
          <v-divider></v-divider>

          <div v-if="cart.length">
            <v-row v-for="item in cart" :key="item.id" class="mb-4">
              <v-col cols="12">
                <v-card outlined>
                  <v-row no-gutters>
                    <v-col cols="4">
                      <v-img
                        :src="item.image"
                        height="100px"
                        cover
                      ></v-img>
                    </v-col>
                    <v-col cols="8">
                      <v-card-title class="text-left">{{ item.name }}</v-card-title>
                      <v-card-subtitle class="text-left font-weight-bold">${{ item.price.toFixed(2) }}</v-card-subtitle>
                      <v-card-text class="d-flex align-center">
                        <v-btn density="compact" icon @click="decrementQuantity(item)">
                          <v-icon>mdi-minus</v-icon>
                        </v-btn>
                        <span class="mx-4 font-weight-medium">{{ item.quantity }}</span>
                        <v-btn density="compact" icon @click="incrementQuantity(item)">
                          <v-icon>mdi-plus</v-icon>
                        </v-btn>
                        <v-btn density="compact" icon class="ml-auto" @click="removeItem(item)">
                          <v-icon color="red">mdi-delete</v-icon>
                        </v-btn>
                      </v-card-text>
                    </v-col>
                  </v-row>
                </v-card>
              </v-col>
            </v-row>
  
            <v-divider></v-divider>
  
            <v-card-text v-if="cart.length" class="d-flex justify-space-between text-h6">
              <span>Total:</span>
              <span>${{ totalPrice.toFixed(2) }}</span>
            </v-card-text>
            <v-card-text v-else class="text-center">Your cart is empty.</v-card-text>
          </div>

          <v-card-actions>
            <v-btn
              class="text-none mb-4"
              size="x-large"
              variant="flat"
              block
              color="primary"
              :disabled="!cart.length"
              prepend-icon="mdi-credit-card-outline"
              @click="checkout"
            >
              Checkout Using Credit Card
            </v-btn>
            <v-btn block color="primary" :disabled="!cart.length" @click="checkout">Block Button</v-btn>
            <!-- <v-btn color="primary" :disabled="!cart.length" @click="checkout">Checkout</v-btn> -->
          </v-card-actions>
          
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';

export default defineComponent({
  name: 'CartDetails',
  setup() {
    const cart = ref([]);

    const loadCart = () => {
      const savedCart = localStorage.getItem('cart');
      if (savedCart) {
        cart.value = JSON.parse(savedCart);
      }
    };

    const saveCart = () => {
      localStorage.setItem('cart', JSON.stringify(cart.value));
    };

    const incrementQuantity = (item) => {
      const cartItem = cart.value.find((i) => i.id === item.id);
      if (cartItem) {
        cartItem.quantity += 1;
        saveCart();
      }
    };

    const decrementQuantity = (item) => {
      const cartItem = cart.value.find((i) => i.id === item.id);
      if (cartItem && cartItem.quantity > 1) {
        cartItem.quantity -= 1;
        saveCart();
      } else {
        removeItem(item);
      }
    };

    const removeItem = (item) => {
      cart.value = cart.value.filter((i) => i.id !== item.id);
      saveCart();
    };

    const totalPrice = computed(() =>
      cart.value.reduce((total, item) => total + item.price * item.quantity, 0)
    );

    const checkout = () => {
      alert('Proceeding to checkout');
      // Implement your checkout logic here
    };

    loadCart();

    return {
      cart,
      totalPrice,
      incrementQuantity,
      decrementQuantity,
      removeItem,
      checkout,
    };
  },
});
</script>

<style scoped>
.v-card-title,
.v-card-subtitle {
  margin-bottom: 0;
}

.v-card-text {
  padding-top: 8px;
}
</style>
