<script>
  import { data } from "./store.js";

  export let id;
  export let name;
  export let isCompleted;

  const updateTodoHandler = (id) => {
    const todo = $data.find((todo) => todo.id === id);
    todo.isCompleted = !todo.isCompleted;
    $data = [...$data]; // <-- rerender data
  };

  const deleteTodoHandler = (id) => {
    $data = $data.filter((todo) => todo.id !== id);
  };
</script>

<div class="list-item">
  <li>
    <input
      type="checkbox"
      checked={isCompleted}
      on:click={() => updateTodoHandler(id)}
    />
    <span class={isCompleted ? "name crossed" : ""}>{name}</span>
    <span class="close">
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

  .close {
    cursor: pointer;
    position: absolute;
    top: 50%;
    right: 0%;
    padding: 12px 16px;
    transform: translate(0%, -50%);
  }

  .close:hover {
    color: red;
  }

  .name.crossed {
    text-decoration: line-through;
  }
</style>
