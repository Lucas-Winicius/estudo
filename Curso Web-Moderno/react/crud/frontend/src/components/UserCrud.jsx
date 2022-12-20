import { Component } from "react";
import Main from "./Main";

const HeaderProps = {
    icon: 'users',
    title: 'Usuarios',
    subtitle: 'Cadastro de usuarios: Incluir, Listar, Alterar e excluir!'
}

export default class UserCrud extends Component {
    render() {
        return (
            <Main {...HeaderProps}>
                Cadastro de usuario
            </Main>
        )
    }
}