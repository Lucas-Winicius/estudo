import '../css/Nav.css'
import NavComponent from './NavComponent'

const Nav = (props) => 
<aside className='menu-area'>
    <NavComponent link="#/" icon="home" label="Inicio"/>
    <NavComponent link="#/users" icon="users" label="Usuarios"/>
</aside>

export default Nav