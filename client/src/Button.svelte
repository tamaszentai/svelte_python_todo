<script>
    export let value;
</script>

<button class={value ? '' : 'button no'} on:click >
  <slot />
</button>

<style>
  button{
    font: inherit;
    border: 1px solid red;
    background: red;
    padding: 0.5rem 1rem;
    color: white;
    border-radius: 5px;
    box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.26);
    cursor: pointer;
    text-decoration: none;
  }

  button.no{
    font: inherit;
    border: 1px solid green;
    background: green;
    padding: 0.5rem 1rem;
    color: white;
    border-radius: 5px;
    box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.26);
    cursor: pointer;
    text-decoration: none;

  }
</style>
