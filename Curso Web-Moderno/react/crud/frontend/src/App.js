import 'bootstrap/dist/css/bootstrap.min.css';
import 'font-awesome/css/font-awesome.min.css';
import './css/App.css'
import Logo from './components/Logo'
import Nav from './components/Nav'
import Footer from './components/Footer'
import { BrowserRouter } from 'react-router-dom'
import Routes from './components/Routes';



const App = props => 
  <BrowserRouter>
  <div className='app'>
    <Logo/>
    <Nav/>
    <Routes/>
    <Footer/>
  </div>
  </BrowserRouter>


export default App