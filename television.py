class TV:
    def __init__(self):
        self.is_on = False
        self.is_muted = False
        self.channel_list = [2,3,4,5,7,8,9,11,20,36,44,54,65]
        self.n_channels = len(self.channel_list)
        self.channel_index = 0
        self.VOLUME_MIN = 0
        self.VOLUME_MAX = 10
        self.volume = self.VOLUME_MAX

    def power(self):
        self.is_on = not self.is_on

    def volume_up(self):
        if not self.is_on:
            return
        if not self.is_muted:
            self.is_muted = False
        if self.volume < self.VOLUME_MAX:
            self.volume +=1
        
    def volume_down(self):
        if not self.is_on:
            return 
        if not self.is_muted:
            self.is_muted = False
