'''
Jessica J. Hernandez
August 26, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Dynamic Site Assignment
'''

#DATA OBJECT CLASS
class Skylander(object):
    def __init__(self):
        self.name = ''
        self.description = ''' '''
        self.image = ''
        self.element = ''
        self.el_img = ''
        self.char_versions = []
        self.power_stats = []

#DATA CLASS
class Data(object):
    def __init__(self):
        eruptor = Skylander()
        eruptor.name = "Eruptor"
        eruptor.description = '''Eruptor is a force of nature, hailing from a species that lived deep in the underground of a floating volcanic island until a massive eruption launched their entire civilization to the surface. He's a complete hot head - steaming, fuming, and quite literally erupting over almost anything. To help control his temper, he likes to relax in lava pools, particularly because there are no crowds.'''
        eruptor.element = "Fire"
        eruptor.el_img = ''
        eruptor.char_versions = ['First Edition', 'Series 2', 'Series 3', 'Mini', 'Lightcore', 'Volcanic', 'Eggsellent']
        eruptor.power_stats = [80,85,25,35]