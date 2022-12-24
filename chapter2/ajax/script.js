document.addEventListener('DOMContentLoaded', () => {
  const divOfTitles = document.querySelector('#titles');
  const URL = 'https://jsonplaceholder.typicode.com/posts';

  fetch(URL)
    .then((response) => response.json())
    .then((data) => {
      for (let i = 0; i < data.length; i++) {
        divOfTitles.insertAdjacentHTML('beforeend', `<p>${data[i].title}</p>`);
      }
    });
});
