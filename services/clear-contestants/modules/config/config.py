from modules.version import version

SERVICE_NAME = 'teams-generator-clear-contestants'

BODY_CONTESTANTS_KEY = 'names'
BODY_TEAMS_KEY = 'teams'
BODY_ERRORS_KEY = 'errors'

INPUT_ERRORS_KEY = 'Input Errors'
INPUT_ERROR_TAG = 'Input Error'

ERROR_TAG = 'Error'
ERROR_INPUT_VALUES = "User Input Error."

LOG_START_SERVICE_MSG = f"Start service {SERVICE_NAME} version: {version.get_version()}"
LOG_END_SERVICE_MSG = f"End service {SERVICE_NAME}"
