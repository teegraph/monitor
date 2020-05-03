<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        Монитор
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <DataGrid/>
    </v-content>
  </v-app>
</template>

<script>
import DataGrid from './components/DataGrid';

export default {
  name: 'App',

  components: {
    DataGrid,
  },

  data: () => ({
    //
  }),
};
</script>
