class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2

def on_overlap_tile(sprite, location):
    game.show_long_text("Bem-vindo a galeria, memorize as pinturas e boa sorte!",
        DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        historius
    """),
    on_overlap_tile)

def setLevelTileMap(level: number):
    clearGame()
    if level == 0:
        tiles.set_tilemap(tilemap("""
            level11
        """))
    elif level == 1:
        tiles.set_tilemap(tilemap("""
            level13
        """))
    elif level == 2:
        tiles.set_tilemap(tilemap("""
            level15
        """))
    elif level == 3:
        tiles.set_tilemap(tilemap("""
            level17
        """))
    elif level == 4:
        tiles.set_tilemap(tilemap("""
            level19
        """))
    elif level == 5:
        tiles.set_tilemap(tilemap("""
            level21
        """))
    elif level == 6:
        tiles.set_tilemap(tilemap("""
            level23
        """))
    elif level == 7:
        tiles.set_tilemap(tilemap("""
            level25
        """))
    initializeLevel(level)

def on_overlap_tile2(sprite2, location2):
    game.show_long_text("Me ajude com esses experimentos!", DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile22
    """),
    on_overlap_tile2)

# interações

def on_overlap_tile3(sprite3, location3):
    game.show_long_text("Olá seja- bem vindo a essa aventura!", DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile18
    """),
    on_overlap_tile3)

def clearGame():
    pass
def setLevelTileMap2(level2: number):
    clearGame()
    if level2 == 0:
        tiles.set_tilemap(tilemap("""
            level27
        """))
    elif level2 == 1:
        tiles.set_tilemap(tilemap("""
            level29
        """))
    elif level2 == 2:
        tiles.set_tilemap(tilemap("""
            level31
        """))
    elif level2 == 3:
        tiles.set_tilemap(tilemap("""
            level33
        """))
    elif level2 == 4:
        tiles.set_tilemap(tilemap("""
            level35
        """))
    elif level2 == 5:
        tiles.set_tilemap(tilemap("""
            level37
        """))
    elif level2 == 6:
        tiles.set_tilemap(tilemap("""
            level39
        """))
    elif level2 == 7:
        tiles.set_tilemap(tilemap("""
            level41
        """))
    initializeLevel(level2)

def on_overlap_tile4(sprite4, location4):
    game.show_long_text("Ache a nave para embarcar em um desafio matemático!",
        DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile16
    """),
    on_overlap_tile4)

def initializeLevel(level22: number):
    pass
# fases

def on_overlap_tile5(sprite5, location5):
    pass
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        transparency16
    """),
    on_overlap_tile5)

tiles.set_current_tilemap(tilemap("""
    level0
"""))
personagem = sprites.create(assets.image("""
    personagem1
"""), SpriteKind.player)
controller.move_sprite(personagem, 100, 100)
scene.camera_follow_sprite(personagem)
info.start_countdown(60)