# state_machine.py

if "bpy" in locals():
    pass
else:
    import bpy

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
        bpy.types.Scene.debug_mode = bpy.props.BoolProperty(name="Debug Mode")
        
        for cls in classes:
            bpy.utils.register_class(cls)

        # Dynamically add from all context menus
        for menu_type in context_menu_types:
            getattr(bpy.types, menu_type, None).append(add_context_menu) if getattr(bpy.types, menu_type, None) is not None else None
        print('Addon activated')

    def on_deactivate(self):
        for cls in reversed(classes):
            bpy.utils.unregister_class(cls)

        # Dynamically remove from all context menus
        for menu_type in context_menu_types:
            getattr(bpy.types, menu_type, None).remove(add_context_menu) if getattr(bpy.types, menu_type, None) is not None else None

        print('Addon deactivated')