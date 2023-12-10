import json

from modules.config.config import (
    BODY_TEAMS_KEY,
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
    is_clear_all_teams = controller.get_is_clear_all_teams()
    log.info(f"Input options: {controller.keys}")

    if not controller.validate_input_values(is_clear_all_teams):
        error_msg = log_validation.log_wrong_input_values(controller)
        log.info(LOG_END_SERVICE_MSG)
        error_msg_json = json.dumps(error_msg)
        s3.upload_teams(resource_name=config_parser['teams_gen_file_teams'], body=error_msg_json)
        return {
            'statusCode': 200,
            'body': error_msg_json,
        }

    res_file_teams = config_parser['teams_gen_file_teams']
    body = {BODY_TEAMS_KEY: {}}
    body_json = json.dumps(body)
    s3.upload_teams(res_file_teams, body=body_json)
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
