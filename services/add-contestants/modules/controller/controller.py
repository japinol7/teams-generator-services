from modules.config.config import N_CONTESTANTS_MAX


class EventController:
    def __init__(self, event):
        self.event = event
        self.keys = set()

    def get_contestants_to_add_raw(self):
        return self.event.get('addContestants', 'false')

    def get_contestants_to_add(self):
        res = self.get_contestants_to_add_raw()
        if isinstance(res, list):
            res = (x.strip() for x in res if len(x.strip()) > 0)
            res = sorted(list(set(res)))
        if res:
            self.keys.add('addContestants')
        return res

    @staticmethod
    def validate_input_values(contestants_to_add):
        res = True
        if not isinstance(contestants_to_add, list):
            res = False
        elif len(contestants_to_add) > N_CONTESTANTS_MAX:
            res = False
        return res
