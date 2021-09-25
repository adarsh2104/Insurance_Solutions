import React from 'react';
import { Table } from 'reactstrap';
import { Container, Row, Col, Form, Button,Input,Label } from 'reactstrap';
import Sugguestions from './suggestions'
import config  from '../config/config';
import axios from 'axios';


class SearchForm extends React.Component {
    constructor() {
        super();
        this.editPremium = this.editPremium.bind(this)
    }

    // toggleEditState(event){
        
    //     const target = event.target
    //     let current_state = target.getAttribute("data-edit")
    //     console.log('=========>',current_state)
    //     target.setAttribute("data-edit",!current_state) 
        
    // }
    editPremium(event) {
        const row_id = event.target.id
        let button_element = document.getElementById(row_id)
        const edit_premium_element_id = row_id.replace("edit_policy_", "new_premium_");
        let edit_premium_element = document.getElementById(edit_premium_element_id)
        if (edit_premium_element.hidden === true){
            edit_premium_element.hidden = false
            button_element.innerText = button_element.innerText.replace('Edit','Save')

        } else if (edit_premium_element.hidden === false){
            if (edit_premium_element.value){
                const new_premium_value = edit_premium_element.value
                const edit_policy_id = edit_premium_element_id.replace('new_premium_','')
                const costomer_id = document.getElementById('customer_'+edit_policy_id)
                console.log('customer_'+edit_policy_id)
                let post_data = new FormData();
                post_data.append('premium',new_premium_value)
                post_data.append('policy_id',edit_policy_id)
                post_data.append('fk_customer',costomer_id.textContent)
                const url = config.POLICY_EDIT 
                axios.post(url,post_data,
                    {
                        headers: {
                          'Sec-Fetch-Mode': 'cors',
                        }
                    }
                )
                    .then(function (json) {
                        console.log('==>',json)
                        let response_data = json.data
                        if (response_data.errors !== ''){
                            alert(response_data.errors)
                        } else{
                            alert(response_data.message)
                            edit_premium_element.hidden = true;
                            let read_policy_premium_element = document.getElementById('read_policy_'+edit_policy_id)
                            console.log('read_policy_'+edit_policy_id,edit_premium_element.value)
                            read_policy_premium_element.textContent = edit_premium_element.value
                            


                            // window.location.reload();
                        }
                        // console.log('------------>',response_data)
                    })
                    .catch(function (error) {
                        
                        if (error.response)
                        alert(error.response.message);
                    });

            }else {
                alert('Please fill up the the new premium value')
            }

        }
    }
    render(props) {
        if (this.props.policy_data.length > 0) {
            return (
                <div>
                    <h2>Search Result : </h2>
                    <h3>Total Results: {this.props.policy_data.length}</h3>
                    {/* <h3>Review: <span style={{ color: this.props.review === 'Positive' ? 'Green' : 'Yellow' }}>{this.props.review}</span> </h3> */}

                    <Table id='result_table'>
                        <thead id="result_table_head">
                            <tr>
                                <th>Sr No.</th>
                                <th>Policy ID</th>
                                <th>Customer ID</th>
                                <th>Purchase Date</th>
                                <th>Premium (USD)</th>
                            </tr>
                        </thead>
                        <tbody>
                            {this.props.policy_data.map((row, index) => {
                                return (
                                    <tr key={index} className=" performance_row">
                                        <td className=" performance_col">{index+1}</td>
                                        <td className=" performance_col">{row.policy_id}</td>
                                        <td className=" performance_col" name='' id={"customer_"+row.policy_id}>{row.fk_customer}</td>
                                        <td className=" performance_col">{row.purchase_date}</td>
                                        <td className=" performance_col" id={"read_policy_"+row.policy_id}>{row.premium} <span style={{margin: '9px',marginLeft: '49px',position:'relative',right:'-100px'}}><Input id={"new_premium_"+row.policy_id} type='text' placeholder='New Premium' style={{width:'20%'}} hidden /><Button id={'edit_policy_'+row.policy_id} onClick={this.editPremium}>  Click To Edit </Button></span></td>
                                    </tr>

                                )
                            }
                            )
                            }
                        </tbody>
                    </Table>
                </div>
            );
        } else if (this.props.results_length === 0){
            return (
                <div>

                    <h1>No Match Found</h1>
                </div>
            )
        }
        
        
        else
            return (
                <div>

                    {/* <h1>Please Make a Search Request</h1> */}
                </div>
            )
    }
}

export default SearchForm;