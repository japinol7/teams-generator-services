Teams Generator Services
========================

Some microservices related to the generation of RPG teams.
<br /> <br />

  Disclaimer: These services are meant as simple examples of <br />  
  AWS lambda services. The state of the system is persisted <br />
  using json files, one for the contestants and another one <br />
  for the generated teams. <br />
  Therefore, this solution does not mean to be scalable nor concurrent.
<br /> <br />


## Services available

* add-contestants
  * addContestants:
    * Adds contestants, so they can be chosen for a team.
    * Note: You can add as many as 100 contestants each time you execute it. <br />
      Maximum number of total contestants: 2100 

* clear-contestants
  * This microservice allows to:
    * clearAllContestants: Remove all contestants.
    * clearContestantsWithoutTeam: Removes all contestants without a team.

* clear-teams
  * clearAllTeams:
    * Deletes all generated teams.

* generate-teams
  * Generates one or more teams.
    * teamsToCalculate: How many teams to generate.
    * numMembersForTeam: How many members for team.
    * Notice that this service is not accumulative. It always generates all the teams. <br />
      More info in the readme of the service.

* list-contestants
  * listAllContestants
    * Lists all contestants, whether they are in a team or not.
  * listContestantsWithoutTeam 
    * Lists contestants that still do not have a team.
  * listContestantsInATeam 
    * Lists contestants that belong to a team. <br />
      It takes the contestants from the teams file, <br /
      without matching them with the contestants file.

* list-teams
  * listAllTeams: Lists all generated teams.

* remove-contestants
  * removeContestants: Remove one or more contestants. <br />
    This will remove them from the team they belong.

* reset-teams-generator
  * resetTeamsGenerator: Reset all contestants to the default names <br /> 
    and clear all teams.
  * For most use cases is best that the default file for contestants, <br />
    will be an empty event.
