init -30 python:

    # Ren'Py actually has an Animation displayable, which this overrides,
    # but I really don't think we will miss the original.
    #
    # Animation holds information about one state the Character be in.
    # image is the image of the state
    # transform is the transform of the state
    # duration is for how long the state sticks around - it has to be calculated manually, and is ignored ignored for idle state 
    class Animation():

        def __init__(self, image, transform, duration, triggers = False, triggersDelay = 0.0):

            self.image = image
            self.transform = transform
            self.duration = duration

            # Whether it triggers an animation.
            self.triggers = triggers
            # Delay before the animations this one triggers start.
            self.triggersDelay = triggersDelay

        def getChild(self):

            return At( self.image, self.transform )


init -25 python:

    enter = Animation("enterState", enterTrans, 1.0)
    enter2 = Animation("enterState", enterTrans, 1.0)
    idle = Animation("idleState", idleTrans, 0)
    moveForward = Animation("moveState", moveForwardTrans, 1.0)
    attack = Animation("attackState", attackTrans, 0.6, triggers = True, triggersDelay = 0.3)
    moveBack = Animation("moveState", moveBackTrans, 1.0)
    hit = Animation("hitState", hitTrans, 0.6)


    enterEnemy = Animation("enterStateEnemy", enterTransEnemy, 1.0)
    idleEnemy = Animation("idleStateEnemy", idleTransEnemy, 0)
    moveForwardEnemy = Animation("moveStateEnemy", moveForwardTransEnemy, 1.0)
    attackEnemy = Animation("attackStateEnemy", attackTransEnemy, 0.6, triggers = True)
    moveBackEnemy = Animation("moveStateEnemy", moveBackTransEnemy, 1.0)
    hitEnemy = Animation("hitStateEnemy", hitTransEnemy, 0.6)