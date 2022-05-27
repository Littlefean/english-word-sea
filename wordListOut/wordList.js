var wordArr = document.getElementsByClassName("word");
// for (let word of wordArr) {
// 	word.style.left = Math.random() * 1300 + 'px';
// 	word.style.top = Math.random() * 1000 + 'px';
// }


for (let i in wordArr) {
	console.log(i);
	wordArr[i].style.left = (i % 20) * 75 + 'px';
	wordArr[i].style.top = Math.floor(i / 20) * 25 + 'px';
}

var c = document.getElementById("myline");
//  计算画布的宽度
c.width = c.offsetWidth;
//  计算画布的高度
c.height = c.offsetHeight;

function line(x1, y1, x2, y2) {
	var ctx = c.getContext("2d");
	ctx.beginPath();
	ctx.moveTo(x1, y1);
	ctx.lineTo(x2, y2);
	ctx.stroke();
}
line(0, 0, 300, 400);
// line(300, 200, 100, 400);
// line(100, 500, 300, 400);
// line(100, 200, 600, 400);
