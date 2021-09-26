import React from 'react';
import { Button, Container } from 'reactstrap';
import SearchForm from './search_form'
import MonthlyChart from './monthly_chart'

class Dashboard extends React.Component {
  render() {
    if (this.props.selected_mode == null) {
      return (
        <Container>
          <h1> Home Page</h1>
          <Button name='selected_mode' id='search' onClick={this.props.setSelectedMode}>Search Policy</Button>
          <Button name='selected_mode' id='monthly_data' onClick={this.props.setSelectedMode}>Check Monthly Policy Purchase Data</Button>
        </Container>
      )
    } else if (this.props.selected_mode === 'search') {
      return (
        <div>
          <SearchForm />
        </div>);
    } else if (this.props.selected_mode === 'monthly_data') {
      return (
        <div>
          <h1>Monthly Policy Purchase Data </h1>
          <MonthlyChart />
        </div>);
    }

  }
}

export default Dashboard;