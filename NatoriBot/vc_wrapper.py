import discord


class vc_wrapper():
    def __init__(self, client):
        if client.voice_clients != []:
            self.voice = client.voice_clients[0]
            self.is_in_vc = True
        else:
            self.is_in_vc = False
