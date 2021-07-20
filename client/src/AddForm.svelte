<script>
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  import { v4 as uuidv4 } from "uuid";

  import Button from "./Button.svelte";

  let todo = {
    id: uuidv4(),
    name: "",
    isCompleted: false,
  };

  const addTodoHandler = (e) => {
    dispatch("addtodo", todo);
    todo = {
      id: uuidv4(),
      name: "",
      isCompleted: false,
    };
  };
</script>

<form on:submit|preventDefault={addTodoHandler}>
  <!-- event modifier -->
  <input
    type="text"
    placeholder="Type something here..."
    bind:value={todo.name}
    required
  />
  <Button className={"lightseagreen"} typeName={"submit"}
    ><i class="fa fa-plus" aria-hidden="true" /></Button
  >
</form>

<style>
  form {
    margin-top: 3rem;
  }

  input[type=text] {
    width: 20rem;
    text-align: center;
  }
</style>
