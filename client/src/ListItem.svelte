<script>
  export let id;
  export let name;
  export let isCompleted;
</script>

<div class="list-item">
  <h1>{name}</h1>
  <h2>{isCompleted}</h2>
  <h3>{id}</h3>
</div>

<style>
    .list-item {
        background-color: green;
    }
</style>
