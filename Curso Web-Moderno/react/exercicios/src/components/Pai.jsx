import Filho from "./Filho";

export default props => 
    <div>
        <h1>{props.nome} {props.sobrenome}</h1>
        <h2>Filhos</h2>
        <ul>
            <Filho nome="Lucas" sobrenome={props.sobrenome} />
            <Filho nome="Leonardo" sobrenome="Soares" />
            <Filho nome="Maria" sobrenome={props.sobrenome} />
            <Filho {...props} />
            <Filho {...props} nome="Carla" />
        </ul>
    </div>