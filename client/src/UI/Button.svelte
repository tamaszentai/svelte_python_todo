<script>
  export let className;
  export let typeName = false;
  export let isDisabled = false;
</script>

<button class={className} type={typeName} disabled={isDisabled} on:click>
  <slot />
</button>

<style>
  button {
    border-radius: 5px;
    transition: 0.2s;
    min-width: 2.5rem;
    cursor: pointer;
  }
  .red {
    background-color: salmon;
  }

  .red:hover {
    background-color: rgb(248, 194, 188);
  }

  .green {
    background-color: rgb(81, 238, 81)
  }

  .green:hover {
    background-color: rgb(172, 238, 172);
  }

  .lightseagreen {
    background-color: lightseagreen;
  }

  .lightseagreen:hover {
    background-color: rgb(40, 219, 210);
  }

  :disabled {
    text-decoration: line-through;
  }

  :disabled:hover {
    background-color: lightseagreen;
    cursor:initial;
  }
</style>
