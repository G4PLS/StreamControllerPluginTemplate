# Import StreamController modules
from src.backend.PluginManager.ActionHolder import ActionHolder
from src.backend.PluginManager.PluginBase import PluginBase

from .actions import *

class AudioControl(PluginBase):
    def __init__(self):
        super().__init__()

        self.l01_holder = ActionHolder(
            plugin_base=self,
            action_base=L01_Basic_Functions.BasicFunctions,
            action_id="com.GAPLS.PluginTemplate::L01",
            action_name="L01"
        )
        self.add_action_holder(self.l01_holder)

        self.l02_holder = ActionHolder(
            plugin_base=self,
            action_base=L02_Adding_Ui.Simple_Ui,
            action_id="com.GAPLS.PluginTemplate::L02",
            action_name="L02"
        )
        self.add_action_holder(self.l02_holder)

        self.register()