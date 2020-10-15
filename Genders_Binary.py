from random import randint as ran
from requests import post


class Human:
    def __init__(self, gender, age, height, haircolor, hairlength, eyecolor):
        self.options = {
            'hair_colors': ('blonde', 'brown', 'black', 'red', 'grey'),
            'eye_colors': ('blue', 'green', 'brown', 'grey'),
            'hair_lengths': {
                'female': ['long', 'middle', 'short'],
                'male': ['long', 'middle', 'short', 'bald']
            }
        }
        self.age = age
        self.height = height
        self.haircolor = self.select(self.options['hair_colors'], haircolor)
        self.hair = self.select(self.options['hair_lengths'][gender], hairlength)
        self.eyecolor = self.select(self.options['eye_colors'], eyecolor)
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

    def asses_worth(self):
        obj = self.__dict__
        if hasattr(self, 'options'): obj.pop('options')
        res = post('https://kamelrechner.eu/en/result', data=obj)
        self.worth = int(str(res.content).split('<span class="result">')[1].split('<')[0])


class Girl(Human):
    def __init__(self, age, height, haircolor, hairlength, eyecolor, boobsize, figure=ran, gender='female'):
        super().__init__(gender, age, height, haircolor, hairlength, eyecolor)
        self.options = {
            'boob_sizes': ('a', 'b', 'c', 'd'),
            'figures': ('thin', 'sporty', 'normal', 'chubby', 'fat')
        }
        self.gender = gender
        self.boobsize = super().select(self.options['boob_sizes'], boobsize)
        self.figure = super().select(self.options['figures'], figure)
        super().asses_worth()


class Boy(Human):
    def __init__(self, age, height, haircolor, hairlength, eyecolor, beard, body, gender='male'):
        super().__init__(gender, age, height, haircolor, hairlength, eyecolor)
        self.options = {
            'beards': ('none', 'small', 'middle', 'large'),
            'bodies': ('muscle', 'normal', 'chubby')
        }
        self.gender = gender
        self.beard = super().select(self.options['beards'], beard)
        self.body = super().select(self.options['bodies'], body)
        super().asses_worth()
