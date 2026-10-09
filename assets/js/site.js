(() => {
  'use strict';
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#site-nav');
  if (toggle && nav) {
    document.documentElement.classList.add('menu-ready');
    const closeMenu = () => toggle.setAttribute('aria-expanded', 'false');
    toggle.addEventListener('click', () => toggle.setAttribute('aria-expanded', String(toggle.getAttribute('aria-expanded') !== 'true')));
    nav.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') { closeMenu(); toggle.focus(); }
    });
    document.addEventListener('click', event => { if (!event.target.closest('.header-inner')) closeMenu(); });
  }
  const dialog = document.querySelector('#donation-dialog');
  document.querySelectorAll('[data-donation]').forEach(link => link.addEventListener('click', event => {
    if (dialog && typeof dialog.showModal === 'function') { event.preventDefault(); dialog.showModal(); }
  }));
  if (dialog) dialog.addEventListener('click', event => {
    const rect = dialog.getBoundingClientRect();
    if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
  });
  const calculator = document.querySelector('#impact-calculator');
  if (calculator) {
    calculator.addEventListener('submit', event => event.preventDefault());
    const update = () => {
      const price = Number(calculator.querySelector('[name="plan"]:checked').value);
      const count = Number(calculator.querySelector('[name="count"]').value);
      const cards = price === 75;
      document.querySelector('#impact-count-label').textContent = cards ? 'Number of punch cards' : 'Number of months';
      document.querySelector('#impact-total').textContent = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 }).format(price * count);
      document.querySelector('#impact-detail').textContent = cards ? `${count} punch ${count === 1 ? 'card' : 'cards'} · ${count * 10} visits` : `${count} ${count === 1 ? 'month' : 'months'} of unlimited adaptive membership`;
    };
    calculator.addEventListener('change', update);
    update();
  }
  const contact = document.querySelector('#contact-form');
  if (contact) {
    document.querySelector('#preview-message').disabled = false;
    contact.addEventListener('submit', event => {
      event.preventDefault();
      const name = contact.elements.name.value.trim();
      const message = contact.elements.message.value.trim();
      if (!name || !message) {
        const field = !name ? contact.elements.name : contact.elements.message;
        field.setCustomValidity('Please add text for the inquiry preview.'); field.reportValidity();
        field.addEventListener('input', () => field.setCustomValidity(''), { once: true }); return;
      }
      document.querySelector('#contact-preview').textContent = `${name} · ${contact.elements.interest.value}\n\n${message}`;
      const result = document.querySelector('#contact-result'); result.hidden = false; result.focus();
    });
  }
})();
