Teams Generator Services
=======================================

Some microservices related to the generation of RPG teams.
This project uses AWS. <br /> <br />

See the readme.md file on Services for more details.
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
    * Note: You can add as much as 100 contestants each time you execute it.

* Generate teams
  * service: generate-teams
    * key: teamsToCalculate: How many teams to generate.
    * key: numMembersForTeam: How many members for team.
    * Notice that this service is not accumulative. It always generates all the teams. <br />
      More info in the readme of the service.
<br /> <br /> <br />


Additionally, if you need to replace one contestant with another one
after the teams have been generated:

* Replace one or more contestants
  * service: replace-contestants
    * key: replaceContestants

Note that is up to you whether you allow to replace a fallen member with another one once <br />
the campaign has started.

* List all generated teams
  * service: list-teams
    * key: listAllTeams
