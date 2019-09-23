<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span class="group">
        <v-icon class="mb-1">
          mdi-rabbit
        </v-icon>
          </span>
        Rabbit
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-content>
      <landing></landing>
    </v-content>
  </v-app>
</template>

<script>

import Landing from "./components/Landing";
export default {
  name: 'App',
  components: {
    Landing
  },
  data: () => ({
    //
  }),
};
</script>
