init -15 python:

    # Represents a character inside a battle.
    # TODO: There will be an extensive GameCharacter class and this will be made to hold only Chains used inside the battle.
    # TODO: So this will probably store all the attacks, spells... And disregard everything not equipped or present? 
    #
    # Arguments:
    # name is the name of this character
    # enterChain is the chain used for entering the battle
    # attackChain is the chain used for attacking
    # hitChain is the chain used when getting hit
    class BattleCharacter():

        def __init__(self, name, enterChain, hitChain, deathChain, hp):

            # Name of the Character.
            self.name = name

            # Relevant Chains.
            self.enterChain = enterChain
            self.hitChain = hitChain
            self.deathChain = deathChain

            # Stats
            self.hp = hp
            self.mp = 100.0
            self.ap = 100.0

            self.spell = None

            # Current Chain used.
            # This is basically the Displayable of this character.
            self.currentChain = None

        # TODO: Will be changed to work with list
        def setSpell(self, spell):

            self.spell = spell

        # Trigger a chain representing the entrance to the battle.
        def enter(self):

            self.currentChain = self.enterChain
            self.currentChain.beginChain()

        # Trigger a chain representing attacking.
        def attack(self, attack, noticeManager):


            if attack.apCost:

                if self.ap < attack.apCost:

                    return renpy.notify("Not enough AP!")

                self.ap -= attack.apCost

                noticeManager.addNotice("{} spent {} Ability Points to use {}!".format(self.name, attack.apCost, attack.name), color = "000")

            self.currentChain = attack.animationChain
            self.currentChain.beginChain()

        def spellCast(self, spell, noticeManager):

            # Implement like in attack.
            # if attack.mpCost:

            noticeManager.addNotice("{} cast {}!".format(self.name, spell.name), color = "000")


            # TODO: currentChain will need to be a list, currentChains
            self.currentChain = spell.animationChain
            self.currentChain.beginChain()


        # Trigger a chain representing getting hit.
        def hit(self, attack, noticeManager, attackerName):

            damageDealt = attack.getDamage()

            self.hp -= damageDealt

            noticeManager.addNotice( "{} hit {} for {} damage!".format(attackerName, self.name, damageDealt), color = "000" )

            self.currentChain = self.hitChain
            self.currentChain.beginChain()

        def died(self):

            self.currentChain = self.deathChain
            self.currentChain.beginChain()

        # Get self.currentChain.
        def getChain(self):

            return self.currentChain

# Characters defined.
default allyCharacter = BattleCharacter( "Ally Character", allySpawnChain, allyHitChain, allyDeathChain, 100.0 )
default enemyCharacter = BattleCharacter( "Enemy Character", enemySpawnChain, enemyHitFancyChain, enemyDeathChain, 46.0 )