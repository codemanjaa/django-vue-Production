<script>

  import {Bar, mixins} from "vue-chartjs";
  import {mapState} from "vuex"

  export default {
    name: "ReactiveBar",
    extends: Bar,
    mixins: [mixins.reactiveProp],
    props: ["options"],

    mounted() {
      // this.chartData is created in the mixin.
      // If you want to pass options please create a local options object
      this.renderChart(this.chartData, this.options);
    },
    computed: mapState(["usermoodcontainer"])
  };

</script>

<style scoped>

</style>
