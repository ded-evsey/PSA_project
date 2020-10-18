<template>
  <div class="hello">
    <button v-on:click="test_get">Fetch info from our backend</button>
    <br />
    <input v-model="user_name" placeholder="user_name" />
    <br />
    <button v-on:click="test_post">Send your name to backend</button>
    <div>{{backend_response}}</div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "test",
  data() {
    return {
      user_name: "",
      backend_response: ""
    };
  },
  props: {
    msg: String
  },
  mounted() {},
  methods: {
    test_get: function() {
      var baseURI = "/api/test_get";
      var vm = this;
      axios
        .get(baseURI)
        .then(response => {
          console.log(response);
          vm.backend_response = response.data.message;
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    test_post: function() {
      var baseURI = "/api/test_post";
      var vm = this;
      axios
        .post(baseURI, {
          user_name: vm.user_name
        })
        .then(response => {
          console.log(response.data);
          vm.backend_response = response.data;
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>
