<script>
  import { fade } from 'svelte/transition';
  import { flip } from 'svelte/animate';
  import { onMount } from "svelte";
  import { todos } from "./store.js";

  import Nav from "./Nav.svelte";
  import AddForm from "./AddForm.svelte";
  import ListItem from "./ListItem.svelte";
  import Modal from "./Modal.svelte";
  import Button from "./Button.svelte";


  let modalToggle = false;

  onMount(async () => {
    fetch("http://localhost:8000")
      .then(res => {
        if (!res.ok) {
          throw new Error("Failed!");
        }
        return res.json();
      })
      .then(data => {
        console.log(data);
        $todos = [...data]
      })
      .catch((error) => {
        console.log(error);
      });
  });

  const addTodoHandler = (e) => {
    const newTodo = e.detail;
    $todos = [...$todos, newTodo];
    console.log($todos);
  };

  const deleteAllHandler = () => {
    $todos = [];
  };

  const openModal = () => {
    modalToggle = true;
  }

  const closeModal = () => {
    modalToggle = false;
  }
</script>

<main>
  {#if modalToggle}
  <Modal on:closemodal={closeModal}>
    <Button value={true}>YES</Button>
    <Button value={false}>NO</Button>
  </Modal>
  {/if}
  <Nav />
  <div class="wrapper">
    <AddForm on:addtodo={addTodoHandler} />
    <button class="delete-all" on:click={openModal}>DELETE ALL</button>
  </div>
  <div class="list">
    <ul>
      {#each $todos as todo (todo.id)}
      <div transition:fade animate:flip>
        <ListItem
          id={todo.id}
          name={todo.name}
          isImportant={todo.isImportant}
        />
      </div>
      {:else}
      <h1>No todos found</h1>
      {/each}
    </ul>
  </div>
</main>

<style>
  main {
    width: 30rem;
    min-height: 35rem;
    margin: 5rem auto;
    background-color: whitesmoke;
  }
  .wrapper {
    text-align: center;
  }

  .list {
    margin: 0 auto;
  }

  h1 {
    text-align: center;
  }

  ul {
    padding: 0;
    margin: 3rem auto;
    list-style: inside;
  }

  .delete-all:hover {
    color: red;
    cursor: pointer;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
