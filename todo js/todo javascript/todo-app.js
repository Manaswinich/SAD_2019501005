const add = document.querySelector(".add");
var input = document.querySelector(".input");
const container = document.querySelector(".container");

class item {
    constructor(itemName) {
        this.createDiv(itemName);
    }
    createDiv(itemName) {
        var input = document.createElement('input');
        input.value = itemName;
        input.disabled = true;
        input.classList.add('item_input');
        input.type = "text";
        console.log("abc");

        var itemBox = document.createElement('div');
        itemBox.classList.add('item');
        console.log("def");

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
    if (e.which == 13) {
        check();
    }
})
function check() {
    if (input.value != "") {
        new item(input.value);
        input.value = "";
    }
}
add.addEventListener('click', check);

