class LightSwitch:
    def __init__(self):
        self.light_is_on = False

    def turn_on(self):
        self.light_is_on = True

    def turn_off(self):
        self.light_is_on = False

    def show(self):
        print(self.light_is_on)

o_light = LightSwitch()
o_light.show()
o_light.turn_on()
o_light.show()
o_light.turn_off()
o_light.show()


class DimmerSwitch:
    def __init__(self):
        self.light_is_on = False
        self.brightness = 0

    def turn_on(self):
        self.light_is_on = True

    def turn_off(self):
        self.light_is_on = False

    def raise_brightness(self):
        if self.brightness < 10:
            self.brightness +=1
        
    def reduce_brightness(self):
        if self.brightness > 0:
            self.brightness -=1

    def show(self):
        print(self.light_is_on)
        print("The brightness is ", self.brightness)

        