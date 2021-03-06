from pi_switch import RCSwitchReceiver
from switch import Switch
import SwitchState


class RCSwitch(Switch):

    def __init__(self, triggervalue, shutdownvalue, exitvalue):
        self.receiver = RCSwitchReceiver()
        self.receiver.enableReceive(2)
        self.triggervalue = triggervalue
        self.shutdownvalue = shutdownvalue
        self.exitvalue = exitvalue

    def get_switch_state(self):
        if self.receiver.available():
            value = self.receiver.getReceivedValue()
            self.receiver.resetAvailable()
            return {
                self.triggervalue: SwitchState.TRIGGER,
                self.shutdownvalue: SwitchState.SHUTDOWN,
                self.exitvalue: SwitchState.EXIT
            }.get(value, SwitchState.NONE)
        return SwitchState.NONE
