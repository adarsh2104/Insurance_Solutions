import React, { Component } from 'react';
import { HashRouter, Route, Switch } from 'react-router-dom';
import './scss/style.scss';
import Dashboard from './components/dashboard'
import './static/css/common.css';

const loading = (
  <div className="pt-3 text-center">
    <div className="sk-spinner sk-spinner-pulse"></div>
  </div>
)

// Containers
const TheLayout = React.lazy(() => import('./containers/TheLayout'));

// Pages
const Login = React.lazy(() => import('./views/pages/login/Login'));
const Register = React.lazy(() => import('./views/pages/register/Register'));
const Page404 = React.lazy(() => import('./views/pages/page404/Page404'));
const Page500 = React.lazy(() => import('./views/pages/page500/Page500'));

class App extends Component {
  constructor() {
    super();
    this.state = {
      selected_mode: null
    };
    this.setSelectedMode = this.setSelectedMode.bind(this)
  }

  setSelectedMode(event) {

    this.setState({ [event.target.name]: event.target.id })

  }

  render() {
    return (
      <HashRouter>
        <div className="application">
          
          <h1><center>Welcome to Policy Management Dashboard</center></h1>
          <Dashboard selected_mode={this.state.selected_mode} setSelectedMode={this.setSelectedMode} />
        </div>
          {!(this.state.selected_mode === 'search') && <React.Suspense fallback={loading}>
            <Switch>
              <Route exact path="/login" name="Login Page" render={props => <Login {...props}/>} />
              <Route exact path="/register" name="Register Page" render={props => <Register {...props}/>} />
              <Route exact path="/404" name="Page 404" render={props => <Page404 {...props}/>} />
              <Route exact path="/500" name="Page 500" render={props => <Page500 {...props}/>} />
              <Route path="/" name="Home" render={props => <TheLayout {...props}/>} />
            </Switch>
          </React.Suspense>
          }
      </HashRouter>
    );
  }
}

export default App;
