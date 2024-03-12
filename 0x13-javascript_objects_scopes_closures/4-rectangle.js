#!/usr/bin/node
class Rectangle {
	constructor (w, h) {
		if ((w > 0) && (h > 0)) {
			this.width = w;
			this.height = h;
		}
	}

	print () {
		for (a = 0; a < this.height; a++) {
			let s = '';
			for (let i = 0; i < this.width; i++) {
				s += 'X';
			}
			console.log(s);
		}
	}

	rotate () {
		const aux = this.width;
		this.width = this.height;
		this.height = aux;
	}

	double () {
		this.width *= 2;
		this.height *= 2;
	}
}

module.exports = Rectangle;

