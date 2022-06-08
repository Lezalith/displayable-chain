init -15 python:

    # Represents a character inside a battle.
    # TODO: There will be an extensive GameCharacter class and this will be made to hold only Chains used inside the battle.
    # TODO: So this will probably store all the attacks, spells... And disregard everything not equipped or present?
    class BattleCharacter():

        # name is a string.
        # enterChain is a AnimationChain.
        # hitChain is a AnimationChain.
        # deathChain is a AnimationChain.
        # hp is the starting health of the Character.
        def __init__(self, name, enterChain, hitChain, deathChain, hp):

            # Name of the Character.
            self.name = name

            # Chains used by the Character.
            self.enterChain = enterChain
            self.hitChain = hitChain
            self.deathChain = deathChain

            # Stats
            self.hp = hp
            self.mp = 100.0
            self.ap = 100.0

            # Current AnimationChain used.
            # This is basically the Displayable of this character.
            self.currentChain = None

        # Trigger AnimationChain representing the entrance to the battle.
        def enter(self):

            self.currentChain = self.enterChain
            self.currentChain.beginChain()

        # Trigger AnimationChain representing an attack, after dealing with the Attack's cost.
        # TODO: Um... Why, exactly, am I mixing dealing with cost when this is just... Supposed to start the chain? Actually, why don't I make a universal function for starting chains??
        # attack is an Attack object of the attack used.
        # noticeManager is an injection for displaying a message.
        def attack(self, attack, noticeManager):

            # If the attack has an AP cost:
            if attack.apCost:

                # If Character doesn't have enough AP to use the attack:
                if self.ap < attack.apCost:

                    return renpy.notify("Not enough AP!")

                # Apply AP cost.
                self.ap -= attack.apCost

                # Message about spending SP to use this Attack.
                noticeManager.addNotice("{} spent {} Ability Points to use {}!".format(self.name, attack.apCost, attack.name), color = "000")

            # Chain to use is taken from the Attack object.
            self.currentChain = attack.animationChain
            self.currentChain.beginChain()

        # Trigger AnimationChain representing a Spell.
        # attack is a Spell object of the spell used.
        # noticeManager is an injection for displaying a message.
        def spellCast(self, spell, noticeManager):

            # If the spell has a MP cost:
            if spell.mpCost:

                # If Character doesn't have enough AP to use the attack:
                if self.mp < spell.mpCost:

                    return renpy.notify("Not enough MP!")

                # Apply AP cost.
                self.mp -= spell.mpCost

                # Message about spending MP to cast this spell.
                noticeManager.addNotice("{} spent {} Mana to cast {}!".format(self.name, spell.mpCost, spell.name), color = "000")

            else:

                # Message about casting this Spell.
                noticeManager.addNotice("{} cast {}!".format(self.name, spell.name), color = "000")

            self.currentChain = spell.castAnimationChain
            self.currentChain.beginChain()

        # Trigger AnimationChain representing getting hit.
        def hit(self, attack, noticeManager, attackerName):

            # Calculate how much damage the attack dealt.
            damageDealt = attack.getDamage()

            # Apply the damage to HP.
            self.hp -= damageDealt

            # Message about hitting the enemy, and for how much damage.
            noticeManager.addNotice( "{} hit {} for {} damage!".format(attackerName, self.name, damageDealt), color = "000" )

            self.currentChain = self.hitChain
            self.currentChain.beginChain()

        # Trigger AnimationChain representing dying/leaving.
        def died(self):

            self.currentChain = self.deathChain
            self.currentChain.beginChain()

        # Get self.currentChain.
        def getChain(self):
            return self.currentChain

# Characters defined.
default allyCharacter = BattleCharacter( "Ally Character", allySpawnChain, allyHitChain, allyDeathChain, 100.0 )
default enemyCharacter = BattleCharacter( "Enemy Character", enemySpawnChain, enemyHitFancyChain, enemyDeathChain, 46.0 )