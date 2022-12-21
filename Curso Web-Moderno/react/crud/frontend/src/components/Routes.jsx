import { Redirect, Route, Router } from 'react-router';
import UserCrud from './UserCrud'
import Home from './Home'

const Routes = props => 
    <Router>
            <Route exact path="/" component={Home} />
            <Route exact path="/users" component={UserCrud} />
            <Redirect from='*' to="/" />
    </Router>

export default Routes