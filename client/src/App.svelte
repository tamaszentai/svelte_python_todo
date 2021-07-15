<script>
  import { v4 as uuidv4 } from "uuid";

  import Nav from "./Nav.svelte";
  import AddForm from "./AddForm.svelte";
  import ListItem from "./ListItem.svelte";

  const addTodoHandler = (e) => {
	const newTodo = e.detail;
	data = [...data, newTodo];
  }

let data = [
	{
		id: uuidv4(),
		name: 'Walk the dog',
		isCompleted: false
	},
	{
		id: uuidv4(),
		name: 'Wash the dishes',
		isCompleted: true
	},
	{
		id: uuidv4(),
		name: 'Cook a meal',
		isCompleted: false
	},
]
</script>

<Nav />
<div class="wrapper">
  <AddForm on:addtodo={addTodoHandler}/>
</div>
<div class="list">
	{#each data as todo}
	<ListItem id={todo.id} name={todo.name} isCompleted={todo.isCompleted} />
	{/each}
</div>

<style>
  .wrapper {
    text-align: center;
  }

  .list {
	  text-align: center;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
