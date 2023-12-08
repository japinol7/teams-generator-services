Generate Teams Service
=======================================

This microservice generates teams from a fixed file of names.
It uses AWS.
<br />  <br />

Notice that this service is not accumulative. It always generates all the teams.
  * So, if you execute this service to generate 5 teams <br />
    and then you execute this service again,  <br />
    you will end up with 5 teams, instead of 10.  <br />
  * That is, only the last execution of this service counts.
<br />  <br />


### Create the Service Package 

Create a package of this service to upload to the lambda on AWS this way:
* Execute this script: <br />
./scripts/package.sh
<br />  <br />

* Upload the zip file generated in the 'build' directory to the AWS Lambda: <br /> 
lambda.zip
