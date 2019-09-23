<template>
    <v-container fluid>
        <register-user></register-user>
    </v-container>
</template>

<script>
    import RegisterUser from "./RegisterUser";
    export default {
        name: "Landing",
        components: {RegisterUser},
    }
</script>

<style scoped>

</style>