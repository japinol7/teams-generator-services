
class EventController:
    def __init__(self, event):
        self.event = event

    def get_is_list_all_teams_raw(self):
        return self.event['listAllTeams']

    def get_is_list_all_teams(self):
        res = self.get_is_list_all_teams_raw()
        if isinstance(res, str):
            if res.lower() == 'true':
                res = True
            elif res.lower() == 'false':
                res = False
        return res

    @staticmethod
    def validate_input_values(is_list_all_teams):
        res = True
        if not isinstance(is_list_all_teams, bool):
            res = False
        return res
