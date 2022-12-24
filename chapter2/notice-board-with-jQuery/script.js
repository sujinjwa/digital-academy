// vanillaJS 버전
// 모달 창에 제목과 내용 넣는 함수
function openModal(row) {
  const modalTitle = document.querySelector('.modal-title');
  const modalBody = document.querySelector('.modal-body');

  const title = row.querySelector('#title');
  const contents = row.querySelector('#contents');

  modalTitle.innerText = title.innerText;
  modalBody.innerText = contents.innerText;
}

document.addEventListener('DOMContentLoaded', async () => {
  // table에 내용 채워넣기
  const table = document.querySelector('.table-group-divider');

  const URL = 'https://jsonplaceholder.typicode.com/posts';
  await fetch(URL)
    .then((response) => response.json())
    .then((data) => {
      for (let i = 0; i < data.length; i++) {
        let title = data[i].title;
        let userId = data[i].userId;
        let contents = data[i].body;

        table.insertAdjacentHTML(
          'afterbegin',
          `<tr class="table-row" data-id="${
            i + 1
          }" data-bs-toggle="modal" data-bs-target="#exampleModal">
                  <th scope="row" class="text-center">${i + 1}</th>
                  <td class="text-center" id="title">${title}</td>
                  <td class="text-center" id="contents">${contents}</td>
                  <td class="text-center">${userId}</td>
                </tr>`
        );
      }
    });

  // 테이블의 각 행 클릭하면 모달 창 띄우기
  const rows = document.querySelectorAll('.table-row');

  for (let i = 0; i < rows.length; i++) {
    rows[i].addEventListener('click', () => {
      openModal(rows[i]);
    });
  }
});
