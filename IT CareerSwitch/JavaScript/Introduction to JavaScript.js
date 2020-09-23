

alert("Hello World");
document.getElementById("demo").style.color="blue"

function myFunction() {
	console.log("Hello World")
}


//jQuery
function myFunction() {
	var obj = document.getElementById("h01");
	obj.innerHTML = "Hello jQuery";
}

function myFunction() {
	$("#h01").html("Hello jQuery")
}

//Summary
function appendText() {
	var txt1 = "<p>This is text along with html markup</p>"; //Create text with HTML
	var txt2 = $("<p></p>").text("This is text."); //Create text with jQuery
	var txt3 = document.createElement("p");
	txt3.innerHTML = "Text xreated using the DOM"; //Create text with the DOM
	$("body").append(text1, txt2, txt3); //Append new elements
}
