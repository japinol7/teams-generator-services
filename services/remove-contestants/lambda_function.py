import json

from modules.config.config import (
    BODY_CONTESTANTS_KEY,
    BODY_CONTESTANTS_REMOVED_KEY,
    BODY_TEAMS_KEY,
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


def remove_contestants(contestants_to_remove):
    res_file_names_contestants = config_parser['teams_gen_file_contestants']
    names = set(s3.get_contestants(res_file_names_contestants))
    names_len_before = len(names)
    names = sorted(names - contestants_to_remove)

    if len(names) < names_len_before:
        body_to_upload = {BODY_CONTESTANTS_KEY: names}
        body_json_to_upload = json.dumps(body_to_upload)
        s3.upload_resource(resource_name=config_parser['teams_gen_file_contestants'],
                           body=body_json_to_upload)
    else:
        log.info(f"Skip uploading contestants to bucket: No contestants to remove.")


def remove_team_members(contestants_to_remove):
    res_file_teams = config_parser['teams_gen_file_teams']
    teams, error = s3.get_teams(res_file_teams)
    contestants_in_a_team = {member for sublist in teams.values() for member in sublist}

    teams_after_remove = {}
    for k, v in teams.items():
        teams_after_remove[k] = [name for name in v if name not in contestants_to_remove]
    contestants_in_a_team_after = {member for sublist in teams_after_remove.values() for member in sublist}

    if len(contestants_in_a_team_after) < len(contestants_in_a_team):
        body_to_upload = {BODY_TEAMS_KEY: teams_after_remove, BODY_ERRORS_KEY: error}
        body_to_upload = json.dumps(body_to_upload)
        s3.upload_resource(resource_name=config_parser['teams_gen_file_teams'],
                           body=body_to_upload)
    else:
        log.info(f"Skip uploading teams to bucket: No teams with contestants to remove.")


def lambda_handler(event, context):
    log.info(LOG_START_SERVICE_MSG)
    controller = EventController(event)
    contestants_to_remove = controller.get_contestants_to_remove()
    log.info(f"Input options: {controller.keys}")

    if not controller.validate_input_values(contestants_to_remove):
        error_msg = log_validation.log_wrong_input_values(controller)
        log.info(LOG_END_SERVICE_MSG)
        error_msg_json = json.dumps(error_msg)
        return {
            'statusCode': 200,
            'body': error_msg_json,
        }

    remove_contestants(contestants_to_remove)
    remove_team_members(contestants_to_remove)

    body = {BODY_CONTESTANTS_REMOVED_KEY: list(contestants_to_remove)}
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
