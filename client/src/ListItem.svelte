<script>
  import { todos } from "./store.js";

  export let id;
  export let name;
  export let isImportant;

  const updateTodoHandler = (id) => {
    const todo = $todos.find((todo) => todo.id === id);
    todo.isImportant = !todo.isImportant;
    $todos = [...$todos]; // <-- rerender data
  };

  const deleteTodoHandler = (id) => {
    $todos = $todos.filter((todo) => todo.id !== id);
  };
</script>

<div class="list-item">
  <li class="{isImportant ? "name important" : ""}">
    <input
      type="checkbox"
      checked={isImportant}
      on:click={() => updateTodoHandler(id)}
    />
    <span>{name}</span>
    <span class="delete">
      <i
        style="font-size:24px"
        class="fa"
        on:click={() => deleteTodoHandler(id)}>&#xf014;</i
      >
    </span>
  </li>
</div>

<style>
  .list-item {
    overflow: hidden;
    /* word-break: break-all; */
  }

  li {
    border: 1px solid #ddd;
    margin-top: -1px;
    background-color: #f6f6f6;
    padding: 12px;
    text-decoration: none;
    font-size: 18px;
    color: black;
    display: block;
    position: relative;
  }

  .delete {
    cursor: pointer;
    position: absolute;
    top: 50%;
    right: 0%;
    padding: 12px 16px;
    transform: translate(0%, -50%);
  }

  .delete:hover {
    color: red;
  }

  .name.important {
    background: salmon;
  }
</style>
