/*
 * Add items to a list - from cssanimation.rocks/list-items/
 */

function addElement(element) {

    var list = document.getElementById('list');
    var newLI = document.createElement('li');
    newLI.innerHTML = element;
    list.appendChild(newLI);
}

$(document).ready(function () {

    $("#first").addClass("show");

    $("li").delay(100).each(function (i) {
        $(this).delay(500 * i).queue(function () {
            $(this).addClass("show");
        })
    })
});