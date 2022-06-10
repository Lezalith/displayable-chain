init -15 python:

    # Represents a character inside a battle.
    # TODO: There will be an extensive GameCharacter class and this will be made to hold only Chains used inside the battle.
    # TODO: So this will probably store all the attacks, spells... And disregard everything not equipped or present?
    class BattleCharacter():

        # name is a string.
        # dictOfChains is a dictionary. Keys are keywords, values are AnimationChains. Valid keywords are:
        # - "enter" - Chain used for entering the battle.
        # - "hit" - Chain used for getting hit.
        # - "death" - Chain used for death/exiting the battle.
        # hp is the starting health of the Character.
        def __init__(self, name, dictOfChains, hp):

            # Name of the Character.
            self.name = name

            # Chains the Character uses.
            self.chains = dictOfChains

            # Stats
            self.hp = hp
            self.mp = 100.0
            self.ap = 100.0

            # BattleActions the Character can use.
            # None by default, all have to be added with learnAction().
            self.knownActions = []

            # Current AnimationChain used.
            # This is basically the Displayable representing this character.
            self.currentChain = None

        # Adds a BattleAction to knownActions so that it can be used. 
        def learnAction(self, action):

            # If the Action is already present. Currently has a notify, might be ignored later.
            if action in self.knownActions:
                return renpy.notify("{} already knows how to use {}.".format(self.name, action.name))

            self.knownActions.append(action)

        # Return a list of known Actions with the given type.
        # Types listed in battle_actions.rpy.
        def getKnownActions(self, type):

            return [action for action in self.knownActions if action.type == type]

        # Sets the currentChain to chain and begins it.
        def setChain(self, chain):

            self.currentChain = chain
            self.currentChain.beginChain()

        # Get the currentChain.
        def getChain(self):
            return self.currentChain

        # Trigger AnimationChain representing the entrance to the battle.
        def enter(self):

            self.setChain(self.chains["enter"])

        # Returns False if not enough AP, MP or HP to use, and True otherwise.
        # action is a BattleAction.
        # noticeManager is an injection for displaying a message.
        def checkCost(self, action, noticeManager):

            # TODO: Maybe actions with BOTH apCost and mpCost?

            # TODO: addNotice("Character is missing {} AP/MP to use {}!")

            # Action costs AP
            if action.apCost > 0:

                # If Character doesn't have enough AP to use the action:
                if self.ap < action.apCost:

                    noticeManager.addNotice("{} doesn't have enough AP to use {}!".format(self.name, action.name), color = "000")
                    return False

            # Action costs MP
            elif action.mpCost > 0:

                # If Character doesn't have enough MP to use the action:
                if self.mp < action.mpCost:

                    noticeManager.addNotice("{} doesn't have enough MP to use {}!".format(self.name, action.name), color = "000")
                    return False 

            # Action costs HP
            elif action.hpCost > 0:

                # If Character's would go below 0 upon using the action:
                if self.hp < action.hpCost:

                    noticeManager.addNotice("Casting {} would reduce {}'s HP below 0!".format(action.name, self.name), color = "000")
                    return False 

            # The Character has everything they need to use this Action.
            return True

        # Applies the AP, MP or HP cost and displays a message about using the action.
        # Should always be under an if of self.checkCost()
        # action is a BattleAction.
        # noticeManager is an injection for displaying a message.
        def applyCost(self, action, noticeManager):

            # TODO: Maybe actions with BOTH apCost and mpCost?

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

            # Action costs HP
            elif action.hpCost > 0:

                # Apply AP cost.
                self.hp -= action.hpCost

                # Message about sacrificing HP to use this Action.
                noticeManager.addNotice("{} sacrificed {} HP to use {}!".format(self.name, action.hpCost, action.name), color = "000")

            # Action doesn't cost either.
            else:

                # Message about using this action.
                noticeManager.addNotice("{} used {}!".format(self.name, action.name), color = "000")

        # Trigger AnimationChain representing an attack, after dealing with the Attack's cost.
        # attack is a BattleAction object of the attack used.
        # noticeManager is an injection for displaying a message.
        def attack(self, attack, noticeManager):

            self.applyCost(attack, noticeManager)

            # Chain to use is taken from the Attack object.
            self.setChain(attack.animationChain)

        # Trigger AnimationChain representing a Spell.
        # attack is a BattleAction object of the spell used.
        # noticeManager is an injection for displaying a message.
        def spellCast(self, spell, noticeManager):

            self.applyCost(spell, noticeManager)

            self.setChain(spell.getAssociatedChain())

        # Trigger AnimationChain representing getting hit.
        def hit(self, action, noticeManager, attackerName):

            # Calculate how much damage the action dealt.
            damageDealt = action.getDamage()

            # Apply the damage to HP.
            self.hp -= damageDealt

            # Message about hitting the enemy, and for how much damage.
            noticeManager.addNotice( "{} hit {} for {} damage!".format(attackerName, self.name, damageDealt), color = "000" )
                
            self.setChain(self.chains["hit"])

        # Trigger AnimationChain representing dying/leaving.
        def died(self):

            self.setChain(self.chains["death"])

        # How enemy acts during turns. Overwritten by EnemyCharacter subclass.
        def enemyTurnAI(self):
            pass 

# Characters defined.
default playerCharacter = BattleCharacter( "Player Character", {"enter" : allySpawnChain, "hit" : allyHitChain, "death" : allyDeathChain}, 100.0 )
# default enemyCharacter = BattleCharacter( "Enemy Character", {"enter" : enemySpawnChain, "hit" : enemyHitFancyChain, "death" : enemyDeathChain}, 46.0 )