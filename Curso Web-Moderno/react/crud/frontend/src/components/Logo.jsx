import '../css/Logo.css'
import logo from '../images/logo.png'

const Logo = (props) => 
<aside className="logo">
    <a href="/" className="logo">
        <img src={logo} alt="Logo" />
    </a>
</aside>

export default Logo