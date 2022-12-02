// Code inspiration: https://codepen.io/anon/pen/pvGrrW

let ingredsNodes = document.querySelectorAll('.ingredients');
let instrNodes = document.querySelectorAll('.instructions')

function splitElements(nodeList, separator) {
    nodeList.forEach(function (node) {
    splitNode = node.innerHTML.split(separator);
    let elementHTML = [];
    splitNode.forEach(function (splitNode) {
        elementHTML.push('<li>' + splitNode + '</li>')
    });
    node.innerHTML = elementHTML.join('')
});
}

splitElements(ingredsNodes, ";");
splitElements(instrNodes, ';')