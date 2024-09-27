from modules.config.config import BODY_ERRORS_KEY, INPUT_ERROR_TAG, INPUT_ERRORS_KEY
from modules.tools.logger.logger import logger as log


def log_wrong_input_values(controller):
    if controller.error_msg:
        error_msg = f"{controller.error_msg}"
    else:
        error_msg = (
            "listAllContestants, listContestantsWithoutTeam and listContestantsInATeam "
            "keys have to be set to a boolean value!"
        )

    log.info(error_msg)
    return {
        BODY_ERRORS_KEY: {
            INPUT_ERRORS_KEY: [[INPUT_ERROR_TAG, error_msg]],
        }
    }
