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
                      <v-img :src="item.image" height="100px" cover></v-img>
                    </v-col>
                    <v-col cols="8">
                      <v-card-title class="text-left">{{ item.name }}</v-card-title>
                      <v-card-subtitle class="text-left font-weight-bold"
                        >${{ item.price.toFixed(2) }}</v-card-subtitle
                      >
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

          <v-divider></v-divider>

          <!-- Address and Email Fields -->
          <v-text-field
            v-model="address"
            label="Shipping Address"
            placeholder="Enter your address"
            required
            outlined
            class="mt-4"
          ></v-text-field>

          <v-text-field
            v-model="email"
            label="Email Address"
            placeholder="Enter your email"
            required
            outlined
            type="email"
            class="mb-4"
          ></v-text-field>

          <!-- Payment Methods -->
          <v-radio-group v-model="selectedPaymentMethod" row>
            <v-radio label="Credit Card" value="credit-card"></v-radio>
            <v-radio label="PayPal" value="paypal"></v-radio>
            <v-radio label="Bank Transfer" value="bank-transfer"></v-radio>
          </v-radio-group>

          <v-card-actions>
            <v-btn
              :loading="loading"
              class="text-none mb-4"
              size="x-large"
              variant="flat"
              block
              color="primary"
              :disabled="!cart.length || !address || !email || !selectedPaymentMethod || loading"
              prepend-icon="mdi-credit-card-outline"
              @click="checkout"
            >
              Checkout
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import router from '@/router'
import webService from '@/webservice'
import { defineComponent, ref, computed } from 'vue'

export default defineComponent({
  name: 'CartDetails',
  setup() {
    const loading = ref(false)
    const cart = ref([])
    const address = ref('')
    const email = ref('')
    const selectedPaymentMethod = ref('credit-card')

    const loadCart = () => {
      const savedCart = localStorage.getItem('cart')
      if (savedCart) {
        cart.value = JSON.parse(savedCart)
      }
    }

    const saveCart = () => {
      localStorage.setItem('cart', JSON.stringify(cart.value))
    }

    const incrementQuantity = (item) => {
      const cartItem = cart.value.find((i) => i.id === item.id)
      if (cartItem) {
        cartItem.quantity += 1
        saveCart()
      }
    }

    const decrementQuantity = (item) => {
      const cartItem = cart.value.find((i) => i.id === item.id)
      if (cartItem && cartItem.quantity > 1) {
        cartItem.quantity -= 1
        saveCart()
      } else {
        removeItem(item)
      }
    }

    const removeItem = (item) => {
      cart.value = cart.value.filter((i) => i.id !== item.id)
      saveCart()
    }

    const totalPrice = computed(() =>
      cart.value.reduce((total, item) => total + item.price * item.quantity, 0)
    )

    const checkout = () => {
      loading.value = true
      if (!address.value || !email.value || !selectedPaymentMethod.value) {
        alert('Please fill in all the fields and select a payment method.')
        return
      }
      // alert('Proceeding to checkout with the selected payment method');
      const orderData = {
        email: email.value,
        address: address.value,
        items: cart.value.map((item) => ({
          product_id: item.id,
          quantity: item.quantity,
        })),
      }
      console.log(orderData)
      webService
        .post('/orders', orderData)
        .then((response) => {
          const order = response.data.order
          router.push({
            path: '/order-success',
            query: {
              orderId: order.id,
              email: order.email,
              totalPrice: order.amount,
            },
          })
          alert(response.data.message)
          loading.value = false
        })
        .catch((error) => {
          alert('There was an issue with placing your order.')
          console.error(error)
          loading.value = false
          // router.push({
          //   path: '/order-success',
          //   query: {
          //     orderId: 1,
          //     email: '1@1.xom',
          //     totalPrice: 300,
          //   },
          // })
        })
    }

    loadCart()

    return {
      cart,
      totalPrice,
      address,
      email,
      selectedPaymentMethod,
      incrementQuantity,
      decrementQuantity,
      removeItem,
      checkout,
      loading,
    }
  },
})
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
