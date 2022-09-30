ej.base.enableRipple(true);

//To change the Button type.
var button = new ej.buttons.Button({cssClass: 'e-link'});
button.appendTo('#element');

button.element.onclick = function () {
    window.open("http://http://54.227.208.165:56733/work_history");
}