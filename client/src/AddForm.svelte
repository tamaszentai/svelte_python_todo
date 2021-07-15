<script>
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  import { v4 as uuidv4 } from "uuid";

  let todo = {
    id: uuidv4(),
    name: '',
    isCompleted: true
  }

  const addTodoHandler = (e) => {
      e.preventDefault();
      dispatch("addtodo", todo);
      console.log(todo);
      todo = {
          id: uuidv4(),
          name: '',
          isCompleted: false
      }
  };
</script>

<form on:submit={addTodoHandler}>
  <input type="text" placeholder="todo" bind:value={todo.name} />
  <input type="submit" value="Add Todo" />
</form>

<style>
  form {
    margin-top: 3rem;
  }
</style>
