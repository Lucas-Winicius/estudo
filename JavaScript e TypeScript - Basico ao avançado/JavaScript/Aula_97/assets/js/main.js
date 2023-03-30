function handleChange() {
  const resultado = document.querySelector('.resultado');

  const l_min = 'abcdefghijklmnopqrstuvwxyz'.split('');
  const l_mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
  const num = '1234567890'.split('');
  const sim = '!@#$%&-_^'.split('');

  const tamanhoDaSenha = parseInt(
    document.querySelector('input[type="number"]').value
  );
  const has_LMin = document.querySelector('#l_min').checked;
  const has_LMai = document.querySelector('#l_mai').checked;
  const hasNum = document.querySelector('#nums').checked;
  const hasSimb = document.querySelector('#simb').checked;

  let conjuntoFinal = [];

  if (has_LMin) conjuntoFinal = conjuntoFinal.concat(l_min);
  if (has_LMai) conjuntoFinal = conjuntoFinal.concat(l_mai);
  if (hasNum) conjuntoFinal = conjuntoFinal.concat(num);
  if (hasSimb) conjuntoFinal = conjuntoFinal.concat(sim);

  if (!tamanhoDaSenha || !conjuntoFinal.length) {
    return (resultado.innerHTML =
      'Selecione alguma opção ou defina o tamanho da senha');
  }

  let senha = '';
  for (let i = 0; i < tamanhoDaSenha; i++) {
    senha += conjuntoFinal[Math.floor(Math.random() * conjuntoFinal.length)];
  }

  resultado.innerHTML = senha;
}

document.addEventListener('change', handleChange);
document.querySelectorAll('input[type="number"]')[0].oninput = handleChange;
handleChange();
