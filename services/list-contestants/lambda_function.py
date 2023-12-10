import json

from modules.config.config import (
    BODY_CONTESTANTS_KEY,
    BODY_ERRORS_KEY,
    LOG_END_SERVICE_MSG,
    LOG_START_SERVICE_MSG,
    )
from modules.config.parser import ConfigParser
from modules.controller.controller import EventController
from modules.aws.s3_client import S3Client
from modules.tools.logger.logger import logger as log
from modules.tools.utils.utils import read_file_as_string
from modules.log_validation import log_validation

config_parser = ConfigParser()
s3 = S3Client()


def get_contestants():
    res_file_names_contestants = config_parser['teams_gen_file_contestants']
    return set(s3.get_contestants(res_file_names_contestants))


def get_team_members():
    res_file_teams = config_parser['teams_gen_file_teams']
    teams, _ = s3.get_teams(res_file_teams)
    contestants_in_a_team = {member for sublist in teams.values() for member in sublist}
    return contestants_in_a_team


def lambda_handler(event, context):
    log.info(LOG_START_SERVICE_MSG)
    controller = EventController(event)
    is_list_all_contestants = controller.get_is_list_all_contestants()
    is_list_contestants_without_team = controller.get_is_list_contestants_without_team()
    is_list_contestants_in_a_team = controller.get_is_list_contestants_in_a_team()

    if not controller.validate_input_values(
            is_list_all_contestants, is_list_contestants_without_team, is_list_contestants_in_a_team):
        error_msg = log_validation.log_wrong_input_values(controller)
        log.info(LOG_END_SERVICE_MSG)
        error_msg_json = json.dumps(error_msg)
        return {
            'statusCode': 200,
            'body': error_msg_json,
        }

    body = {BODY_CONTESTANTS_KEY: {}, BODY_ERRORS_KEY: {}}
    if is_list_all_contestants:
        body = {BODY_CONTESTANTS_KEY: sorted(get_contestants())}
    elif is_list_contestants_without_team:
        contestants_without_team = sorted(get_contestants() - get_team_members())
        body = {BODY_CONTESTANTS_KEY: contestants_without_team or []}
    elif is_list_contestants_in_a_team:
        contestants_in_a_team = sorted(get_team_members())
        body = {BODY_CONTESTANTS_KEY: contestants_in_a_team or []}

    body_json = json.dumps(body)
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
