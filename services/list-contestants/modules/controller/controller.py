from modules.config.config import EVENT_KEYS


def is_not_only_one_true(sequence):
    return len([x for x in sequence if x]) != 1


class EventController:
    def __init__(self, event):
        self.event = event
        self.keys = set()
        self.error_msg = ''

    def get_is_list_all_contestants_raw(self):
        return self.event.get('listAllContestants', 'false')

    def get_is_list_all_contestants(self):
        res = self.get_is_list_all_contestants_raw()
        if isinstance(res, str):
            if res.lower() == 'true':
                res = True
            elif res.lower() == 'false':
                res = False
        if res:
            self.keys.add('listAllContestants')
        return res

    def get_is_list_contestants_without_team_raw(self):
        return self.event.get('listContestantsWithoutTeam', 'false')

    def get_is_list_contestants_without_team(self):
        res = self.get_is_list_contestants_without_team_raw()
        if isinstance(res, str):
            if res.lower() == 'true':
                res = True
            elif res.lower() == 'false':
                res = False
        if res:
            self.keys.add('listContestantsWithoutTeam')
        return res

    def get_is_list_contestants_in_a_team_raw(self):
        return self.event.get('listContestantsInATeam', 'false')

    def get_is_list_contestants_in_a_team(self):
        res = self.get_is_list_contestants_in_a_team_raw()
        if isinstance(res, str):
            if res.lower() == 'true':
                res = True
            elif res.lower() == 'false':
                res = False
        if res:
            self.keys.add('listContestantsInATeam')
        return res

    def validate_input_values(self, is_list_all_contestants, is_list_contestants_without_team,
                              is_list_contestants_in_a_team):
        res = True
        if 'listAllContestants' in self.keys and not isinstance(is_list_all_contestants, bool):
            res = False
        elif ('listContestantsWithoutTeam' in self.keys
              and not isinstance(is_list_contestants_without_team, bool)):
            res = False
        elif ('listContestantsInATeam' in self.keys
              and not isinstance(is_list_contestants_in_a_team, bool)):
            res = False
        elif is_not_only_one_true([is_list_all_contestants,
                                  is_list_contestants_without_team,
                                  is_list_contestants_in_a_team]):
            self.error_msg = (f"One and only one event key should be set to True. "
                              f"Available event keys: {EVENT_KEYS}")
            res = False
        return res
