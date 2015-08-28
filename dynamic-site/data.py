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
        eruptor.image = 'eruptor.png'
        eruptor.element = "Fire"
        eruptor.el_img = 'fire.png'
        eruptor.char_versions = ['First Edition', 'Series 2', 'Series 3', 'Mini', 'Lightcore', 'Volcanic', 'Eggsellent']
        eruptor.power_stats = [80,85,25,35]
        
        gill = Skylander()
        gill.name = "Gill Grunt"
        gill.description = '''Gill Grunt was a brave soul who joined the Gillmen military in search of adventure. While journeying through a misty lagoon in the clouds, he met an enchanting mermaid. He vowed to return to her after his tour. Keeping his promise, he came back to the lagoon years later, only to learn a nasty band of pirates had kidnapped the mermaid. Heartbroken, Gill Grunt began searching all over Skylands. Though he had yet to find her, he joined the Skylanders to help protect others from such evil, while still keeping an ever-watchful eye for the beautiful mermaid and the pirates who took her.'''
        gill.image = 'gill_grunt.png'
        gill.element = "Water"
        gill.el_img = 'water.png'
        gill.char_versions = ['First Edition', 'Series 2', 'Series 3', 'Series 4', 'Mini']
        gill.power_stats = [70,60,40,50]
        
        terra = Skylander()
        terra.name = "Terrafin"
        terra.description = '''Terrafin hails from The Dirt Seas,where it was common to swim, bathe, and even snorkel beneath the ground. But a powerful explosion in the sky created a blast wave that turned the ocean of sand into a vast sheet of glass, putting an end to Terrafin's duty as the local lifeguard. Not one to stay idle, the brawny dirt shark found himself training in the art of boxing, and not long after he was local champ. Fighters came from all around to challenge him, but it was a chance meeting with a great Portal Master that led him to give up his title for a greater purpose.'''
        terra.image = 'terrafin.png'
        terra.element = "Earth"
        terra.el_img = 'earth.png'
        terra.char_versions = ['First Edition', 'Series 2', 'Series 3', 'Mini']
        terra.power_stats = [70,80,25,50]
        
        elf = Skylander()
        elf.name = "Stealth Elf"
        elf.description = '''As a small child, Stealth Elf awoke one morning inside the hollow of an old tree with no memory of how she got there. She was taken in by an unusually stealthy, ninja-like forest creature in the deep forest. Under his tutelage, she has spent the majority of her life training in the art of stealth fighting. After completing her training, she became a Skylander and set out into the world to uncover the mystery behind her origins.'''
        elf.image = 'stealth_elf.png'
        elf.element = "Life"
        elf.el_img = 'life.png'
        elf.char_versions = ['First Edition', 'Series 2', 'Series 3', 'Mini', 'Dark', 'Legendary']
        elf.power_stats = [60,30,100,70]
        
        warnado = Skylander()
        warnado.name = "Warnado"
        warnado.description = '''Warnado was hatched in the fury of a rare and powerful Enchanted Twister. Although initially frightened and quite dizzy, over the passing years he grew to enjoy his whirling surroundings and learned many abilities and secrets of the Air Element. This led to Warnado becoming a powerful force and the only known turtle of his kind. Now, the only time he gets dizzy is when standing still.'''
        warnado.image = 'warnado.png'
        warnado.element = "Air"
        warnado.el_img = 'air.png'
        warnado.char_versions = ['First Edition', 'Lightcore']
        warnado.power_stats = [50,90,70,45]
        
        trigger = Skylander()
        trigger.name = "Trigger Happy"
        trigger.description = '''Trigger Happy is more than his name - it's his solution to every problem. Nobody knows from where he came. He just showed up one day in a small village, saving it from a group of terrorizing bandits by blasting gold coins everywhere with his custom-crafted shooters. Similar tales were soon heard from other villages, and his legend quickly grew. Now everyone in all of Skylands knows of the crazy goldslinger that will take down any bad guy... usually without bothering to aim.'''
        trigger.image = 'trigger_happy.png'
        trigger.element = "Tech"
        trigger.el_img = 'tech.png'
        trigger.char_versions = ['First Edition', 'Series 2', 'Series 3', 'Mini', 'Legendary', 'Springtime']
        trigger.power_stats = [40,20,60,100]
        
        spyro = Skylander()
        spyro.name = "Spyro"
        spyro.description = '''Spyro hails from a rare line of magical purple dragons who can harness the power of the Elements of Skylands, though he prefers to master fire.  But his innate ability with Elemental powers also leaves him vulnerable to darker magic.  When The Darkness is nearby, Spyro can channel its energy and combine its power with his own, becoming Dark Spyro!  Over the years, he has learned to focus and control this power, using dark magic to fight the forces of evil.'''
        spyro.image = 'spyro.png'
        spyro.element = "Magic"
        spyro.el_img = 'magic.png'
        spyro.char_versions = ['First Edition', 'Series 2', 'Series 3', 'Mini', 'Dark', 'Dark Edition', 'Legendary']
        spyro.power_stats = [60,50,90,60]
        
        sl_hex = Skylander()
        sl_hex.name = "Hex"
        sl_hex.description = '''Long ago, Hex was a gifted and powerful sorceress who traveled deep into the underworld to confront the Undead Dragon King named Malefor, who made several attempts to capture her to learn her secrets. Though she successfully battled the dragon, Hex returned from the underworld changed - having unwillingly joined the ranks of the Undead. Many are wary of her since her transformation, suspecting she has used her powerful magic for evil purposes. But Eon trusts her, and views her as a most valuable Skylander ally.'''
        sl_hex.image = 'hex.png'
        sl_hex.element = "Undead"
        sl_hex.el_img = 'undead.png'
        sl_hex.char_versions = ['First Edition', 'Series 2', 'Mini', 'Lightcore']
        sl_hex.power_stats = [70,70,40,50]
        
        self.skylanders = [eruptor, gill, terra, elf, warnado, trigger, spyro, sl_hex]