// @ts-nocheck

//Анимации появления
ScrollReveal().reveal('.news__item:nth-of-type(2)', { delay: 200, distance: '20px', origin: 'top' })
ScrollReveal().reveal('.news__item', { distance: '20px', origin: 'top' })
ScrollReveal().reveal('.news__item:nth-child(3n)', { delay: 400, distance: '20px', origin: 'top' })
ScrollReveal().reveal('.news__item:nth-of-type(5)', { delay: 200, distance: '20px', origin: 'top' })
ScrollReveal().reveal('.header__content', { distance: '10px', origin: 'top' })
ScrollReveal().reveal('.home__title', { delay: 100, distance: '10px', origin: 'left' })
ScrollReveal().reveal('.home__descriprion', { delay: 200, distance: '10px', origin: 'right' })
ScrollReveal().reveal('.home__ask', { delay: 300, origin: 'bottom' })
ScrollReveal().reveal('.achivements__title', { distance: '10px', origin: 'top' })
ScrollReveal().reveal('.achivements__item:nth-of-type(2)', { delay: 200, distance: '20px', origin: 'top' })
ScrollReveal().reveal('.achivements__item', { distance: '20px', origin: 'top' })
ScrollReveal().reveal('.achivements__item:nth-child(3n)', { delay: 400, distance: '20px', origin: 'top' })
ScrollReveal().reveal('.achivements__item:nth-of-type(5)', { delay: 200, distance: '20px', origin: 'top' })
ScrollReveal().reveal('.about__title', { distance: '20px', origin: 'top' })
ScrollReveal().reveal('.about__content', { delay: 100, distance: '20px', origin: 'left' })
ScrollReveal().reveal('.contact__content', { delay: 200, distance: '20px', origin: 'right' })


//Прокрутка
document.addEventListener('click', (event) => {
   if (event.target.dataset.anchor) {
      console.log(1)
      event.preventDefault()
      document.querySelector(`#${event.target.dataset.anchor}`).scrollIntoView({ behavior: 'smooth' })
   }
})

window.onload = () => {
   console.log(1)
}