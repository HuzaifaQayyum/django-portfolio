/**
 * Hero type effect
 */
 const typed = select('.typed')
 if (typed) {
   let typed_strings = typed.getAttribute('data-typed-items')
   typed_strings = typed_strings.split(',')
   new Typed('.typed', {
     strings: typed_strings,
     loop: true,
     typeSpeed: 150,
     backSpeed: 70,
     backDelay: 1500
   });
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
 window.addEventListener('load', () => {
   let portfolioContainer = select('.portfolio-container');
   if (portfolioContainer) {
     let portfolioIsotope = new Isotope(portfolioContainer, {
       itemSelector: '.portfolio-item'
     });
 
     let portfolioFilters = select('#portfolio-flters li', true);
 
     on('click', '#portfolio-flters li', function (e) {
       e.preventDefault();
       portfolioFilters.forEach(function (el) {
         el.classList.remove('filter-active');
       });
       this.classList.add('filter-active');
 
       portfolioIsotope.arrange({
         filter: this.getAttribute('data-filter')
       });
       portfolioIsotope.on('arrangeComplete', function () {
         AOS.refresh()
       });
     }, true);
   }
 
 });
 
 /**
  * Initiate portfolio lightbox 
  */
 const portfolioLightbox = GLightbox({
   selector: '.portfolio-lightbox'
 });
 
 /**
  * Initiate portfolio details lightbox 
  */
 const portfolioDetailsLightbox = GLightbox({
   selector: '.portfolio-details-lightbox',
   width: '90%',
   height: '90vh'
 });
 
 /**
  * Portfolio details slider
  */
 new Swiper('.portfolio-details-slider', {
   speed: 400,
   loop: true,
   autoplay: {
     delay: 5000,
     disableOnInteraction: false
   },
   pagination: {
     el: '.swiper-pagination',
     type: 'bullets',
     clickable: true
   }
 });
 
 /**
  * Testimonials slider
  */
 new Swiper('.testimonials-slider', {
   speed: 600,
   loop: true,
   autoplay: {
     delay: 5000,
     disableOnInteraction: false
   },
   slidesPerView: 'auto',
   pagination: {
     el: '.swiper-pagination',
     type: 'bullets',
     clickable: true
   }
 });


 /**
 * Animation on scroll
 */
window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: 'ease-out',
      mirror: false,
      once: true
    })
  });