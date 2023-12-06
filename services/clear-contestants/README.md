Clear Contestants Service
=======================================

This microservice removes contestants. Two actions are allowed:
   * Remove all contestants.
   * Remove all contestants without a team.
It uses AWS.


### Create the Service Package 

Create a package of this service to upload to the lambda on AWS this way:
* Execute this script: <br />
./scripts/package.sh
<br />  <br />

* Upload the zip file generated in the 'build' directory to the AWS Lambda: <br /> 
lambda.zip
