const description = document.querySelector(".card-text");
const moreBtn = document.querySelector("#more");

moreBtn.addEventListener("click",()=>{
    if(description.classList.contains("show-more")) {
        description.classList.remove("show-more");
        moreBtn.innerHTML = "더보기";
    } else {
        description.classList.add("show-more");
        moreBtn.innerHTML = "접기";
    }
});