class EventController:
    def __init__(self, event):
        self.event = event
        self.keys = set()

    def get_is_clear_all_teams_raw(self):
        return self.event.get('ResetTeamsGenerator', 'false')

    def get_is_reset_teams_generator(self):
        res = self.get_is_clear_all_teams_raw()
        if isinstance(res, str):
            if res.lower() == 'true':
                res = True
            elif res.lower() == 'false':
                res = False
        if res:
            self.keys.add('ResetTeamsGenerator')
        return res

    @staticmethod
    def validate_input_values(is_reset_teams_generator):
        res = True
        if not isinstance(is_reset_teams_generator, bool):
            res = False
        if not is_reset_teams_generator:
            res = False
        return res
