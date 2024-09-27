from modules.version import version

SERVICE_NAME = 'teams-generator-remove-contestants'

N_CONTESTANTS_REMOVE_MAX = 25

EVENT_KEYS = ['clearAllTeams']

BODY_CONTESTANTS_KEY = 'names'
BODY_CONTESTANTS_REMOVED_KEY = 'removed names'
BODY_TEAMS_KEY = 'teams'
BODY_ERRORS_KEY = 'errors'

INPUT_ERRORS_KEY = 'Input Errors'
INPUT_ERROR_TAG = 'Input Error'

ERROR_TAG = 'Error'
ERROR_INPUT_VALUES = (
    "User Input Error. A clearAllTeams key has to be set to the boolean value: true!"
)
ERROR_MAX_MSG = (
    f"User input Error. Maximum {N_CONTESTANTS_REMOVE_MAX} contestants to remove."
)

LOG_START_SERVICE_MSG = f"Start service {SERVICE_NAME} version: {version.get_version()}"
LOG_END_SERVICE_MSG = f"End service {SERVICE_NAME}"
