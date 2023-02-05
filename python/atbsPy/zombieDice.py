import zombiedice
import random


class MyZombieTwoBrains:
    def __init__(self, name):
        # give zombies a name
        self.name = name

    def turn(self, gameState):
        ''' param: gameState: is a dic with information about the current gamestate
            roll returns a dic with brain, shotgun and footsteps as keys and the 
            amount of rolls as value
            rolls is a list of (color,symbol)-tuples with information about the dice result
        '''
        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class MyZombieRandom:
    def __init__(self, name):
        # give zombies a name
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        while diceRollResults is not None and random.randint(0, 1) == 0:
            diceRollResults = zombiedice.roll()


class MyZombieTwoShotguns:
    def __init__(self, name):
        # give zombies a name
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class MyZombieRandomShotgun:
    def __init__(self, name):
        # give zombies a name
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        shotguns = 0
        rollCounter = 0
        rolls = random.randint(1, 4)
        while diceRollResults is not None:
            rollCounter += 1
            shotguns += diceRollResults['shotgun']
            if shotguns < 2 and rollCounter < rolls:
                diceRollResults = zombiedice.roll()
            else:
                break


class MyZombieMoreShotgun:
    def __init__(self, name):
        # give zombies a name
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        brains = 0
        shotgun = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']
            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


zombies = (
    MyZombieTwoBrains(name='Two brains'),
    MyZombieRandom(name='Random'),
    MyZombieTwoShotguns(name='Two shotguns'),
    MyZombieRandomShotgun(name='Random Rolls shotgun'),
    MyZombieMoreShotgun(name='More Shotgun than brain')
)

# run in web-GUI-Mode
zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
