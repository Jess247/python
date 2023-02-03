import zombiedice


class MyZombie:
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

        zombies = (
            zombiedice.examples.RandomCoinFlipZombie(name='Random'),
            zombiedice.examples.RollsUntilInTheLeadZombie(
                name='Until leading'),
            zombiedice.examples.minNumShotgunsThenStopsZombie(
                name='Stop at 2 Shotguns', minShotguns=2),
            zombiedice.examples.minNumShotgunsThenStopsZombie(
                name='Stop at 1 Shotguns', minShotguns=1),
            MyZombie(name='My Zombie Bot')
        )

        # run in web-GUI-Mode
        zombiedice.runTournament(zombies=zombies, numGames=1000)
        zombiedice.runWebGui(zombies=zombies, numGames=1000)
