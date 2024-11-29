// Input field effects
document.querySelectorAll('.form input, .form textarea').forEach((input) => {
    input.addEventListener('keyup', (e) => {
      const label = input.previousElementSibling;
      if (e.target.value === '') {
        label.classList.remove('active', 'highlight');
      } else {
        label.classList.add('active', 'highlight');
      }
    });
  
    input.addEventListener('blur', (e) => {
      const label = input.previousElementSibling;
      if (e.target.value === '') {
        label.classList.remove('active', 'highlight');
      } else {
        label.classList.remove('highlight');
      }
    });
  
    input.addEventListener('focus', (e) => {
      const label = input.previousElementSibling;
      if (e.target.value === '') {
        label.classList.remove('highlight');
      } else {
        label.classList.add('highlight');
      }
    });
  });
  
  // Tab switching
  document.querySelectorAll('.tab a').forEach((tabLink) => {
    tabLink.addEventListener('click', (e) => {
      e.preventDefault();
  
      const parentTab = tabLink.parentElement;
      parentTab.classList.add('active');
      Array.from(parentTab.parentElement.children)
        .filter((li) => li !== parentTab)
        .forEach((sibling) => sibling.classList.remove('active'));
  
      const targetId = tabLink.getAttribute('href').substring(1);
      document.querySelectorAll('.tab-content > div').forEach((content) => {
        if (content.id === targetId) {
          content.style.display = 'block';
        } else {
          content.style.display = 'none';
        }
      });
    });
  });
