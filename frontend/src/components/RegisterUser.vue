<template>
      <div id="registerUser">
        <v-form @submit="CreateUser">
          <v-card class="elevation-10 mx-auto mt-3 my-auto" max-width="500">
            <v-card-title>New User</v-card-title>
            <v-card-text>
            <v-text-field
                    v-model="username"
                    prepend-icon="mdi-account-circle"
                    label="Username"></v-text-field>
            <v-text-field
                    v-model="email"
                    prepend-icon="mdi-email"
                    label="Email"></v-text-field>
             <v-text-field
              v-model="password"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              prepend-icon="mdi-key"
              :rules="[rules.required, rules.min]"
              :type="show1 ? 'text' : 'password'"
              label="Password"
              hint="At least 8 characters"
              @click:append="show1 = !show1"
              ></v-text-field>
              </v-card-text>
            <v-card-actions class="text-right">
              <v-btn dark color="primary" type=submit @submit.prevent="CreateUser">Submit!</v-btn>
            </v-card-actions>
            </v-card>
        </v-form>
      </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "registerUser",
        data () {
            return {
                show1: false,
                rules: {
                  required: value => !!value || 'Required.',
                  min: v => v.length >= 8 || 'Min 8 characters',
                },
                username: "",
                password: "",
                email: "",
            }
        },
        methods: {
            CreateUser: function(e) {
              e.preventDefault();
              axios.post("http://127.0.0.1:8000/api/users/", {
                  username: this.username,
                  email: this.email,
                  password: this.password
              })
              .catch(e => {
                this.errors.push(e)
              })
          }
        }
    }
</script>

<style scoped>

</style>
