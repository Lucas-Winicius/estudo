// fetch('pessoas.json')
//   .then((res) => res.json())
//   .then((res) => loadResponse(res));

axios('pessoas.json')
  .then(res => loadResponse(res.data))


function loadResponse(res) {
  const divResponse = document.querySelector('div#res');
  const table = document.createElement('table');

  Array.from(res).forEach((people) => {
    const tr = document.createElement('tr');

    let td = document.createElement('td');
    td.innerHTML = people.nome;
    tr.appendChild(td);

    td = document.createElement('td');
    td.innerHTML = people.idade;
    tr.appendChild(td);

    td = document.createElement('td');
    td.innerHTML = people.salario;
    tr.appendChild(td);

    table.appendChild(tr);
  });
  divResponse.appendChild(table);
}
