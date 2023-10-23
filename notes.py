# Imports
if "bpy" in locals():
    from .state_machine import BlenderKeyCaptureStateMachine
    pass
else:
    import bpy

+ # Initialize state machine
+ sm = BlenderKeyCaptureStateMachine()

# Popup Window Operator
class ShortcutOrganizerPopupOperator(bpy.types.Operator):
    ...
    def modal(self, context, event):
        ...
+       # Leverage state machine for key capture
+       sm.transition(event.type)
+       captured_keys = sm.get_captured_keys()
+       if captured_keys:
+           self.proposed_keys = captured_keys
        ...
