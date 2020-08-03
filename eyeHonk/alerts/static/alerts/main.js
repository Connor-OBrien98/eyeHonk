//shine is a function that applys a border when hovered over
const shine = id => {
    let sections = document.getElementById(id);
    sections.setAttribute("style", "border: 5px solid lightgreen;");
}

//removeShine removes the style applied to a section
const removeShine = id => {
    let sections = document.getElementById(id);
    sections.removeAttribute("style");
}

//alertShine was used doing testing to alert the specific section when clicked
const alertShine = id => {
    if (id === "honk"){
        alert("Connor needs assistance!");
    } else if (id === "water") {
        alert("Connor needs water!");
    } else if (id === "food") {
        alert("Connor needs food!");
    } else if (id === "bathroom") {
        alert("Connor needs the bathroom!");
    }
}
