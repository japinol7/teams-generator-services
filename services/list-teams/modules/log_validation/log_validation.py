from modules.config.config import BODY_ERRORS_KEY, INPUT_ERROR_TAG, INPUT_ERRORS_KEY, ERROR_INPUT_VALUES
from modules.tools.logger.logger import logger as log


def log_wrong_input_values(controller):
    log.info(ERROR_INPUT_VALUES)
    return {BODY_ERRORS_KEY: {
                INPUT_ERRORS_KEY: [[INPUT_ERROR_TAG, ERROR_INPUT_VALUES]],
                }
            }
