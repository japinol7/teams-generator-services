from modules.version import version

SERVICE_NAME = 'teams-generator-add-contestants'

# You can add up to this number of contestants each execution
N_CONTESTANTS_MAX = 100
# The system will manage a total maximum of contestants
N_CONTESTANTS_MAX_TOTAL = 2100

EVENT_KEYS = ['addContestants']

BODY_CONTESTANTS_KEY = 'names'
BODY_CONTESTANTS_ADDED_KEY = 'added names'
BODY_ERRORS_KEY = 'errors'

INPUT_ERRORS_KEY = 'Input Errors'
INPUT_ERROR_TAG = 'Input Error'

ERROR_TAG = 'Error'
ERROR_INPUT_VALUES = (
    "User Input Error. Missing addContestants key or not set to a list of names."
)
ERROR_MAX_MSG = f"User input Error. Maximum {N_CONTESTANTS_MAX} contestants to add."

LOG_START_SERVICE_MSG = f"Start service {SERVICE_NAME} version: {version.get_version()}"
LOG_END_SERVICE_MSG = f"End service {SERVICE_NAME}"
