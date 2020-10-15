from random import randint as ran


class Human:
    def __init__(self, gender, age=ran(14, 70), height=ran(140, 220), hair_color=ran(0, 4),
                 hair_length=ran(0, 2), eye_color=ran(0, 3)):
        self.options = {
            'hair_color': ('blonde', 'brown', 'black', 'red', 'grey'),
            'eye_colors': ('blue', 'green', 'brown', 'grey'),
            'hair_lengths': {
                'female': ['long', 'middle', 'short'],
                'male': ['long', 'middle', 'short', 'bald']
            }
        }
        self.age = age
        self.height = height
        self.hair_color = self.select(self.options['hair_color'], hair_color)
        self.hair_length = self.select(self.options['hair_lengths'][gender], hair_length)
        self.eye_color = self.select(self.options['eye_colors'], eye_color)
        self.gender = gender

    @staticmethod
    def select(choices, selection):
        max_index = len(choices) - 1
        if isinstance(selection, int) and 0 <= selection <= max_index:
            return choices[selection]
        elif isinstance(selection, str) and selection in choices:
            return choices
        else:
            return choices[ran(0, max_index)]

    def values(self):
        obj = self.__dict__
        obj.pop('options')
        return obj


class Girl(Human):
    def __init__(self, gender='female', boob_size=ran(0, 3), figure=ran(0, 4)):
        super().__init__(gender)
        self.options = {
            'boob_sizes': ('a', 'b', 'c', 'd'),
            'figures': ('thin', 'sporty', 'normal', 'chubby', 'fat')
        }
        self.gender = gender
        self.boob_size = super().select(self.options['boob_sizes'], boob_size)
        self.figure = super().select(self.options['figures'], figure)


class Boy(Human):
    def __init__(self, gender='male', beard=ran(0, 3), body=ran(0, 2)):
        super().__init__(gender)
        self.options = {
            'beards': ('none', 'small', 'middle', 'large'),
            'bodies': ('muscle', 'normal', 'chubby')
        }
        self.gender = gender
        self.beard = super().select(self.options['beards'], beard)
        self.body = super().select(self.options['bodies'], body)


girl = Girl()
print(girl.values())
