<script>
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  export let id;
  export let name;
  export let isCompleted;

  const updateTodoHandler = (id) => {
    dispatch("updatetodo", id);
  };

  const deleteTodoHandler = (id) => {
    dispatch("deletetodo", id);
  };
</script>

<div class="list-item">
  <li class={isCompleted ? "completed" : ""}>
    <span on:click={() => updateTodoHandler(id)}>{name}</span>
    <span class="delete" on:click={() => deleteTodoHandler(id)}>
      <i style="font-size:24px" class="fa">&#xf014;</i>
    </span>
  </li>
</div>

<style>
  li {
    border: 1px solid #ddd;
    margin-top: -1px;
    background-color: #f6f6f6;
    padding: 1rem 3rem;
    text-decoration: none;
    font-size: 18px;
    color: black;
    display: block;
    position: relative;
    transition: 0.2s;
    overflow: hidden;
  }

  li:hover {
    cursor: pointer;
    background-color: lightgray;
  }

  li.completed {
    background: rgb(114, 114, 114);
    color: whitesmoke;
    text-decoration: line-through;
  }

  li.completed:hover {
    background: rgba(114, 114, 114, 0.8);
  }

  li.completed::before {
    content: "";
    position: absolute;
    border-color: lightgreen;
    border-style: solid;
    border-width: 0 2px 2px 0;
    top: 1rem;
    left: 1rem;
    transform: rotate(45deg);
    height: 15px;
    width: 7px;
  }

  .delete {
    cursor: pointer;
    position: absolute;
    top: 50%;
    right: 0%;
    padding: 12px 1rem;
    transform: translate(0%, -50%);
  }

  .delete:hover {
    color: salmon;
  }
</style>
