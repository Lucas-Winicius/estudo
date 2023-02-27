const request = (obj) => {
  const xhr = new XMLHttpRequest();
  xhr.open(obj.method, obj.url, true);
  xhr.send();

  xhr.addEventListener('load', (e) => {
    if (xhr.status >= 200 && xhr.status < 300) {
      obj.success(xhr.responseText);
    } else {
      obj.error({
        code: xhr.status,
        msg: xhr.statusText,
      });
    }
  });
};

document.addEventListener('click', (e) => {
  const el = e.target;
  const tag = el.tagName.toLowerCase();

  if (tag === 'a') {
    e.preventDefault();
    carregaPagina(el);
  }
});

function carregaPagina(el) {
  const href = el.getAttribute('href');
  request({
    method: 'GET',
    url: href,
    success(responseText) {
      const resultado = document.querySelector('.resultado');
      resultado.innerHTML = responseText;
    },
    error(e) {
      console.log(e);
    },
  });
}
