from modules.version import version

SERVICE_NAME = 'teams-generator-add-contestants'

N_MEMBERS_MAX = 100

BODY_CONTESTANTS_KEY = 'names'
BODY_CONTESTANTS_ADDED_KEY = 'added names'
BODY_ERRORS_KEY = 'errors'

INPUT_ERRORS_KEY = 'Input Errors'
INPUT_ERROR_TAG = 'Input Error'

ERROR_TAG = 'Error'
ERROR_INPUT_VALUES = "User Input Error. addContestants key has to be set to a boolean value!"
ERROR_MAX_MSG = f"User input Error. Maximum {N_MEMBERS_MAX} contestants to add."

LOG_START_SERVICE_MSG = f"Start service {SERVICE_NAME} version: {version.get_version()}"
LOG_END_SERVICE_MSG = f"End service {SERVICE_NAME}"
