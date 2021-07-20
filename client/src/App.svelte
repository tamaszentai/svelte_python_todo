<script>
  import { fade } from "svelte/transition";
  import { flip } from "svelte/animate";
  import { onMount } from "svelte";
  import { todos } from "./Todo/store.js";

  import axios from "axios";

  import Header from "./UI/Header.svelte";
  import AddForm from "./Todo/AddForm.svelte";
  import ListItem from "./Todo/ListItem.svelte";
  import Modal from "./UI/Modal.svelte";
  import Button from "./UI/Button.svelte";

  let modalToggle = false;

  $: todosNumber = $todos.length;
  $: completed = $todos.filter((todo) => todo.isCompleted === true);
  $: completedTodosNumber = completed.length;

  let modalTitle = "";
  let errorModal = false;
  let deleteModal = false;

  onMount(() => {
    axios
      .get("http://localhost:8000")
      .then((response) => {
        if (response.statusText === "OK" && response.status === 200) {
          $todos = response.data;
        }
      })
      .catch((err) => {
        console.log(err);
        errorModalHandler()
      });
  });

  const addTodoHandler = (e) => {
    const newTodo = e.detail;
    axios
      .post("http://localhost:8000", newTodo)
      .then((response) => {
        if (response.statusText === "OK" && response.status === 200) {
          $todos = [...$todos, newTodo];
        }
      })
      .catch((err) => {
        console.log(err);
        errorModalHandler()
      });
  };

  const updateTodoHandler = (e) => {
    const id = e.detail;
    const todo = $todos.find((todo) => todo.id === id);
    todo.isCompleted = !todo.isCompleted;
    axios
      .put(`http://localhost:8000/${id}`, todo)
      .then((response) => {
        if (response.statusText === "OK" && response.status === 200) {
          $todos = [...$todos];
        }
      })
      .catch((err) => {
        console.log(err);
        errorModalHandler()
      });
  };

  const deleteTodoHandler = (e) => {
    const id = e.detail;
    axios
      .delete(`http://localhost:8000/${id}`)
      .then((response) => {
        if (response.statusText === "OK" && response.status === 200) {
          $todos = $todos.filter((todo) => todo.id !== id);
        }
      })
      .catch((err) => {
        console.log(err);
        errorModalHandler()
      });
  };

  const deleteAllHandler = () => {
    axios
      .delete("http://localhost:8000")
      .then((response) => {
        if (response.statusText === "OK" && response.status === 200) {
          $todos = [];
        }
      })
      .catch((err) => {
        console.log(err);
        errorModalHandler()
      });
  };

  const openModal = () => {
    modalToggle = true;
  };

  const closeModal = () => {
    modalToggle = false;
    errorModal = false;
    deleteModal = false;
  };

  const deleteAllModalHandler = () => {
    deleteModal = true;
    modalTitle = "Are you sure you want to delete all Todos?";
    openModal();
  };

  const errorModalHandler = () => {
    errorModal = true;
    modalTitle = "Something went wrong, please try again later...";
    openModal();
  };
</script>

<main>
  {#if modalToggle}
    <Modal on:closemodal={closeModal} {modalTitle}>
      {#if deleteModal}
      <Button
        className={"red"}
        on:click={deleteAllHandler}
        on:click={closeModal}>YES</Button
      >
      <Button className={"green"} on:click={closeModal}>NO</Button>
      {/if}

      {#if errorModal}
      <Button className={"lightseagreen"} on:click={closeModal}>OK</Button>
      {/if}
    </Modal>
  {/if}
  <Header />
  <div class="wrapper">
    <AddForm on:addtodo={addTodoHandler} />
    <Button
      className={"lightseagreen"}
      on:click={deleteAllModalHandler}
      isDisabled={!todosNumber}>DELETE ALL</Button
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
            on:deletetodo={deleteTodoHandler}
            on:updatetodo={updateTodoHandler}
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
    margin: 10rem auto;
    background-color: whitesmoke;
    border-radius: 5px;
  }
  .wrapper {
    text-align: center;
  }

  .counters {
    font-size: 1.5rem;
    transition: 0.2s;
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
