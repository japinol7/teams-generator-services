from modules.config.config import BODY_ERRORS_KEY, INPUT_ERROR_TAG, INPUT_ERRORS_KEY, ERROR_INPUT_VALUES
from modules.tools.logger.logger import logger as log


def log_wrong_input_values(controller):
    if 'clearAllContestants' in controller.keys and 'clearContestantsWithoutTeam' in controller.keys:
        error_msg = f"{ERROR_INPUT_VALUES} Asked for both clearAllContestants and clearContestantsWithoutTeam options. " \
                    f"Choose only one."
    else:
        error_msg = f"{ERROR_INPUT_VALUES} clearAllContestants and clearContestantsWithoutTeam keys have to be set " \
                    f"to a boolean value!."

    log.info(error_msg)
    return {BODY_ERRORS_KEY: {
                INPUT_ERRORS_KEY: [[INPUT_ERROR_TAG, error_msg]],
                }
            }
