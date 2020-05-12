const add = document.querySelector(".add");
const errorMessage = document.querySelector(".error");
var input = document.querySelector(".input");
const container = document.querySelector(".container");

class item {
    constructor(itemName) {
        this.createDiv(itemName);
    }
    createDiv(itemName) {

        var checkBox = document.createElement('input');
        checkBox.setAttribute('type', 'checkbox');
        checkBox.classList.add('checkmark');

        var input = document.createElement('input');
        input.value = itemName;
        input.disabled = true;
        input.classList.add('item_input');
        input.type = "text";


        var itemBox = document.createElement('div');
        itemBox.classList.add('item');


        var editButton = document.createElement('button');
        editButton.innerHTML = "Edit";
        editButton.classList.add('editButton');
        editButton.addEventListener('click', () => this.edit(input));
        console.log("ikl");


        var deleteButton = document.createElement('button');
        deleteButton.innerHTML = "Delete";
        deleteButton.classList.add('deleteButton');
        deleteButton.addEventListener('click', () => this.delete(itemBox));
        console.log("qqq");

        container.appendChild(itemBox);

        itemBox.appendChild(checkBox);
        itemBox.appendChild(input);
        itemBox.appendChild(editButton);
        itemBox.appendChild(deleteButton);




    }
    edit(input) {
        input.disabled = !input.disabled;

    }

    delete(item) {
        container.removeChild(item);
    }


}

window.addEventListener('keydown', (e) => {
    errorMessage.style.display = "none";
    if (e.which == 13) {
        check();
    }
})
function check() {
    if (input.value != "") {
        new item(input.value);
        input.value = "";
    } else {
        errorMessage.style.display = "block";
        console.log("ppppp");

    }
}
add.addEventListener('click', check);

