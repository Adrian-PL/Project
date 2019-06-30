import tcod as libtcod

from entity import Entity
from input_handlers import handle_keys
from map_objects.game_map import GameMap
from render_functions import clear_all, render_all


def main():
    screen_width = 50
    screen_height = 50
    map_width = 50
    map_height = 50

    colors = {
        'dark_wall': libtcod.Color(50, 50, 50),
        'dark_ground': libtcod.Color(0, 160, 0)
    }

    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.orange)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), 'h', libtcod.blue)
    enemy = Entity(int(screen_width / 2 - 12), int(screen_height / 2 + 3), 'e', libtcod.red)
    entities = [enemy, npc, player]

    libtcod.console_set_custom_font('font.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'Project', False)

    con = libtcod.console_new(screen_width, screen_height)

    game_map = GameMap(map_width, map_height)

    entity = Entity

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        render_all(con, entities, game_map, screen_width, screen_height, colors)

        libtcod.console_flush()

        clear_all(con, entities)

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move

            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)

            if not entity.us_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
     main()
