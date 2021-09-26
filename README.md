##                                [Insurance_Solutions](https://github.com/adarsh2104/Insurance_Solutions)  

A REST API based applications with following salient features: (Visuals)[https://github.com/adarsh2104/Insurance_Solutions/tree/master/Visuals]

### [Frontend](https://github.com/adarsh2104/Insurance_Solutions/tree/master/frontend-app): React.JS 
##### [Frontend Template](https://coreui.io/react/)

1. Home Page:
  * Minimalistic Home page with Buttons for navigating to Policy Search Page and Monthly Purchase Data Page.

<p align="center"><img width="100%" height="700px"  src="https://github.com/adarsh2104/Insurance_Solutions/blob/master/Visuals/01.Policy%20Management%20Dashboard%20Home.png" ></img></p>

2.Policy Search Page :
  * Implemeted Simple Form using Input component from [reactstrap](https://reactstrap.github.io/).
  * Added a loader component to show processing request [react-loader](https://www.npmjs.com/package/react-loader)
  * Option to find Policy using Policy ID and Customer ID.
  * Option to Edit/Update the premium value from the result table impplemeted using javascript event handler functions.
<p align="center"><img width="100%" height="700px" src="https://github.com/adarsh2104/Insurance_Solutions/blob/master/Visuals/03.Policy%20Results%20View%20Page.png"></img></p>

3.Results Table:
  * Policy ID and its attributes are presented in tabular format.
  * Used conditional rendering using state variables to control the behaviour of result table and its attributes.
  * Conditional rendering of table attributes based on state variables.
  * Option to Edit/Update the premium value from the result table impplemeted using javascript event handler functions.

<p align="center"><img width="100%" height="700px" src="https://github.com/adarsh2104/Insurance_Solutions/blob/master/Visuals/04.Policy%20Results%20Edit%20Form.png"></img></p>

4.Region Wise data View Page:
 * Created a interarctive Bar chart using (Chart.js) [https://www.npmjs.com/package/react-chartjs-2] library wrappper for react.js
 * Used react state variables for managing chart component. 
<p align="center"><img width="100%" height="700px" src="https://github.com/adarsh2104/Insurance_Solutions/blob/master/Visuals/08.Monthly%20Policy%20Purchase%20Region%20Chart%20View.png"></img></p>

### [Backend](https://github.com/adarsh2104/Insurance_Solutions/tree/master/bcg_insurance_solutions): Python + Django+Django REST

5.[Views](https://github.com/adarsh2104/Insurance_Solutions/blob/master/agent_dashboard/views.py):
 * Class Based API Views for GET and POST requests.
 * Used Django for Rest APIs.
 * Model Serializers for serializing/deserializing objects of Policy Model.
 * (Added logger) [https://github.com/adarsh2104/Insurance_Solutions/blob/master/Loggers/logfile] for performing project maintainacee related tasks on the backend.

6.[Models](https://github.com/adarsh2104/Insurance_Solutions/blob/master/agent_dashboard/models.py):
 * Models for saving Policy and Customer data.
 * Implemented Foreign Key relation between the models.

7.[Utils](https://github.com/adarsh2104/Insurance_Solutions/tree/master/agent_dashboard/utils):
 * Implemented (Custom field validator) [https://github.com/adarsh2104/Insurance_Solutions/blob/master/agent_dashboard/utils/custom_field_validators.py] for premium field in Policy Model .
 * (Data Importing functions) [https://github.com/adarsh2104/Insurance_Solutions/blob/master/agent_dashboard/utils/policy_data_import.py ] for importing policy data through various data pipelines(CSV implemented). 
 * Implemeted common function class for clean and detailed reporting of serializer errors.

### [Database](https://github.com/adarsh2104/Insurance_Solutions/blob/master/mysql-table-schema/BCG_Insurance_Data_Table_schema.sql): SQL
 * Used MySQL database for saving Policy and Customer Model objects.
 
 <p align="center"><img width="100%" height="700px" src="https://github.com/adarsh2104/Insurance_Solutions/blob/master/Visuals/10.Customer%20Table%20schema%20with%20data.png"></img></p>
 <p align="center"><img width="100%" height="700px" src="https://github.com/adarsh2104/Insurance_Solutions/blob/master/Visuals/11.Policy%20Table%20schema%20with%20data.png"></img></p>
 
 
 ## Running the code : On Ubuntu

### Frontend: 

Navigate to the `frontend-app directory`:

```bash
cd frontend-app
```

Install the dependencies from npm:

``` bash
sudo npm install
```

Run the dev server (starts on localhost:3001/3000):

```bash
sudo npm start
```

### Backend:

To get the Django server running:

Install the requirements from pip

```bash
pip install -r requirements.txt
```

Run django's development server (starts on localhost:8000):

```bash
python manage.py runserver
```


### Stacks Used:
* Python 3.7
* Django 3.2.6
* DRF 3.12.4
* React.JS/CSS
* MySQL
* Chart.js 3.0.5


:star2::star2::star2:

