// @ts-nocheck

//Прокрутка
document.addEventListener('click', (event) => {
   if (event.target.tagName == 'BUTTON' || event.target.tagName == 'A') {
      event.preventDefault()
   }
   if (event.target.dataset.anchor) {
      event.preventDefault()
      document.querySelector(`#${event.target.dataset.anchor}`).scrollIntoView({ behavior: 'smooth' })
   }
})

//Появление блоков
function onEntry(entry) {
   entry.forEach(change => {
      if (change.isIntersecting) {
         change.target.classList.add('element-show');
      }
   });
}

let options = {
   threshold: [0.5]
};
let observer = new IntersectionObserver(onEntry, options);
let elements = document.querySelectorAll('.element-animation');

for (let elm of elements) {
   observer.observe(elm);
}

//Обнуление формы
document.querySelector('.contact__button').addEventListener('click', () => {
   document.querySelector('.contact__name').value = '';
   document.querySelector('.contact__question').value = '';
})