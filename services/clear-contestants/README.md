Clear Contestants Service
=======================================

This microservice removes contestants. Two actions are allowed:
   * Remove all contestants.
   * Remove all contestants without a team.
It uses AWS.
<br />  <br />


### Create the Service Package 

#### 1. Create the package with dockerfile 

Create a package of this service to upload to the lambda on AWS this way:
* Execute this script from the lambda folder: <br />
./scripts/package_with_dockerfile.sh
<br /> <br />

* Upload the zip file generated in the 'build' directory to the AWS Lambda: <br /> 
lambda.zip


#### 2. Create the package with a simple docker run.

Create a package of this service to upload to the lambda on AWS this way:
* Execute this script from the lambda folder: <br />
./scripts/package.sh
<br /> <br />

* Upload the zip file generated in the 'build' directory to the AWS Lambda: <br /> 
lambda.zip


#### 3. Create the package with a simple docker run. Windows version. 

This change is necessary because of limitations of Git Bash for Windows <br />
when resolving paths., 
Edit this file and replace PATH_TO_THIS_LAMBDA_ON_WINDOWS with the lambda path: <br />
./scripts/other/package-win-alt.sh

Create a package of this service to upload to the lambda on AWS this way:
* Execute this script from the lambda folder: <br />
./scripts/other/package-win-alt.sh
<br /> <br />

* Upload the zip file generated in the 'build' directory to the AWS Lambda: <br /> 
lambda.zip
