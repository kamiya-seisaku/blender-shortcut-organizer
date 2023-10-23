# state_machine.py

if "bpy" in locals():
    pass
else:
    import bpy

class BlenderKeyCaptureStateMachine:
    def __init__(self):
        self.state = 'Idle'
    def transition(self, new_state):
        valid_transitions = {
            'Idle': ['Listening', 'Terminated'],
            'Listening': ['Paused', 'Processing', 'Idle'],
            'Paused': ['Listening', 'Idle'],
            'Processing': ['Listening', 'Idle', 'Error'],
            'Error': ['Idle'],
            'Terminated': []
        }
        key_strokes = ""
        
        if new_state in valid_transitions[self.state]:
            if self.state == 'Idle' & new_state == 'Listening':
                # initialize key_strokes            
                self.key_strokes = ""
                self.state = 'Listening'
            print(f"Transitioned to {self.state}")
        else:
            print(f"Invalid transition from {self.state} to {new_state}")
    
    # 
    def addKeyStroke(self, event):
        pass

# # Proposed State Machine Class
# class BlenderAddonStateMachine:
#     def __init__(self):
#         self.state = 'INITIAL'

#     def transition(self, event):
#         if self.state == 'INITIAL':
#             if event == 'activate':
#                 self.state = 'ACTIVE'
#                 self.on_activate()
#         elif self.state == 'ACTIVE':
#             if event == 'deactivate':
#                 self.state = 'INACTIVE'
#                 self.on_deactivate()

#     def on_activate(self):
#         print('Addon activated')

#     def on_deactivate(self):

#         print('Addon deactivated')