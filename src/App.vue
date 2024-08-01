<template>
<!-- <v-toolbar :elevation="8" title="Application"></v-toolbar> -->
<v-toolbar id="nav" small color="indigo" dark>
    <v-toolbar-side-icon></v-toolbar-side-icon>
    <v-toolbar-title>Web Shop</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn icon>
      <v-icon>search</v-icon>
    </v-btn>
    <router-link to="/">Cart</router-link> |
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </v-toolbar>
  <router-view />
</template>

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
