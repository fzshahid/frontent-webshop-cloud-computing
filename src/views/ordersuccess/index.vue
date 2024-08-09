<template>
  <v-container>
    <v-row justify="center" class="my-12">
      <v-col cols="12" md="8">
        <v-card class="text-center pa-5">
          <v-icon color="green" size="64" class="mb-4">mdi-check-circle-outline</v-icon>
          <v-card-title class="headline mb-4">Order Successful!</v-card-title>
          <v-card-subtitle>Your order has been placed successfully. We have sent a confirmation email to {{ email }}.</v-card-subtitle>
          <v-divider class="my-4"></v-divider>
          
          <v-card-text>
            <p>Order ID: <strong>{{ orderId }}</strong></p>
            <p>Total Amount: <strong>€{{ totalPrice }}</strong></p>
          </v-card-text>

          <v-divider class="my-4"></v-divider>

          <v-btn color="primary" @click="goToHome">Go to Home</v-btn>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useRouter, useRoute } from 'vue-router';

export default defineComponent({
  name: 'OrderSuccess',
  setup() {
    const router = useRouter();
    const route = useRoute();

    const orderId = route.query.orderId;
    const email = route.query.email;
    const totalPrice = route.query.totalPrice;

    const goToHome = () => {
      router.push('/');
    };

    return {
      orderId,
      email,
      totalPrice,
      goToHome,
    };
  },
});
</script>

<style scoped>
.headline {
  font-size: 2rem;
  font-weight: bold;
}
</style>
