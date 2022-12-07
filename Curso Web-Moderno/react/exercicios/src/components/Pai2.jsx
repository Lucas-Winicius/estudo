import Filho from "./Filho";
import childrenWithProps from "../utilities/childrenWithProps";

export default props => 
    <div>
        <h1>{props.nome} {props.sobrenome}</h1>
        <h2>Filhos</h2>
        <ul>
            {/* {cloneElement(props.children, {...props, ...props.children.props})} */}
            { childrenWithProps(props) }
        </ul>
    </div>