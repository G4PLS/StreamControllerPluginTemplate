from src.backend.PluginManager.ActionBase import ActionBase

# Import Ui Stuff
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw

'''
You may have noticed that the Console gets filled quite a lot with the Ticking message because of the on_tick method.
In this example we will add very simple Ui to make it possible to toggle the Ticking message On/Off.

For this we need Adw and/or Gtk, in the import above is what is used for Gtk and Adw.

We will also need a few new methods:

get_config_rows:
    Creates and returns the created/build Ui
'''

class Simple_Ui(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        '''
        has_configuration:
            True/False determines if the Action Ui should be opened when adding the Action to a Button
            
        tick:
            Custom variable that will control if the "Ticking" message will be displayed to the console
        '''

        self.has_configuration = True
        self.tick = False

    # Overrides

    def on_ready(self):
        '''
        Loading any form of settings needs to be done earliest in on_ready, doing it in the init method will not work
        because the settings are not present at that state of the program flow.

        load_config will load our settings
        '''
        self.load_config()

    def get_config_rows(self) -> "list[Adw.PreferencesRow]":
        '''
        Create/Builds the Ui for the Action. This will be shown when the User clicks on the action to change settings (When present)

        In here we create a switch row (Its just a Fancy switch).

        We also need to connect the event of said switch so we can update the settings depending on the switch.
        Event keywords can be different for every Ui Element and most of the times you have to look up what the correct keyword is that needs to be used.
        You also cant always directly use the .connect on the element, sometimes you need to access a sub-element to connect to.

        Yes it is very confusing and it can become frustrating

        Lastly we want to load settings into our Ui, this is done so the Ui can always represent the actual settings.
        If we would not do this the switch would always be Off when opening the Action Ui, and ofcourse this is not always the case.

        At the end we return all needed Ui Elements, meaning we could also do:
        return [ui_elem_1, ui_elem_2, ...]
        '''
        # Creates the Switch
        self.switch_row = Adw.SwitchRow(title="Toggle Ticking")

        # Connect the needed event to the on_switch_row_changed function
        self.switch_row.connect("notify::active", self.on_switch_row_changed)

        # Loads settings into the Ui
        self.load_ui_config()

        # Returns all needed Ui Elements
        return [self.switch_row]

    def on_tick(self):
        if self.tick:
            print("Ticking")

    # Helper Functions

    def load_config(self):
        '''
        This is used to get the current settings that are present and assigning the corresponding value to tick.

        get_settings() returns the current setting dict, this is why we use .get(<KEY>).
        Should we get None we set a default, in this case False
        '''
        # Gets the current settings
        settings = (self.get_settings())

        # Adds the value from the settings or uses False as a default value if the settings dont contain the value
        self.tick = settings.get("ticking") or False

    def on_switch_row_changed(self, *args):
        '''
        This will get triggered whenever we change the state of the switch (On/Off).
        We use *args to make sure args that may get passed into the function work and dont throw an error.
        Most of the time args are not used because you can access everything you need without them (Mostly)

        We also need to update tick and the settings, this is done by either "adding" or "modifying" the Value at the Key.
        Then we can use set_settings(<SETTINGS DICT>) to save the settings
        '''
        # Gets the current settings
        settings = self.get_settings()

        # Updates the Tick variable with the current state of the Switch
        self.tick = self.switch_row.get_active()

        # Adds or Modifies the Value at the Key "ticking" to the current value in tick
        settings["ticking"] = self.tick

        # Saves the settings
        self.set_settings(settings)

    def load_ui_config(self):
        '''
        In this method we load all values that are needed into our Ui, this gets called every time we open the Ui.

        We could use the settings directly but because we already have the values needed
        we can just use tick and save a few extra unneeded steps
        '''

        self.switch_row.set_active(self.tick)