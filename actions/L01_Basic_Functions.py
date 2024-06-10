from src.backend.PluginManager.ActionBase import ActionBase

'''
In this example we simple print Key Down when the key is pressed and
Key Up when the Key is Released. There are other functions like on_ready and on_tick, those are used in this example to
give an overview over the most basic functions and most used functions in every Action.

on_ready:
    his method is called when the page is ready to process requests made by the actions.

on_key_down:
    Gets called whenever a key on the Stream Deck is pressed down

on_key_up:
    Gets called whenever a key on the Stream Deck is released
    
on_tick:
    Gets called every second/tick
    
Most event functions, meaning the functions that will be called when something happens, have the prefix on_X_Y_Z.
'''

class BasicFunctions(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_ready(self):
        print("Action is ready to go!")

    def on_key_down(self):
        print("Key Down")

    def on_key_up(self):
        print("Key Up")

    def on_tick(self):
        print("Tick")