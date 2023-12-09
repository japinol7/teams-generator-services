List Contestants Service
=======================================

This microservice lists contestants that can be chosen for a team.
It uses AWS.

Event keys:

* listAllContestants
  * Lists all contestants, whether they are in a team or not.

* listContestantsNotInATeam 
  * Lists contestants that still do not have a team.

* listContestantsInATeam 
  * Lists contestants that belong to a team. <br />
    It takes the contestants from the teams file, <br /
    without matching them with the contestants file.
<br />  <br /> <br />


### Create the Service Package 

Create a package of this service to upload to the lambda on AWS this way:
* Execute this script: <br />
./scripts/package.sh
<br />  <br />

* Upload the zip file generated in the 'build' directory to the AWS Lambda: <br /> 
lambda.zip
