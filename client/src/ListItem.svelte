<script>
  export let id;
  export let name;
  export let isCompleted;


</script>

<div class="list-item">
    <p>
  <input type=checkbox checked={isCompleted}/>
  {name}
</p>
</div>

<style>
  .list-item {
    word-break: break-all;
  }

  p {
      padding: 0 1rem;
  }

</style>
