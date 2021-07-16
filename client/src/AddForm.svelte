<script>
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  import { v4 as uuidv4 } from "uuid";

  let todo = {
    id: uuidv4(),
    name: "",
    isCompleted: false,
  };

  const addTodoHandler = (e) => {
    e.preventDefault();
    dispatch("addtodo", todo);
    todo = {
      id: uuidv4(),
      name: "",
    };
  };
</script>

<form on:submit={addTodoHandler}>
  <input type="text" placeholder="todo" bind:value={todo.name} required />
  <input type="submit" value=" + " />
</form>

<style>
  form {
    margin-top: 3rem;
  }

  input[type="submit"] {
    background-color: rgb(99, 0, 156);
    color: white;
    cursor: pointer;
  }
</style>
