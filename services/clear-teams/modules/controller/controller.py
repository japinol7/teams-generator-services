
class EventController:
    def __init__(self, event):
        self.event = event
        self.keys = set()

    def get_is_clear_all_teams_raw(self):
        return self.event.get('clearAllTeams', 'false')

    def get_is_clear_all_teams(self):
        res = self.get_is_clear_all_teams_raw()
        if isinstance(res, str):
            if res.lower() == 'true':
                res = True
            elif res.lower() == 'false':
                res = False
        if res:
            self.keys.add('clearAllTeams')
        return res

    @staticmethod
    def validate_input_values(is_clear_all_teams):
        res = True
        if not isinstance(is_clear_all_teams, bool):
            res = False
        if not is_clear_all_teams:
            res = False
        return res
