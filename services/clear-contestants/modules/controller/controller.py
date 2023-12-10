from modules.config.config import EVENT_KEYS


def is_not_only_one_true(sequence):
    return len([x for x in sequence if x]) != 1


class EventController:
    def __init__(self, event):
        self.event = event
        self.keys = set()
        self.error_msg = ''

    def get_is_clear_all_contestants_raw(self):
        return self.event.get('clearAllContestants', 'false')

    def get_is_clear_all_contestants(self):
        res = self.get_is_clear_all_contestants_raw()
        if isinstance(res, str):
            if res.lower() == 'true':
                res = True
            elif res.lower() == 'false':
                res = False
        if res:
            self.keys.add('clearAllContestants')
        return res

    def get_is_clear_contestants_without_team_raw(self):
        return self.event.get('clearContestantsWithoutTeam', 'false')

    def get_is_clear_contestants_without_team(self):
        res = self.get_is_clear_contestants_without_team_raw()
        if isinstance(res, str):
            if res.lower() == 'true':
                res = True
            elif res.lower() == 'false':
                res = False
        if res:
            self.keys.add('clearContestantsWithoutTeam')
        return res

    def validate_input_values(self, is_clear_all_contestants, is_clear_contestants_without_team):
        res = True
        if 'clearAllContestants' in self.keys and not isinstance(is_clear_all_contestants, bool):
            res = False
        elif 'clearContestantsWithoutTeam' in self.keys and not isinstance(is_clear_contestants_without_team, bool):
            res = False
        elif is_not_only_one_true([is_clear_all_contestants, is_clear_contestants_without_team]):
            self.error_msg = (f"One and only one event key should be set to True. "
                              f"Available event keys: {EVENT_KEYS}")
            res = False
        return res
