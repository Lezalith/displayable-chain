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


        def setChain(self, chain):

            self.currentChain = chain
            self.currentChain.beginChain()

        # Trigger AnimationChain representing the entrance to the battle.
        def enter(self):

            self.setChain(self.enterChain)

        # Returns False if not enough AP or MP to use, and True otherwise.
        # action is a BattleAction.
        # noticeManager is an injection for displaying a message.
        def checkCost(self, action, noticeManager):

            # TODO: hpCost could be easily made!
            # TODO: So could be actions with BOTH apCost and mpCost.

            # Action costs AP
            if action.apCost > 0:

                # If Character doesn't have enough AP to use the attack:
                if self.ap < action.apCost:

                    noticeManager.addNotice("{} doesn't have enough AP to use {}!".format(self.name, action.name), color = "000")
                    return False

            # Action costs MP
            elif action.mpCost > 0:

                # If Character doesn't have enough MP to use the attack:
                if self.mp < action.mpCost:

                    noticeManager.addNotice("{} doesn't have enough MP to use {}!".format(self.name, action.name), color = "000")
                    return False 

            return True

        # Applies the AP or MP cost and displays a message about using the action.
        # Should always be under an if of self.checkCost()
        # action is a BattleAction.
        # noticeManager is an injection for displaying a message.
        def applyCost(self, action, noticeManager):

            # TODO: hpCost could be easily made!
            # TODO: So could be actions with BOTH apCost and mpCost.

            # Action costs AP
            if action.apCost > 0:

                # Apply AP cost.
                self.ap -= action.apCost

                # Message about spending MP to use this Action.
                noticeManager.addNotice("{} spent {} AP to use {}!".format(self.name, action.apCost, action.name), color = "000")

            # Action costs MP
            elif action.mpCost > 0:

                # Apply AP cost.
                self.mp -= action.mpCost

                # Message about spending MP to use this Action.
                noticeManager.addNotice("{} spent {} Mana to use {}!".format(self.name, action.mpCost, action.name), color = "000")

            # Action doesn't cost either.
            else:

                # Message about using this action.
                noticeManager.addNotice("{} used {}!".format(self.name, action.name), color = "000")

            return True

        # Trigger AnimationChain representing an attack, after dealing with the Attack's cost.
        # TODO: FIX ATTACK/SPELL IN ARGUMENTS
        # attack is an Attack object of the attack used.
        # noticeManager is an injection for displaying a message.
        def attack(self, attack, noticeManager):

            self.applyCost(attack, noticeManager)

            # Chain to use is taken from the Attack object.
            self.setChain(attack.animationChain)

        # Trigger AnimationChain representing a Spell.
        # attack is a Spell object of the spell used.
        # noticeManager is an injection for displaying a message.
        def spellCast(self, spell, noticeManager):

            self.applyCost(spell, noticeManager)

            self.setChain(spell.getAssociatedChain())

        # Trigger AnimationChain representing getting hit.
        def hit(self, attack, noticeManager, attackerName):

            # Calculate how much damage the attack dealt.
            damageDealt = attack.getDamage()

            # Apply the damage to HP.
            self.hp -= damageDealt

            # Message about hitting the enemy, and for how much damage.
            noticeManager.addNotice( "{} hit {} for {} damage!".format(attackerName, self.name, damageDealt), color = "000" )
                
            self.setChain(self.hitChain)

        # Trigger AnimationChain representing dying/leaving.
        def died(self):

            self.setChain(self.deathChain)

        # Get self.currentChain.
        def getChain(self):
            return self.currentChain

# Characters defined.
default allyCharacter = BattleCharacter( "Ally Character", allySpawnChain, allyHitChain, allyDeathChain, 100.0 )
default enemyCharacter = BattleCharacter( "Enemy Character", enemySpawnChain, enemyHitFancyChain, enemyDeathChain, 46.0 )