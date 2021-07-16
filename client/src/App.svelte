<script>
  import { v4 as uuidv4 } from "uuid";

  import Nav from "./Nav.svelte";
  import AddForm from "./AddForm.svelte";
  import ListItem from "./ListItem.svelte";

  const addTodoHandler = (e) => {
    const newTodo = e.detail;
    data = [...data, newTodo];
  };

  const updateTodoHandler = (e) => {
    const id = e.detail;
    const todo = data.find((todo) => todo.id === id);
    todo.isCompleted = !todo.isCompleted;
    data = [...data]; // <-- rerender data
  };

  const deleteTodoHandler = (e) => {
    const id = e.detail;
    data = data.filter((todo) => todo.id !== id);
  };

  let data = [
    {
      id: uuidv4(),
      name: "Walk the dog",
      isCompleted: false,
    },
    {
      id: uuidv4(),
      name: "Wash the dishes",
      isCompleted: true,
    },
    {
      id: uuidv4(),
      name: "Cook a meal",
      isCompleted: false,
    },
  ];
</script>

<main>
  <Nav />
  <div class="wrapper">
    <AddForm on:addtodo={addTodoHandler} />
  </div>
  <div class="list">
    <ul>
      {#each data as todo}
        <ListItem
          on:updatetodo={updateTodoHandler}
          on:deletetodo={deleteTodoHandler}
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
    margin: 0 auto;
    list-style: inside;
  }

  li {
    display: block;
    border: 1px solid black;
    margin: 1rem;
    background-color: lightgray;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
