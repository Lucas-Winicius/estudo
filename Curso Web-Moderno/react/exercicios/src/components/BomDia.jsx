import { Fragment } from "react";

export default props => [
    <h1 key={1}>Bom Dia {props.nome}, Você tem {props.idade} anos!</h1>,
    <h2 key={2}>Até Breve!</h2>
]

// export default props => 
//     <div>
//         <h1>Bom Dia {props.nome}, Você tem {props.idade} anos!</h1>
//         <h2>Até Breve!</h2>
//     </div>

// export default props => 
//     <Fragment>
//         <h1>Bom Dia {props.nome}, Você tem {props.idade} anos!</h1>
//         <h2>Até Breve!</h2>
//     </Fragment>