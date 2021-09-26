import {server_back} from './local_config';
import axios from 'axios';


axios.defaults.headers.common = {
    'Sec-Fetch-Mode': 'cors'
  };


const config = {
    SEARCH_REQUEST        : server_back + 'search/',
    POLICY_EDIT           : server_back + 'search/policy_edit/',
    GET_REGION_WISE_DATA  : server_back + 'search/regions/',

    }


export default config;    