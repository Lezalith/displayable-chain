# Transforms used by the AnimationChain
transform enterTransEnemy():

    xalign 0.7 yalign 0.5 xoffset 600 alpha 0.0
    linear 1.0 xoffset 0 alpha 1.0

transform idleTransEnemy():

    xalign 0.7 yalign 0.5

transform moveForwardTransEnemy():

    xalign 0.7 yalign 0.5
    linear 1.0 xalign 0.3

transform attackTransEnemy():

    xalign 0.3 yalign 0.5
    linear 0.3 xoffset -50
    linear 0.3 xoffset 0

transform moveBackTransEnemy():

    xalign 0.3 yalign 0.5
    linear 1.0 xalign 0.7


# Images definitions
image enterStateEnemy = Composite(
    (200, 200),
    (0, 0), Solid("00FF7F"),
    (0, 0), Text("entering", size = 40, color = "f00"))

image idleStateEnemy = Composite(
    (200, 200),
    (0, 0), Solid("7CFC00"),
    (0, 0), Text("idle", size = 40, color = "f00"))

image moveStateEnemy = Composite(
    (200, 200),
    (0, 0), Solid("90EE90"),
    (0, 0), Text("moving", size = 40, color = "f00"))

image attackStateEnemy = Composite(
    (200, 200),
    (0, 0), Solid("8FBC8F"),
    (0, 0), Text("attacking", size = 40, color = "f00"))


# Animation definitions, put together from Transforms and Images defined above.
define enterEnemy = Animation("enterStateEnemy", enterTransEnemy, 1.0)
define idleEnemy = Animation("idleStateEnemy", idleTransEnemy, 0)
define moveForwardEnemy = Animation("moveStateEnemy", moveForwardTransEnemy, 1.0)
define attackEnemy = Animation("attackStateEnemy", attackTransEnemy, 0.6)
define moveBackEnemy = Animation("moveStateEnemy", moveBackTransEnemy, 1.0)

default enemyChain = AnimationChain( enterEnemy, idleEnemy, moveForwardEnemy, attackEnemy, moveBackEnemy )