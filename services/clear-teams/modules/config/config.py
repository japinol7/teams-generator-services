from modules.version import version

SERVICE_NAME = 'teams-generator-clear-teams'

EVENT_KEYS = ['clearAllTeams']

BODY_TEAMS_KEY = 'teams'
BODY_ERRORS_KEY = 'errors'

INPUT_ERRORS_KEY = 'Input Errors'
INPUT_ERROR_TAG = 'Input Error'

ERROR_TAG = 'Error'
ERROR_INPUT_VALUES = (
    "User Input Error. A clearAllTeams key has to be set to the boolean value: true!"
)

LOG_START_SERVICE_MSG = f"Start service {SERVICE_NAME} version: {version.get_version()}"
LOG_END_SERVICE_MSG = f"End service {SERVICE_NAME}"
