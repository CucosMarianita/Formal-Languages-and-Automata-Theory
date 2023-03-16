
    let incepe = document.querySelector(".incepe")
    // st -- functia care aplica filtre
    function st(){
    fetch("http://localhost:3000/start")
    .then((response)=>response.json())
    .then(function(afisare){
        let el = document.createElement('div');
        // console.log(Object.keys(afisare))
        el.innerText = afisare;
        let content = document.querySelector('.content');
        content.innerText="";
        content.appendChild(el);
        console.log(JSON.stringify(afisare));
    });
    
}
    // let result = await response.json;

incepe.addEventListener('click', st);

let crawl = document.querySelector(".crawl");
// cr -- functia care face crawl
function cr(){
    fetch("http://localhost:3000/crawl")
    // .then((response)=>response.json())
    .then(function(afisare){
        console.log("crawling")})
}

crawl.addEventListener('click', cr);

