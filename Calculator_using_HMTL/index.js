function appendToValue (value) {
    document.getElementById("display").value += value;
}

function calculate () {
    try {
        document.getElementById("display").value = eval(document.getElementById("display").value);
    }
    catch (error) {
        document.getElementById("display").value = "Error";
    }  
}

function allClear () {
    document.getElementById("display").value = "";
}

function deleteElement () {
    let value = document.getElementById("display").value;
    document.getElementById("display").value = value.slice(0,-1);
}
