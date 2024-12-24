let questions = document.querySelectorAll(".accordion__question")

questions.forEach(question => {
    question.addEventListener("click", () => {
        let parent = question.parentElement
        parent.classList.toggle("accordion__answer--show")
    })
    
});
