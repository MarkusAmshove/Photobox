import SwitchState
import pygame


class Switch():
    def __init__(self):
        pass

    def get_switch_state(self):
        raise NotImplementedError


class KeyboardSwitch(Switch):

    def __init__(self):
        pass

    def get_switch_state(self):
        events = pygame.event.get()
        if len(events) == 0:
            return
        event = events[0]
        switchstate = SwitchState.NONE
        if event.type == pygame.KEYDOWN:
            switchstate = self.get_switch_state_for_key(event.key)
        pygame.event.clear()
        return switchstate

    def get_switch_state_for_key(self, key):
        return {
            pygame.K_ESCAPE: SwitchState.SHUTDOWN,
            pygame.K_RETURN: SwitchState.TRIGGER,
            pygame.K_F4: SwitchState.EXIT
        }.get(key, SwitchState.NONE)
