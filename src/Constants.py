
SCREEN_SIZE = (240, 136)

t=0
pos = Vector2(0,0)

invent = 1
inventmen = False
inventbtnPresses = [False, False, False, False]

inventory = {"grass": 10, "planks": 10, "stone": 10, "leaves": 10, "logs": 2, "chest": 1, "":0, "stone pickaxe":1, "iron ingot": 3, "stone sword": 120}
inventoryLayout = [["grass", "planks", "stone","leaves","logs",""],
                   ["chest","stone pickaxe","iron ingot","","",""],
                   ["","stone sword","","","",""],
                   ["","","","","",""],
                   ["","","","","",""],
                   ["","","","","",""]]



sprites = {"grass":2, "planks":101, "":150, "stone":3, "leaves": 4, "logs": 5, "chest": 18, "dark stone":20,
           "stone pickaxe":320, "iron pickaxe": 321, "gold pickaxe": 322, "diamond pickaxe": 323,
           "stone sword": 336, "iron sword": 336, "gold sword": 337, "diamond sword": 338,
           "stone spear": 352, "iron spear": 337, "gold spear": 338, "diamond spear": 339,
           "stone axe": 368, "iron axe":369, "gold axe":370, "diamond axe": 371,
           # ores
           "iron ore": 22, "gold ore": 23, "diamond ore": 24,
           "iron ingot": 38, "gold ingot": 39, "diamond peice": 40}

UNDERGROUND = ["stone", "darkstone", "gold ore", "iron ore", "diamond ore"]


ORES = ["iron ore", "gold ore", "diamond ore"]

INVENTORY_ORES = ["iron ingot", "gold ingot", "diamond peice"]

ORES_TO_INVENTORY = {"iron ore":"iron ingot", "gold ore": "gold ingot", "diamond ore": "diamond peice"}

ORES_VEIN_SIZE = {"iron ore": 4, "gold ore": 3, "diamond ore": 2}

WEAPONS = ["stone sword", "iron sword", "gold sword", "diamond sword", "stone spear", "iron spear", "gold spear", "diamond spear"]

WEAPONS_ATTACK = {"stone sword": 12, "iron sword": 20, "diamond sword": 30, "stone spear": 10, "gold spear": 15, "iron spear": 20, "diamond spear": 40, "gold sword": 23}

WEAPONS_DURABILITY = {"stone sword": 120, "iron sword": 200, "gold sword": 50, "diamond sword": 300, " stone spear": 50, "iron spear": 100, "gold spear": 25, "diamond spear": 150}

nonPlacables = ["stone pickaxe", "stone sword", "stone axe", "stone spear",
                "iron pickaxe", " iron sword", "iron axe", "iron spear",
                "gold pickaxe", "gold sword", "gold axe", "gold spear",
                "diamond pickaxe", "diamond sword", "diamond axe", "diamond spear",
                ### ores and ingots
                "iron ingot", "gold ingot", "diamond peice"]

breaking_tools = {"stone pickaxe":1, "iron pickaxe": 2, "gold pickaxe": 4, "diamond pickaxe": 5}

placeSprites = {"grass":2, "planks":1, "stone":3, "": 0, "leaves": 4, "logs": 5, "chest": 18, "dark stone":20}

bottomBlocks = ["dark stone", "grass"]

inventorySellection = [0,0]

cBlock = ""

counter = Vector2(0,0)

speed = 1

walkable_blocks = ["grass", "leaves", "dark stone"]

walkable_blocks = [placeSprites[block] for block in walkable_blocks]

bottomBlocksBack = [placeSprites[block] for block in bottomBlocks]

#player stuff
PLAYERMAXHEALTH = 100


playerCurrentHealth = PLAYERMAXHEALTH

stone_map = [
    [False for x in range(SCREEN_SIZE[0])]
    for y in range(SCREEN_SIZE[1])
]

