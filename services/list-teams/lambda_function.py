import json

from modules.config.config import (
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


def lambda_handler(event, context):
    log.info(LOG_START_SERVICE_MSG)

    config_parser = ConfigParser()
    s3 = S3Client()

    controller = EventController(event)
    is_list_all_teams = controller.get_is_list_all_teams()
    if not controller.validate_input_values(is_list_all_teams):
        error_msg = log_validation.log_wrong_input_values(controller)
        log.info(LOG_END_SERVICE_MSG)
        error_msg_json = json.dumps(error_msg)
        return {
            'statusCode': 200,
            'body': error_msg_json,
        }

    res_file_teams = config_parser['teams_gen_file_teams']
    teams, errors = s3.get_teams(res_file_teams)
    body = {BODY_TEAMS_KEY: teams, BODY_ERRORS_KEY: errors}
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
