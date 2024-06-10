# Import StreamController modules
from src.backend.PluginManager.ActionHolder import ActionHolder
from src.backend.PluginManager.PluginBase import PluginBase

# Import Actions
from .actions.BasicActions import BasicActions
from .actions.TickingUi import TickingUi

class AudioControl(PluginBase):
    def __init__(self):
        super().__init__()

        self.basic_action_holder = ActionHolder(
            plugin_base=self,
            action_base=BasicActions,
            action_id="com.GAPLS.PluginTemplate::BasicAction",
            action_name="Basic Action"
        )
        self.add_action_holder(self.basic_action_holder)

        self.ticking_ui_holder = ActionHolder(
            plugin_base=self,
            action_base=TickingUi,
            action_id="com.GAPLS.PluginTemplate::TickingUiExample",
            action_name="Ticking Ui Example"
        )
        self.add_action_holder(self.ticking_ui_holder)

        self.register()