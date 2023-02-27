document.addEventListener('click', (e) => {
  const el = e.target;
  const tag = el.tagName.toLowerCase();

  if (tag === 'a') {
    e.preventDefault();
    carregaPagina(el);
  }
});

async function carregaPagina(el) {
  const href = el.getAttribute('href');
  try {
    const resposta = await fetch(href);
    
    if(resposta.status !== 200) throw new Error(response.statusText)
    
    const respostaHTML = await resposta.text();
    carregaResultado(respostaHTML);
  } catch (e) {
    console.error(e);
  }

  // .then(response => {
  //   if(response.status !== 200) throw new Error(response.statusText)
  //   return response.text();
  // })
  // .then(html => carregaResultado(html))
  // .catch(error => console.error(error))
}

function carregaResultado(html) {
  const resultado = document.querySelector('.resultado');
  resultado.innerHTML = html;
}
