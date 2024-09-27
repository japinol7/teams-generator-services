from modules.config.config import (
    BODY_ERRORS_KEY,
    INPUT_ERROR_TAG,
    INPUT_ERRORS_KEY,
    ERROR_INPUT_VALUES,
)
from modules.config.config import N_CONTESTANTS_MAX, ERROR_MAX_MSG
from modules.tools.logger.logger import logger as log


def log_wrong_input_values(controller, contestants_to_add):
    if len(contestants_to_add) > N_CONTESTANTS_MAX:
        error_msg = ERROR_MAX_MSG
    else:
        error_msg = ERROR_INPUT_VALUES
    log.info(error_msg)
    return {
        BODY_ERRORS_KEY: {
            INPUT_ERRORS_KEY: [[INPUT_ERROR_TAG, error_msg]],
        }
    }
