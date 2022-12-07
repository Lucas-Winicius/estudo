import './App.css';
import HelloWorld from './components/HelloWorld'

function App() {
  const name = 'Lucas'
  const processedName = name.toLocaleUpperCase()

  const sum = (a, b) => a + b

  const url = "https://via.placeholder.com/150"

  return (
    <div className="App">
      <h1>Olá, Mundo</h1>
      <p>Meu Segundo APP</p>
      <p>Boa Tarde {processedName}!</p>
      <p>Soma: { sum(10, 3) }</p>
      <img alt='Minha Imagem' src={url} />
      <HelloWorld />
    </div>
  );
}

export default App;
