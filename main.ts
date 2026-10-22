namespace SpriteKind {
    export const Marco = SpriteKind.create()
    export const Globo1 = SpriteKind.create()
    export const Globo2 = SpriteKind.create()
}

controller.player2.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function on_player2_button_a_pressed() {
    scaling.scaleByPixels(Globo22, 1, ScaleDirection.Uniformly, ScaleAnchor.Bottom)
    Raton2.setImage(assets.image`
        Raton2-Abajo
    `)
})
sprites.onOverlap(SpriteKind.Globo1, SpriteKind.Marco, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    mp.gameOverPlayerWin(mp.playerSelector(mp.PlayerNumber.One))
    game.gameOver(true)
})
controller.player1.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function on_player1_button_a_pressed() {
    scaling.scaleByPixels(Globo12, 1, ScaleDirection.Uniformly, ScaleAnchor.Bottom)
    Raton1.setImage(assets.image`
        Raton-Abajo
    `)
})
controller.player1.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Released, function on_player1_button_a_released() {
    Raton1.setImage(assets.image`
        Raton-Arriba
    `)
})
sprites.onOverlap(SpriteKind.Globo2, SpriteKind.Marco, function on_on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    mp.gameOverPlayerWin(mp.playerSelector(mp.PlayerNumber.Two))
    game.gameOver(true)
})
controller.player2.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Released, function on_player2_button_a_released() {
    Raton2.setImage(assets.image`
        Raton2-Arriba
    `)
})
let Marco2 = sprites.create(assets.image`
    Marco
`, SpriteKind.Marco)
let Globo12 = sprites.create(assets.image`
    Globo
`, SpriteKind.Globo1)
let Globo22 = sprites.create(assets.image`
    Globo2
`, SpriteKind.Globo2)
Globo12.setPosition(40, 94)
let Raton1 = sprites.create(assets.image`
    Raton-Abajo
`, SpriteKind.Player)
Raton1.setPosition(40, 104)
mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.One), Raton1)
let Raton2 = sprites.create(assets.image`
    Raton2-Abajo
`, SpriteKind.Player)
mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two), Raton2)
Globo22.setPosition(120, 94)
Raton2.setPosition(120, 104)
info.startCountdown(15)
scene.setBackgroundColor(8)
