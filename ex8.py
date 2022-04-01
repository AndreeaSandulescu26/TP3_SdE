list2: List[Image] = []
index = 0
index2 = 0

def on_forever():
    global list2, index, index2
    list2 = [images.icon_image(IconNames.EIGTH_NOTE),
        images.icon_image(IconNames.GHOST),
        images.icon_image(IconNames.UMBRELLA),
        images.icon_image(IconNames.GIRAFFE)]
    index = 0
    while index < len(list2):
        if input.button_is_pressed(Button.B):
            list2[index].show_image(0)
            index += 1
        if input.button_is_pressed(Button.A) and index > 0:
            list2[index - 1].show_image(0)
            index += -1
        if input.button_is_pressed(Button.A) and index == 0:
            index = len(list2) - 1
            list2[index].show_image(0)
            index2 += -1
basic.forever(on_forever)

