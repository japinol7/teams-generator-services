Clear Teams Service
=======================================

This microservice deletes all generated teams.
It uses AWS.
<br /> <br /> <br />


### Create the Service Package with one of these options

#### Option 1. Create the package with dockerfile 

Create a package of this service to upload to the lambda on AWS this way:
* Execute this script from the lambda folder: <br />
./scripts/package_with_dockerfile.sh
<br /> <br />

* Upload the zip file generated in the 'build' directory to the AWS Lambda: <br /> 
lambda.zip


#### Option 2. Create the package with a simple docker run.

Create a package of this service to upload to the lambda on AWS this way:
* Execute this script from the lambda folder: <br />
./scripts/package.sh
<br /> <br />

* Upload the zip file generated in the 'build' directory to the AWS Lambda: <br /> 
lambda.zip


#### Option 3. Create the package with a simple docker run. Windows version. 

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
<br /> <br />


#### Create a package for unit testing. 

You can use package options 2 and 3 to execute the unit tests inside the container. <br />
If the tests pass, the package will be created; <br />
otherwise, the package will not be created. <br />
We assume that the tests are written using pytest. <br />

To execute the unit tests, execute the script with the argument: --devtest
