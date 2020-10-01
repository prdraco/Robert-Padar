// Handlebars "if"
const source = document.getElementById('ifHelper').innerHTML;
const template = Handlebars.compile(source);
const context = {
  opinion: true
}
const compiledHtml = template(context);
const debateElement = document.getElementById('debate');

debateElement.innerHTML = compiledHtml



// Handlebars "Each"
const source2 = document.getElementById('eachHelper').innerHTML;
const template2 = Handlebars.compile(source2);
const context2 = {
  newArray: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
};
const compiledHtml2 = template2(context2);
const displayElements = document.getElementById('display');

displayElements.innerHTML = compiledHtml2;



// Handlebars "Each" and "This"
const source3 = document.getElementById('languagesTemp').innerHTML;
const template3 = Handlebars.compile(source3);

const context3 = {
  languages: [{name: 'HTML'}, {name: 'CSS'}, {name: 'JavaScript'}]
};

const compiledHtml3 = template3(context3);

const displayGoals = document.getElementById('goals');
displayGoals.innerHTML = compiledHtml3;
