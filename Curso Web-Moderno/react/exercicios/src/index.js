import React from 'react'
import ReactDOM from 'react-dom'
// const elemento = <h1>React 2</h1>
// import Primeiro from './components/Primeiro'
// import BomDia from './components/BomDia'
import Cumprimentos, { BoaNoite } from './components/Multiplos'

// ReactDOM.render(elemento, document.getElementById('root'))

// ReactDOM.render(<Primeiro />, document.getElementById('root'))

// ReactDOM.render(<BomDia nome="Lucas" idade={10} />, document.getElementById('root'))

ReactDOM.render(<div>
    <Cumprimentos.BoaTarde nome="Lucas"/>
    <BoaNoite nome="Leo"/>
</div>, document.getElementById('root'))