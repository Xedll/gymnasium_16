// @ts-nocheck

//Прокрутка
document.addEventListener('click', (event) => {
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