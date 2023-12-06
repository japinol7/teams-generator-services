Reset Teams Generator Service
=======================================

This microservice reset all contestants to the default names and clear all teams.
It uses AWS.
<br />  <br />


### Create the Service Package 

Create a package of this service to upload to the lambda on AWS this way:
* Execute this script: <br />
./scripts/package.sh
<br />  <br />

* Upload the zip file generated in the 'build' directory to the AWS Lambda: <br /> 
lambda.zip
