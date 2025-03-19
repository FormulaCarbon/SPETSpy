import pyglet

window = pyglet.window.Window(caption = "SPETSpy")
label = pyglet.text.Label('SPETSpy')

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()