import json

from modules.config.config import (
    BODY_CONTESTANTS_KEY,
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


def lambda_handler(event, context):
    log.info(LOG_START_SERVICE_MSG)
    controller = EventController(event)
    is_clear_all_contestants = controller.get_is_clear_all_contestants()
    is_clear_contestants_without_team = (
        controller.get_is_clear_contestants_without_team()
    )
    log.info(f"Input options: {controller.keys}")

    if not controller.validate_input_values(
        is_clear_all_contestants, is_clear_contestants_without_team
    ):
        error_msg = log_validation.log_wrong_input_values(controller)
        log.info(LOG_END_SERVICE_MSG)
        error_msg_json = json.dumps(error_msg)
        return {
            'statusCode': 200,
            'body': error_msg_json,
        }

    res_file_contestants = config_parser['teams_gen_file_contestants']

    if is_clear_contestants_without_team:
        names = set(s3.get_contestants(res_file_contestants))
        res_file_teams = config_parser['teams_gen_file_teams']
        teams, _ = s3.get_teams(res_file_teams)
        names_in_teams = {name for sublist in teams.values() for name in sublist}
        names_body = sorted(list(names & names_in_teams))
        body = {BODY_CONTESTANTS_KEY: names_body}
    else:
        body = {BODY_CONTESTANTS_KEY: []}

    body_json = json.dumps(body)
    s3.upload_contestants(res_file_contestants, body=body_json)
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
