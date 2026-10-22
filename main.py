@namespace
class SpriteKind:
    Marco = SpriteKind.create()
    Globo1 = SpriteKind.create()
    Globo2 = SpriteKind.create()

def on_player2_button_a_pressed():
    scaling.scale_by_pixels(Globo22, 1, ScaleDirection.UNIFORMLY, ScaleAnchor.BOTTOM)
    Raton2.set_image(assets.image("""
        Raton2-Abajo
    """))
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_on_overlap(sprite, otherSprite):
    mp.game_over_player_win(mp.player_selector(mp.PlayerNumber.ONE))
    game.game_over(True)
sprites.on_overlap(SpriteKind.Globo1, SpriteKind.Marco, on_on_overlap)

def on_player1_button_a_pressed():
    scaling.scale_by_pixels(Globo12, 1, ScaleDirection.UNIFORMLY, ScaleAnchor.BOTTOM)
    Raton1.set_image(assets.image("""
        Raton-Abajo
    """))
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player1_button_a_pressed)

def on_player1_button_a_released():
    Raton1.set_image(assets.image("""
        Raton-Arriba
    """))
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.RELEASED,
    on_player1_button_a_released)

def on_on_overlap2(sprite, otherSprite):
    mp.game_over_player_win(mp.player_selector(mp.PlayerNumber.TWO))
    game.game_over(True)
sprites.on_overlap(SpriteKind.Globo2, SpriteKind.Marco, on_on_overlap2)

def on_player2_button_a_released():
    Raton2.set_image(assets.image("""
        Raton2-Arriba
    """))
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.RELEASED,
    on_player2_button_a_released)

Marco2 = sprites.create(assets.image("""
    Marco
"""), SpriteKind.Marco)
Globo12 = sprites.create(assets.image("""
    Globo
"""), SpriteKind.Globo1)
Globo22 = sprites.create(assets.image("""
    Globo2
"""), SpriteKind.Globo2)
Globo12.set_position(40, 94)
Raton1 = sprites.create(assets.image("""
    Raton-Abajo
"""), SpriteKind.player)
Raton1.set_position(40, 104)
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE), Raton1)
Raton2 = sprites.create(assets.image("""
    Raton2-Abajo
"""), SpriteKind.player)
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.TWO), Raton2)
Globo22.set_position(120, 94)
Raton2.set_position(120, 104)
info.start_countdown(15)
scene.set_background_color(8)