const items = document.querySelectorAll('.nav__item')

window.onload = () => {
   for (let i of items) {
      setTimeout(() => { i.classList.add('show') }, 1000)
   }
}