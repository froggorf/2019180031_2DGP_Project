import game_framework
import pico2d

import logo_state
import play_state
import title_state
import stage_select_state
import game_over_state

pico2d.open_canvas(1200,975,sync=True)
game_framework.run(title_state)
pico2d.close_canvas()