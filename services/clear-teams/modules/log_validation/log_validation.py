from modules.config.config import BODY_ERRORS_KEY, INPUT_ERROR_TAG, INPUT_ERRORS_KEY, ERROR_INPUT_VALUES
from modules.tools.logger.logger import logger as log


def log_wrong_input_values(controller):
    error_msg = ERROR_INPUT_VALUES + f" Asked for clearAllTeams: {controller.get_is_clear_all_teams()}."
    log.info(error_msg)
    return {BODY_ERRORS_KEY: {
                INPUT_ERRORS_KEY: [[INPUT_ERROR_TAG, error_msg]],
                }
            }
