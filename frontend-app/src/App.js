import React from 'react';
import Dashboard from './components/dashboard'
import './static/css/common.css';


class App extends React.Component {
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
        <div className="application">
          <h1><center>Policy Management Dashboard</center></h1>
          <Dashboard selected_mode={this.state.selected_mode} setSelectedMode={this.setSelectedMode} />
        </div>
      );
  }
}

export default App;
