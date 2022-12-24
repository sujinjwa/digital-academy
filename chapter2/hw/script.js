const lists = document.querySelectorAll('.list-group-item');

const openModal = async (id) => {
  const URL = 'https://jsonplaceholder.typicode.com/posts/' + id;

  let modal = new bootstrap.Modal(document.getElementById('exampleModal'), {});
  let modalTitle = document.querySelector('#exampleModalLabel');
  let modalBody = document.querySelector('.modal-body');

  await fetch(URL)
    .then((response) => response.json())
    .then((data) => {
      modalTitle.innerText = data.title;
      modalBody.innerText = data.body;
    });

  modal.show();

  // 확인 버튼 클릭한 경우 모달창 닫기
  let modalBtn = document.querySelector('.closeBtn');

  modalBtn.addEventListener('click', () => {
    modal.hide();
  });
};

for (let i = 0; i < lists.length; i++) {
  lists[i].addEventListener('click', () => {
    openModal(i + 1);
  });
}
