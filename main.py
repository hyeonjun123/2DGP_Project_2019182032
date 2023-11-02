from pico2d import *

import logo_mode
open_canvas()
logo_mode.init()


#logo_mode.running = true이다.
while logo_mode.running:
    logo_mode.handle_events()
    logo_mode.update()
    logo_mode.draw()
    delay(0.01)

logo_mode.finish()
close_canvas()
