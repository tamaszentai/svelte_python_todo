<script>
  import Nav from "./Nav.svelte";
  import AddForm from "./AddForm.svelte";
  import ListItem from "./ListItem.svelte";

  import { data } from "./store.js";

  const addTodoHandler = (e) => {
    const newTodo = e.detail;
    $data = [...$data, newTodo];
  };

  const deleteAllHandler = () => {
    $data = [];
  }
</script>

<main>
  <Nav />
  <div class="wrapper">
    <AddForm on:addtodo={addTodoHandler} />
    <button class="delete-all" on:click={deleteAllHandler}>DELETE ALL</button>
  </div>
  <div class="list">
    <ul>
      {#each $data as todo}
        <ListItem
          id={todo.id}
          name={todo.name}
          isCompleted={todo.isCompleted}
        />
      {/each}
    </ul>
  </div>
</main>

<style>
  main {
    width: 20rem;
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
