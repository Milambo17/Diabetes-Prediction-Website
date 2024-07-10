const modalContainer = document.querySelector('.modal-container');
const modals = modalContainer.querySelectorAll('.modal');
const readMoreBtns = modalContainer.querySelectorAll('.read-more');

readMoreBtns.forEach((btn, index) => {
  btn.addEventListener('click', () => {
    // Expand the modal
    modals[index].classList.add('expanded');
    
    // Make the expanded modal the main focus
    modals[index].classList.add('active');
    
    // Make the other modals less prominent
    for (let i = 0; i < modals.length; i++) {
      if (i !== index) {
        modals[i].classList.remove('active');
      }
    }
  });
});
