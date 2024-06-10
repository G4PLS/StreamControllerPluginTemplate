from src.backend.PluginManager.ActionBase import ActionBase

import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw

'''
In this example we now integrate some UI into our action so that the user can change things.
Here we only modify if the Action should print "Ticking" into the console but it can be used in more complex ways

First lets go through the methods that are new:

on_ready: 
    This method is called when the page is ready to process requests made by the actions.
    
get_config_rows:
    This is called whenever we "open" the Action Ui, it builds our Ui to be displayed.
    It needs to return an array, meaning you can return multiple elements with: return [ui_elem1, ui_elem2, ...]

We also have a new variable that will be set

self.has_configuration: 
    This comes from the ActionBase and makes it so the Action Automatically opens the
    Ui when we add this Action to a Button
    
    
We also provide some custom methods that make loading easier.
'''

class TickingUi(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.has_configuration = True
        self.should_tick = False

    # Overrides

    def on_ready(self):
        self.load_config()

    def get_config_rows(self):
        '''
        This is responsible to load/build the Ui and return the elements that will be displayed.
        We use an SwitchRow provided by Adw to make the life easy.

        Most Ui elements also have some events that we can listen to. This can be accessed by
        switch_row.connect(<EVENT>, <LISTENER METHOD>).
        What keyword needs to be used for the Ui element is different and not all elements can be connected to so easily.

        After we create the Ui elements we set the Ui config, this just makes it so the Switch is On/Off based on the settings.
        (See self.load_ui_config)

        In the end we only return the switch_row because this is the actual Ui Element. You can also return multiple by doing:
        return [ui_element_1, ui_element_2, ...]
        '''
        self.switch_row = Adw.SwitchRow(title="Is Ticking")

        self.switch_row.connect("notify::active", self.switch_row_changed)

        self.load_ui_config()

        return [self.switch_row]

    def on_tick(self):
        if self.should_tick:
            print("Ticking")

    # Custom Methods

    def load_config(self):
        '''
        This is used in this example to load the settings from the Json into the variable should_tick.
        self.get_settings() returns the dict containing all the keys, this is why we use
        settings.get(<KEY>) to get the value from the dict and provide the default False if it returns None.
        This is so we have a value when the settings are empty, this occurs when the Action is freshly added to an Button
        '''
        settings = self.get_settings()

        self.should_tick = settings.get("should-tick") or False

    def load_ui_config(self):
        '''
        This is used to set Ui settings. It gets called within get_config_rows and makes it so our
        switch actually gets set by default to On/Off True/False.
        Without this it would always be Off/False and wouldnt represent the Settings we actually have

        Because we load our config with load_config we dont have to access the settings (But this can be done aswell)
        '''
        self.switch_row.set_active(self.should_tick)

    def switch_row_changed(self, *args):
        '''
        This method gets triggered whenever the switch changes its state On/Off.
        We use it to update the settings based on the switch state. This is also where the keyword comes into play,
        because this is needed to save and read the settings. So make sure you dont have spelling mistakes!
        '''
        settings = self.get_settings()

        self.should_tick = self.switch_row.get_active()

        settings["should-tick"] = self.should_tick
        self.set_settings(settings)
