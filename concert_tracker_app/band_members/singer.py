from concert_tracker_app.band_members.musician import Musician


class Singer(Musician):

    SKILLS = ['sing high pitch notes', 'sing low pitch notes']

    def learn_new_skill(self, new_skill):

        if new_skill not in Singer.SKILLS:
            raise ValueError(f'{new_skill} is not a needed skill!')

        if new_skill in self.skills:
            raise Exception(f'{new_skill} is already learned!')

        self.skills.append(new_skill)
        return f'{self.name} learned to {new_skill}.'
