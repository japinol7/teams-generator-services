from modules.version import version

SERVICE_NAME = 'teams-generator-list-contestants'

EVENT_KEYS = [
    'listAllContestants',
    'listContestantsWithoutTeam',
    'listContestantsInATeam',
]

BODY_CONTESTANTS_KEY = 'names'
BODY_ERRORS_KEY = 'errors'

INPUT_ERRORS_KEY = 'Input Errors'
INPUT_ERROR_TAG = 'Input Error'

ERROR_TAG = 'Error'

LOG_START_SERVICE_MSG = f"Start service {SERVICE_NAME} version: {version.get_version()}"
LOG_END_SERVICE_MSG = f"End service {SERVICE_NAME}"
