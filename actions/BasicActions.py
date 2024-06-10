from src.backend.PluginManager.ActionBase import ActionBase


'''
The most basic method every Method can use are:

on_key_down: 
    This gets triggered whenever the key is pressed down
    
on_key_up: 
    This gets triggered when the key is released,
    it only gets triggered when the key is not being held down.
    When the key is held down on_key_hold_stop will be used
    
on_key_hold_start:
    Triggers when the key is held down for 0.75 seconds

on_key_hold_stop:
    Triggers when the key gets released after on_key_hold_start got triggered

on_tick:
    Triggers every second after the action is initialized 
'''

class BasicActions(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_key_down(self):
        print("Key Is Pressed Down")

    def on_key_up(self):
        print("Key Is Released")

    def on_key_hold_start(self):
        print("Key Is Held Down")

    def on_key_hold_stop(self):
        print("Key Is Released After Holding")

    def on_tick(self):
        print("Ticking")