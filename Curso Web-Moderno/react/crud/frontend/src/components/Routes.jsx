import { Redirect, Route, Router } from 'react-router'
import UserCrud from './UserCrud'
import Home from './Home'

const Routes = props => 
    <Router>
        <Route exact path="/" element={<Home/>}/>
        <Route path="/users" element={<UserCrud/>}/>
        <Redirect from='*' element={<Home/>} />
    </Router>

export default Routes