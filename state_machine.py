# state_machine.py

# Proposed State Machine Class
class BlenderAddonStateMachine:
    def __init__(self):
        self.state = 'INITIAL'

    def transition(self, event):
        if self.state == 'INITIAL':
            if event == 'activate':
                self.state = 'ACTIVE'
                self.on_activate()
        elif self.state == 'ACTIVE':
            if event == 'deactivate':
                self.state = 'INACTIVE'
                self.on_deactivate()

    def on_activate(self):
        print('Addon activated')

    def on_deactivate(self):
        print('Addon deactivated')