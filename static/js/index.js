/**
 * Hero type effect
 */
 const typed = select('.typed')
 if (typed) {
   let typed_strings = typed.getAttribute('data-typed-items')
   typed_strings = typed_strings.split(',')
   const typed_instance = new Typed('.typed', {
     strings: typed_strings,
     loop: true,
     typeSpeed: 150,
     backSpeed: 70,
     backDelay: 1500
   });

   new IntersectionObserver((entries, observer) => 
     entries.forEach(entry => entry.isIntersecting ? typed_instance.start() : typed_instance.stop()), {
       rootMargin: '10px'
     }).observe(typed)
 }
 



 /**
  * Skills animation
  */
 let skilsContent = select('.skills-content');
 if (skilsContent) {
   new Waypoint({
     element: skilsContent,
     offset: '80%',
     handler: function (direction) {
       let progress = select('.progress .progress-bar', true);
       progress.forEach((el) => {
         el.style.width = el.getAttribute('aria-valuenow') + '%'
       });
     }
   })
 }
 
 /**
  * Porfolio isotope and filter
  */
//  window.addEventListener('load', () => {
//    let portfolioContainer = select('.portfolio-container');
//    if (portfolioContainer) {
//      let portfolioIsotope = new Isotope(portfolioContainer, {
//        itemSelector: '.portfolio-item'
//      });
 
//      let portfolioFilters = select('#portfolio-flters li', true);
 
//      on('click', '#portfolio-flters li', function (e) {
//        e.preventDefault();
//        portfolioFilters.forEach(function (el) {
//          el.classList.remove('filter-active');
//        });
//        this.classList.add('filter-active');
 
//        portfolioIsotope.arrange({
//          filter: this.getAttribute('data-filter')
//        });
//        portfolioIsotope.on('arrangeComplete', function () {
//          AOS.refresh()
//        });
//      }, true);
//    }
 
//  });
 
 /**
  * Initiate portfolio lightbox 
  */
//  const portfolioLightbox = GLightbox({
//    selector: '.portfolio-lightbox'
//  });
 
 /**
  * Initiate portfolio details lightbox 
  */
//  const portfolioDetailsLightbox = GLightbox({
//    selector: '.portfolio-details-lightbox',
//    width: '90%',
//    height: '90vh'
//  });
 
 
 /**
  * Testimonials slider
  */

 const testimonialSlider = document.querySelector('.testimonials-slider');
 if (testimonialSlider) {
  const swiper = new Swiper('.testimonials-slider', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 4000,
      disableOnInteraction: false
    },
    spaceBetween: 100,
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  new IntersectionObserver((entries, observer) => {
    entries.forEach(entry =>
      entry.isIntersecting ? (swiper.autoplay.start() && swiper.attachEvents()) : 
                             (swiper.autoplay.stop() && swiper.detachEvents())
    )
  }, { rootMargin: '200px' }).observe(testimonialSlider)
}


 /**
 * Animation on scroll
 */
// window.addEventListener('load', () => {
//     AOS.init({
//       duration: 1000,
//       easing: 'ease-out',
//       mirror: false,
//       once: true
//     })
//   });