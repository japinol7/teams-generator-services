from modules.config.config import N_MEMBERS_MAX


class EventController:
    def __init__(self, event):
        self.event = event

    def get_contestants_to_add_raw(self):
        return self.event['addContestants']

    def get_contestants_to_add(self):
        res = self.get_contestants_to_add_raw()
        if isinstance(res, list):
            res = (x.strip() for x in res if len(x.strip()) > 0)
            res = sorted(list(set(res)))
        return res

    @staticmethod
    def validate_input_values(contestants_to_add):
        res = True
        if not isinstance(contestants_to_add, list):
            res = False
        elif len(contestants_to_add) > N_MEMBERS_MAX:
            res = False
        return res
