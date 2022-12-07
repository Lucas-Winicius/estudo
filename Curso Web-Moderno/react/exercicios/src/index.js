import React from 'react'
import ReactDOM from 'react-dom'
// const elemento = <h1>React 2</h1>
// import Primeiro from './components/Primeiro'
// import BomDia from './components/BomDia'
// import Cumprimentos, { BoaNoite } from './components/Multiplos'
// import Saudacao from './components/Saudação'
import Pai from './components/Pai2'
import Filho from './components/Filho'


// ReactDOM.render(elemento, document.getElementById('root'))

// ReactDOM.render(<Primeiro />, document.getElementById('root'))

// ReactDOM.render(<BomDia nome="Lucas" idade={10} />, document.getElementById('root'))

// ReactDOM.render(
    // <div>
    //     <Cumprimentos.BoaTarde nome="Lucas"/>
    //     <BoaNoite nome="Leo"/>
    // </div>, document.getElementById('root'))
    
// ReactDOM.render(<Saudacao nome="Lucas" tipo="Boa Tarde" />, document.getElementById('root'))

// ReactDOM.render(
//     <div>
//         <Pai nome="Luiz" sobrenome='Souza'/>
//     </div>, document.getElementById('root'))

ReactDOM.render(
    <div>
        <Pai nome="Luiz" sobrenome='Winicius'>
            <Filho nome="Lucas" />            
            <Filho nome="Pedro" sobrenome="Silva" />            
            <Filho nome="Carla" sobrenome="Silva" />            
        </Pai>
    </div>, document.getElementById('root')
)
    