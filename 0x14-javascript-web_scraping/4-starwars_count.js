#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url, (err, response, body) => {
	if (!err) {
		const results = JSON.parse(body).results;
		const count = results.reduce((acc, movie) => {
			const characters = movie.characters;
			const containswedgeantilles = characters.some(character => character.endsWith('/18/'));
			if (containswedgeantilles) {
				return acc + 1;
			} else {
				return acc;
			}
		}, 0);
		console.log(count);
	} else {
		console.error(err);
	}
});
