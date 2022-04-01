def on_forever():
    led.plot(2, 3)
    basic.pause(500)
    led.unplot(2, 3)
    basic.pause(500)
basic.forever(on_forever)