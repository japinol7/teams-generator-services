import json

from modules.config.config import (
    BODY_TEAMS_KEY,
    BODY_ERRORS_KEY,
    ERROR_TAG,
    LOG_END_SERVICE_MSG,
    LOG_START_SERVICE_MSG,
    IS_ADD_DEBUG_INFO_TO_RESPONSE,
    )
from modules.config.parser import ConfigParser
from modules.controller.controller import EventController
from modules.aws.s3_client import S3Client
from modules.team.team import calc_team
from modules.tools.logger.logger import logger as log
from modules.tools.utils.utils import read_file_as_string
from modules.log_validation import log_validation

config_parser = ConfigParser()
s3 = S3Client()


def lambda_handler(event, context):
    log.info(LOG_START_SERVICE_MSG)
    controller = EventController(event)
    num_teams = controller.get_teams_to_calculate()
    num_members = controller.get_num_members_for_team()
    if not controller.validate_input_values(num_teams, num_members):
        error_msg = log_validation.log_wrong_input_values(controller)
        log.info(LOG_END_SERVICE_MSG)
        error_msg_json = json.dumps(error_msg)
        s3.upload_teams(resource_name=config_parser['teams_gen_file_teams'], body=error_msg_json)
        return {
            'statusCode': 200,
            'body': error_msg_json,
        }

    res_file_names_contestants = config_parser['teams_gen_file_contestants']
    names = s3.get_contestants(res_file_names_contestants)

    names_sel = []
    body = {BODY_TEAMS_KEY: {}, BODY_ERRORS_KEY: {}}
    log.info(f"Generate {num_teams} Teams of {num_members} members")
    for i in range(num_teams):
        team_name = f'Team {i + 1}'
        team = calc_team(team_name, names, names_sel, num_members)
        body_key = BODY_TEAMS_KEY if team.get(team_name)[0] != ERROR_TAG else BODY_ERRORS_KEY
        body[body_key].update(team)
        # remove currently selected member names from the list of available names
        names = list(set(names) - set(names_sel))
        names_sel = []

    if IS_ADD_DEBUG_INFO_TO_RESPONSE:
        body['debug_info'] = {
            'teamsToCalculate': num_teams,
            'numMembersForTeam': num_members,
            }

    body_json = json.dumps(body)
    s3.upload_teams(resource_name=config_parser['teams_gen_file_teams'], body=body_json)
    log.info(LOG_END_SERVICE_MSG)
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': body_json,
        }


if __name__ == "__main__":
    event_json = read_file_as_string('events/event.json')
    res = lambda_handler(event=json.loads(event_json), context=None)
    log.info(res['body'])
