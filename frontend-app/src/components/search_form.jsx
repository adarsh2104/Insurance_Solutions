// import React from 'react';
// import ReactDOM from 'react-dom';
import React from 'react';
import { Input, Button, Label } from 'reactstrap';
import axios from 'axios';
import config from '../config/config.js'
import SearchResult from './search_result'
import Loader from 'react-loader'
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";


class SearchForm extends React.Component {
    constructor() {
        super();
        this.state = {
            data: [],
            results_length : null,
            loaded: true
        };
        this.sendQueryRequest = this.sendQueryRequest.bind(this)
    }

    sendQueryRequest(event) {
        let self = this;
        const form = document.getElementById("query_form");
        const query_type = event.target.id
        const query = form.query.value
        if (query_type && form) {
            if (query) {
                const url = config.SEARCH_REQUEST + query_type+'/'+query
                console.log('====>',url)
                self.setState({ loaded: false });

                axios.get(url,
                    {
                        headers: {
                          'Sec-Fetch-Mode': 'cors',
                        }
                    }
                )
                    .then(function (json) {
                        console.log('==>',json.data.response_data)
                        let response_data = json.data.response_data
                        self.setState({ data: response_data,loaded: true ,results_length: response_data.length });
                    })
                    .catch(function (error) {
                        alert('Search Failed !! Please try again');
                        self.setState({ loaded: true });
                    });

            } else {
                alert('Please enter a valid Search ID !')
                self.setState({ loaded: true });
            }

        }

    }
    render() {
        return (
            <div>
                <h1>Please Make a Search Request</h1>
                <div>
                    <form id='query_form' >
                        <Label className="search_bar"> Search Policy: <Input name="query" type='number' placeholder="Eg: 420" /></Label>
                        <Button id='search_by_policy' onClick={this.sendQueryRequest}>  By Policy ID  </Button>
                        <Button id='search_by_customer' onClick={this.sendQueryRequest}>  By Customer ID  </Button>

                    </form>

                </div>
                <Loader loaded={this.state.loaded} >
                    <SearchResult policy_data={this.state.data} results_length={this.state.results_length} />
                </Loader>

            </div>
        );

    }
}

export default SearchForm;