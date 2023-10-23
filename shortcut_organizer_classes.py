# shortcut_organizer_classes.py

# Imports
import bpy

# Globals
context_menu_types = [menu for menu in dir(bpy.types) if menu.endswith('_context_menu')]

class BlenderKeyCaptureStateMachine:
    def __init__(self):
        self.key_strokes = ""
        self.valid_state_transitions = {
            'Idle': ['Listening', 'Terminated'],
            'Listening': ['Paused', 'Processing', 'Idle'],
            'Paused': ['Listening', 'Idle'],
            'Processing': ['Listening', 'Idle', 'Error'],
            'Error': ['Idle'],
            'Terminated': []
        }
        self.state = 'Idle'
        self.key_strokes = ""

    def transition(self, new_state):
        # check validness of new_state
        if not new_state in self.valid_state_transitions(self.state):
            print(f"Invalid transition from {self.state} to {new_state}")
            self.state = 'Error'
            return('Error')

        # continue only for valid new_state
        if self.state == 'Idle' and new_state == 'Listening':
            # state is just transitioning to 'Listening'
            self.state = 'Listening'
            # Initialize self.key_strokes
            self.key_strokes = ""
            return('Listening')
        else:
            pass
    # 
    def addKeyStroke(self, event):
        self.key_strokes = event

# Initialize state machine
sm = BlenderKeyCaptureStateMachine

# Popup Window Operator
class ShortcutOrganizerPopupOperator(bpy.types.Operator):
    bl_idname = "object.shortcut_organizer_popup"
    bl_label = "Shortcut Organizer Popup"
    proposed_keys = bpy.props.StringProperty()
    
    # Event history.
    # Format: [time, event_type, modifiers, repeat_count]
    event_history = []
    # Operator history.
    # Format: [time, bl_label, idname_py, addr]
    operator_history = []

    @classmethod
    def poll(cls, context):
        # Always active
        return True

    def modal(self, context, event):
        if event.type == 'TIMER':  # Timer event
            context.area.tag_redraw()  # Force a redraw of the area to update the UI

        if event.type == 'ESC':  # Cancel
            sm.transition("Terminated")
            return {'CANCELLED'}

        elif event.type == 'RET':  # Confirm
            sm.transition("Terminated")
            self.proposed_keys = sm.key_strokes
            return {'FINISHED'}
        
        if event.value == 'PRESS':
            # Initiate listening to key strokes
            if sm.state == "Idle": 
                sm.transition("Listening")
                sm.addKeyStroke(event)
                self.proposed_keys = sm.key_strokes
            elif sm.state == "Listening":
                sm.addKeyStroke(event)
            captured_keys = sm.get_captured_keys()
            if captured_keys:
                self.proposed_keys = captured_keys

        else:  # Capture any other key
            self.report({'INFO'}, f"Captured key: {event.type}")
            return {'RUNNING_MODAL'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)  #Initiate the modal operation
        self.proposed_keys = "Press key to assign.  Type F11 to finish."
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.label(text=f"{self.proposed_keys}")  # Display proposed keys
        layout.operator("object.reload_addon", text="Reload Addon")
        layout.operator("object.assign_key", text="Assign")  # Add Assign button

    def execute(self, context):
        self.report({'INFO'}, "Popup Opened")
        return {'FINISHED'}

# Assign Key Operator
class AssignKeyOperator(bpy.types.Operator):
    bl_idname = "object.assign_key"
    bl_label = "Assign Key"

    def execute(self, context):
        # Your code to assign the key stroke
        return {'FINISHED'}

# Main Class for the Addon
class ShortcutOrganizer(bpy.types.Operator):
    bl_idname = "object.shortcut_organizer"
    bl_label = "Shortcut Organizer"

    def draw(self, context):
        layout = self.layout
        pass

    # Todo: Functionality implementations

# Panel class for the Property Window
class OBJECT_PT_ShortcutOrganizerPropertyPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_ShortcutOrganizerPropertyPanel"
    bl_label = "Shortcut Organizer"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        # layout = self.layout
        # layout.label(text="Shortcut Organizer in Property Panel")
        # layout.operator("object.shortcut_organizer_popup", text="Open Shortcut Organizer")
        layout = self.layout
        # layout.label(text="Press key to assign")
        layout.operator("object.reload_addon", text="Reload Addon")
        # layout.operator("object.assign_key", text="Assign")  # Add Assign button

# Context menu to add Popup
def add_context_menu(self, context):
    self.layout.operator('object.shortcut_organizer_popup')

# Reload Addon Operator
class ReloadAddonOperator(bpy.types.Operator):
    bl_idname = "object.reload_addon"
    bl_label = "Reload Addon"

    def execute(self, context):
        bpy.ops.preferences.addon_disable(module="blender-shortcut-organizer")
        bpy.ops.preferences.addon_enable(module="blender-shortcut-organizer")
        return {'FINISHED'}

classes = [ShortcutOrganizer, OBJECT_PT_ShortcutOrganizerPropertyPanel, ReloadAddonOperator, AssignKeyOperator, ShortcutOrganizerPopupOperator]

