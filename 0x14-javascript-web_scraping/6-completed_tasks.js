#!/usr/bin/node
const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request.get(url, (err, reponse, body) => {
	if (!err) {
		const todos = JSON.parse(body);
    const completed = {};
    todos.forEach((todo) => {
      if (todo.completed && completed[todo.userId] === undefined) {
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        completed[todo.userId] += 1;
      }
    });
    console.log(completed);
  }
});
