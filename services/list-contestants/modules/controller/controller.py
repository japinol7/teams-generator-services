
class EventController:
    def __init__(self, event):
        self.event = event

    def get_is_list_all_contestants_raw(self):
        return self.event['listAllContestants']

    def get_is_list_all_contestants(self):
        res = self.get_is_list_all_contestants_raw()
        if isinstance(res, str):
            if res.lower() == 'true':
                res = True
            elif res.lower() == 'false':
                res = False
        return res

    @staticmethod
    def validate_input_values(is_list_all_contestants):
        res = True
        if not isinstance(is_list_all_contestants, bool):
            res = False
        return res
