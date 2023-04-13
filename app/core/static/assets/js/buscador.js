const searchBar = document.getElementById('buscador');
    
searchBar.addEventListener('keyup', function() {
  const query = searchBar.value.toLowerCase();

  const cards = document.querySelectorAll('.card');

  cards.forEach(card => {
    const title = card.querySelector('h2').textContent.toLowerCase();
    if (title.startsWith(query)) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
});