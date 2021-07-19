<script>
  import { fade, fly } from "svelte/transition";
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  const closeModal = () => {
    dispatch("closemodal");
  };
</script>

<div class="modal-backdrop" in:fade={{duration: 200}} out:fade={{duration: 300}} on:click={closeModal} />
<div class="modal" in:fade={{duration: 500}} out:fly={{y:200, duration: 300}}>
  <h2>Are you sure you want to delete all Todos?</h2>
  <footer>
    <slot />
  </footer>
</div>

<style>
  .modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.75);
    z-index: 10;
  }

  .modal {
    position: fixed;
    top: 30vh;
    left: 10%;
    width: 80%;
    max-height: 80vh;
    background: whitesmoke;
    border-radius: 5px;
    z-index: 100;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
    overflow: scroll;
  }

  footer {
    text-align: center;
  }

  h2 {
    text-align: center;
  }

  @media (min-width: 768px) {
    .modal {
      width: 40rem;
      left: calc(50% - 20rem);
    }
  }
</style>
