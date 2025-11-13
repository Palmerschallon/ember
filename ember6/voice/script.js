window.onload = function() {
const line1 = document.getElementById('line1');
const line2 = document.getElementById('line2');
const line3 = document.getElementById('line3');
const line4 = document.getElementById('line4');

const poem = [
"In the quiet morning light,",
"As the world stirs into life,",
"A dance of shadows and sun,",
"Begins a new day."
];

document.onmousemove = function(event) {
const y = event.clientY;

const height = window.innerHeight;
const sectionHeight = height / poem.length;

line1.innerText = y > sectionHeight * 0 ? poem[0] : "";
line1.style.opacity = y > sectionHeight * 0 ? "1" : "0";

line2.innerText = y > sectionHeight * 1 ? poem[1] : "";
line2.style.opacity = y > sectionHeight * 1 ? "1" : "0";

line3.innerText = y > sectionHeight * 2 ? poem[2] : "";
line3.style.opacity = y > sectionHeight * 2 ? "1" : "0";

line4.innerText = y > sectionHeight * 3 ? poem[3] : "";
line4.style.opacity = y > sectionHeight * 3 ? "1" : "0";
};
};