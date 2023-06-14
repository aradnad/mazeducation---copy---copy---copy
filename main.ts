scene.onOverlapTile(SpriteKind.Player, assets.tile`historius`, function (sprite, location) {
    game.showLongText("Bem-vindo a galeria, memorize as pinturas e boa sorte!", DialogLayout.Bottom)
})
// fases
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairWest, function (sprite5, location5) {
    createlevel()
})
function createlevel () {
    if (level == 1) {
        tiles.setCurrentTilemap(tilemap`level0`)
    } else if (level == 2) {
        tiles.setCurrentTilemap(tilemap`level9`)
    } else if (level == 3) {
        tiles.setCurrentTilemap(tilemap`level4`)
    }
}
function clearlevel () {
    for (let value of level) {
        level += 1
    }
    createlevel()
}
// interações
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile18`, function (sprite3, location3) {
    game.showLongText("Olá seja- bem vindo a essa aventura!", DialogLayout.Bottom)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile16`, function (sprite4, location4) {
    game.showLongText("Ache a nave para embarcar em um desafio matemático!", DialogLayout.Bottom)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile22`, function (sprite2, location2) {
    game.showLongText("Me ajude com esses experimentos!", DialogLayout.Bottom)
})
let level = 0
class ActionKind {
    static Walking: number
    private ___Walking_is_set: boolean
    private ___Walking: number
    get Walking(): number {
        return this.___Walking_is_set ? this.___Walking : ActionKind.Walking
    }
    set Walking(value: number) {
        this.___Walking_is_set = true
        this.___Walking = value
    }
    
    static Idle: number
    private ___Idle_is_set: boolean
    private ___Idle: number
    get Idle(): number {
        return this.___Idle_is_set ? this.___Idle : ActionKind.Idle
    }
    set Idle(value: number) {
        this.___Idle_is_set = true
        this.___Idle = value
    }
    
    static Jumping: number
    private ___Jumping_is_set: boolean
    private ___Jumping: number
    get Jumping(): number {
        return this.___Jumping_is_set ? this.___Jumping : ActionKind.Jumping
    }
    set Jumping(value: number) {
        this.___Jumping_is_set = true
        this.___Jumping = value
    }
    
    public static __initActionKind() {
        ActionKind.Walking = 0
        ActionKind.Idle = 1
        ActionKind.Jumping = 2
    }
    
}
ActionKind.__initActionKind()
level = 1
let personagem = sprites.create(assets.image`personagem1`, SpriteKind.Player)
controller.moveSprite(personagem, 100, 100)
scene.cameraFollowSprite(personagem)
info.startCountdown(60)
createlevel()
