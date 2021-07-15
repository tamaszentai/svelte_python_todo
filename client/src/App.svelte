<script>
  import { v4 as uuidv4 } from "uuid";

  import Nav from "./Nav.svelte";
  import AddForm from "./AddForm.svelte";
  import ListItem from "./ListItem.svelte";

  const addTodoHandler = (e) => {
    const newTodo = e.detail;
    data = [...data, newTodo];
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
			<li>
			  <ListItem
				id={todo.id}
				name={todo.name}
				isCompleted={todo.isCompleted}
			  />
			</li>
		  {/each}
		</ul>
	  </div>
</main>




<style>
main {
	width: 30%;
	margin: 10rem auto;
	background-color: whitesmoke;
	border-radius: 15px;
	border: 1px solid black;
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
