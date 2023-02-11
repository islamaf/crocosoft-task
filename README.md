# crocosoft-task

## How to run using docker
* Clone this repo.
* cd into the repo after cloning it.
* In terminal, ```docker compose up```.
* In postman or insomnia, use ```0.0.0.0:5000/``` as the app url.

## Endpoints
As requested, the 4 endpoints related to customers have been done.
* Add customer at ```/customers/add``` using POST method with the appropriate JSON body.
  * Fields available: name, email, password, phone, date_of_birth, address, driving_license_number
* Update customer at ```/customers/update/:id``` using PATCH method with the appropriate JSON body.
* Delete customer at ```/customers/delete/:id``` using DELETE method.
* Get customer at ```/customers/:id``` using GET method.

## ERD
![Alt text](crocosoft-car-rental.png?raw=true "ERD")
