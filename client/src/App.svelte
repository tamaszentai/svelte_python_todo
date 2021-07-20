<script>
  import { fade } from "svelte/transition";
  import { flip } from "svelte/animate";
  import { onMount } from "svelte";
  import { todos } from "./store.js";

  import axios from "axios";

  import Nav from "./Nav.svelte";
  import AddForm from "./AddForm.svelte";
  import ListItem from "./ListItem.svelte";
  import Modal from "./Modal.svelte";
  import Button from "./Button.svelte";

  let modalToggle = false;

  $: todosNumber = $todos.length;
  $: completed = $todos.filter((todo) => todo.isCompleted === true);
  $: completedTodosNumber = completed.length;

  onMount(async () => {
    axios.get("http://localhost:8000").then((res) => {
      $todos = res.data;
    });
  });

  const addTodoHandler = (e) => {
    const newTodo = e.detail;
    $todos = [...$todos, newTodo];
    axios.post("http://localhost:8000", newTodo);
  };

  const deleteAllHandler = () => {
    $todos = [];
    axios.delete("http://localhost:8000");
  };

  const openModal = () => {
    modalToggle = true;
  };

  const closeModal = () => {
    modalToggle = false;
  };
</script>

<main>
  {#if modalToggle}
    <Modal on:closemodal={closeModal}>
      <Button
        className={"red"}
        on:click={deleteAllHandler}
        on:click={closeModal}>YES</Button
      >
      <Button className={"green"} on:click={closeModal}>NO</Button>
    </Modal>
  {/if}
  <Nav />
  <div class="wrapper">
    <AddForm on:addtodo={addTodoHandler} />
    <!-- <button class="delete-all" on:click={openModal}>DELETE ALL</button> -->
    <Button className={"lightseagreen"} on:click={openModal} {todosNumber}
      >DELETE ALL</Button
    >
    <div class="counters">
      {completedTodosNumber}
      /
      {todosNumber}
    </div>
  </div>
  <div class="list">
    <ul>
      {#each $todos as todo (todo.id)}
        <div transition:fade animate:flip>
          <ListItem
            id={todo.id}
            name={todo.name}
            isCompleted={todo.isCompleted}
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
    min-height: 36rem;
    margin: 5rem auto;
    background-color: whitesmoke;
    border-radius: 5px;
  }
  .wrapper {
    text-align: center;
  }

  .counters {
    font-size: 1.5rem;
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

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
