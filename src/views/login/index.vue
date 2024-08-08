<template>
    <div class="login">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" sm="8" md="4">
            <v-card>
              <v-card-title class="headline">Login</v-card-title>
              <v-card-text>
                <v-form ref="form">
                  <v-text-field
                    v-model="email"
                    label="Email"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="password"
                    label="Password"
                    type="password"
                    required
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-btn color="primary" @click="login">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import { useRouter } from 'vue-router';
  
  export default defineComponent({
    name: 'LoginPage',
    components: {},
    data() {
      return {
        email: '',
        password: '',
      };
    },
    methods: {
      login() {
        console.log('Email:', this.email);
        console.log('Password:', this.password);  
        useRouter().push('/');
      }
    }
  });
  </script>
  
  <style lang="scss">
  .login {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  </style>
  