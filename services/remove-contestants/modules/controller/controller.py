from modules.config.config import N_CONTESTANTS_REMOVE_MAX


class EventController:
    def __init__(self, event):
        self.event = event
        self.keys = set()

    def get_contestants_to_remove_raw(self):
        return self.event.get('removeContestants', 'false')

    def get_contestants_to_remove(self):
        res = self.get_contestants_to_remove_raw()
        if isinstance(res, list):
            res = (x.strip() for x in res if len(x.strip()) > 0)
            res = set(res)
        if res:
            self.keys.add('removeContestants')
        return res

    @staticmethod
    def validate_input_values(contestants_to_remove):
        res = True
        if not isinstance(contestants_to_remove, set):
            res = False
        elif len(contestants_to_remove) > N_CONTESTANTS_REMOVE_MAX:
            res = False
        return res
