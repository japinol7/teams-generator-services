import json

from modules.config.config import (
    BODY_CONTESTANTS_KEY,
    BODY_CONTESTANTS_ADDED_KEY,
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
    contestants_to_add = controller.get_contestants_to_add()
    if not controller.validate_input_values(contestants_to_add):
        error_msg = log_validation.log_wrong_input_values(controller, contestants_to_add)
        log.info(LOG_END_SERVICE_MSG)
        error_msg_json = json.dumps(error_msg)
        return {
            'statusCode': 200,
            'body': error_msg_json,
        }

    res_file_names_contestants = config_parser['teams_gen_file_contestants']
    names = s3.get_contestants(res_file_names_contestants)
    names_len_before = len(names)
    names.extend(contestants_to_add)
    names = sorted(list(set(names)))

    if len(names) > names_len_before:
        body_to_upload = {BODY_CONTESTANTS_KEY: names}
        body_json_to_upload = json.dumps(body_to_upload)
        s3.upload_resource(resource_name=config_parser['teams_gen_file_contestants'], body=body_json_to_upload)
    else:
        log.info(f"Skip uploading names to bucket: No new names to add.")

    body = {BODY_CONTESTANTS_ADDED_KEY: contestants_to_add}
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
