
class EventController:
    def __init__(self, event):
        self.event = event
        self.keys = set()

    def get_is_clear_all_contestants_raw(self):
        return self.event.get('clearAllContestants')

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
        return self.event.get('clearContestantsWithoutTeam')

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
        elif is_clear_all_contestants and is_clear_contestants_without_team:
            res = False
        elif not is_clear_all_contestants and not is_clear_contestants_without_team:
            res = False
        return res
