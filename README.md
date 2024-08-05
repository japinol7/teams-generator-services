Teams Generator Services
=======================================

Some microservices related to the generation of RPG teams.
This project uses AWS S3 and System Params. <br /> <br />

	General version: 0.1.6
	author: Joan A. Pinol
	author_nickname: japinol
	author_gitHub: japinol7
	author_twitter: @japinol
	Python requires: 3.12 or greater.

See the readme.md file on the Services readme file for more details.
<br /> <br />


### Usage

This is a recommended basic flow to use these services:

* Clear contestants
  * service: clear-contestants
    * key: clearAllContestants: Removes all contestants.

* Clear teams
  * service: clear-teams
    * key: clearAllTeams: Deletes all generated teams.

* Add contestants to the system
  * service: add-contestants
    * key: addContestants: Adds contestants, so they can be chosen for a team.
    * Note: You can add as many as 100 contestants each time you execute it.

* Generate teams
  * service: generate-teams
    * key: teamsToCalculate: How many teams to generate.
    * key: numMembersForTeam: How many members for team.
    * Notice that this service is not accumulative. It always generates all the teams. <br />
      More info in the readme of the service.
<br /> <br />


## How to execute this lambda from a local development environment

* Go to the lambda folder in your system
* If you want to add additional debug info to the lambda response:<br>
  $ export JAP_IS_ADD_DEBUG_INFO_TO_RESPONSE=true<br>
* Execute the lambda function script:<br>
  $ python lambda_function.py
