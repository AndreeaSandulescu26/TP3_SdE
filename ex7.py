for i in range(5):
        led.plot(i, 2)
        basic.pause(500)
        led.unplot(i, 2)