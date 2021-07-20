<script>
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  import { v4 as uuidv4 } from "uuid";

  import Button from "../UI/Button.svelte";

  $: validName = isEmpty(name);

  let id = uuidv4();
  let name = "";
  let isCompleted = false;

  const addTodoHandler = () => {
    let todo = {
      id: id,
      name: name.trim(),
      isCompleted: isCompleted,
    };
    dispatch("addtodo", todo);
    id = uuidv4();
    name = "";
    isCompleted = false;
  };

  const isEmpty = (val) => {
    return val.trim().length === 0;
  };
</script>

<form on:submit|preventDefault={addTodoHandler}>
  <!-- event modifier -->
  <input
    type="text"
    placeholder="Type something here..."
    bind:value={name}
    required
  />
  <Button className={"lightseagreen"} typeName={"submit"} isDisabled={validName}
    ><i class="fa fa-plus" aria-hidden="true" /></Button
  >
</form>

<style>
  form {
    margin-top: 3rem;
  }

  input[type="text"] {
    width: 20rem;
    text-align: center;
  }
</style>
