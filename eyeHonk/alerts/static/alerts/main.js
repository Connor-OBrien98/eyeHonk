shine = id => {
    let sections = document.getElementById(id);
    console.log(sections);
    sections.setAttribute("style", "border: 5px solid lightgreen;");
    console.log('please lol');
}

removeShine = id => {
    let sections = document.getElementById(id);
    sections.removeAttribute("style");
}

alertShine = (id) => {
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