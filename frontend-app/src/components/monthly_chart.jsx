import React, { Component } from 'react'
import { Form, Button, Input } from 'reactstrap';
import { Bar } from 'react-chartjs-2';
import config from '../config/config';
import axios from 'axios';

class MonthlyChart extends Component {
    constructor() {
        super();
        this.state = {
            chart_data: []
        };
        this.loadChartData = this.loadChartData.bind(this);
    }

    loadChartData(event) {
        var self = this;
        let select_region_el = document.getElementById('select_region')
        const selected_region = select_region_el.value

        if (selected_region) {
            const url = config.GET_REGION_WISE_DATA
            let post_data = new FormData();
            post_data.append('selected_region', selected_region)
            axios.post(url, post_data,
                {
                    headers: {
                        'Sec-Fetch-Mode': 'cors',
                    }
                }
            )
                .then(function (json) {
                    console.log('==>', json.data.response)
                    if (json.data) {
                        let reponse = json.data.response
                        self.setState({ chart_data: reponse })



                    }

                })
                .catch(function (error) {

                    if (error.response)
                        alert(error.response.message);
                });
        } else {
            alert('Please select a Region')
        }

    }
    render() {
        let chart_options = {
            labels: ['Jan', 'Feb', 'Mar',
                'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [
                {
                    label: 'Policies Bought',
                    backgroundColor: 'rgba(75,192,192,1)',
                    borderColor: 'rgba(0,0,0,1)',
                    borderWidth: 2,
                    data: this.state.chart_data
                }
            ]
        }
        return (
            <React.Fragment>
                <div >
                    <div>
                        <Form >
                            <Input type='select' id="select_region" >
                                <option value="" defaultValue> Available Regions </option>
                                <option value="east">  EAST  </option>
                                <option value="west">  WEST  </option>
                                <option value="north"> NORTH </option>
                                <option value="south"> SOUTH </option>
                            </Input>
                            <Button onClick={this.loadChartData} > Load Policy Purchase Data</Button>
                        </Form>
                    </div>
                    <div style={{ width: '50%', height: '50%', margin: 'auto' }}>
                        {this.state.chart_data.length > 0 && <Bar
                            data={chart_options}
                            options={{
                                title: {
                                    display: false,
                                    text: 'Regionwise Data for Policies Bought In Every Month',
                                    fontSize: 1
                                },
                                legend: {
                                    display: true,
                                    position: 'center'
                                }
                            }}
                        />}
                    </div>
                </div>
            </React.Fragment>
        )
    }
}

export default MonthlyChart