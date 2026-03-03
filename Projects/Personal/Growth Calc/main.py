#Growth multiplier 1.0125 ** how many levels
GROWTH = 1.0125
MAX_LEVEL = 120


def multiplier_calc(*args, **kwargs):
    multiplier = float(GROWTH ** (MAX_LEVEL - args[0]))
    damage = round(float(kwargs["dmg"]  * multiplier),2)
    health = round(float(kwargs["hp"] * multiplier),2)

    print(f"{damage}K DMG, {health}K HP")

"""(insert level, dmg= insert dmg, hp = insert hp"""
multiplier_calc(101, dmg=244.34, hp=488.67)