Teams Generator Services
=======================================

Some microservices related to the generation of RPG teams.
This project uses AWS S3 and System Params. <br /> <br />

  Disclaimer: These services are meant as simple examples of <br />  
  AWS lambda services. The state of the system is persisted <br />
  using json files, one for the contestants and another one <br />
  for the generated teams. <br />
  Therefore, this solution does not mean to be scalable nor concurrent.
<br /> <br />

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
