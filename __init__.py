# Mostly stable
# -Issues
#  -key stroke capture not stable
#   -look more into screencap code
#  -need icon
# todo: recent operaions list
# todo: invite use of keyboard sc
# todo: operations user frequently use

bl_info = {
    "name": "Blender Shortcut Organizer",
    "author": "kkay",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Tool Shelf > Shortcut Organizer",
    "description": "Simplifies the management of shortcuts in Blender",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

import bpy
import tkinter as tk
import subprocess
import sys

# Initialize variables
keystrokes = ""
modifier = ""

context_menu_types = [menu for menu in dir(bpy.types) if menu.endswith('_context_menu')]

# check for Tkinter availability
def check_tkinter_availability():
    try:
        import tkinter
        print('Tkinter is available.')
    except ImportError:
        print('Tkinter is not available. Installing...')
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tk'])
            print('Tkinter installed successfully.')
        except subprocess.CalledProcessError as e:
            print(f'An error occurred while installing Tkinter: {e}')

# Call the function to check for Tkinter
check_tkinter_availability()

# Function to handle keystrokes in Tkinter
def on_key(event):
    global keystrokes, modifier
    if event.keysym == 'Escape':
        root.quit()
    else:
        if event.keysym in ['Shift_L', 'Shift_R', 'Control_L', 'Control_R', 'Alt_L', 'Alt_R']:
            modifier = event.keysym + "+"
        else:
            combined_key = f"{modifier}{event.keysym}"
            keystrokes += f"{combined_key}, "
            modifier = ""
    root.clipboard_clear()
    root.clipboard_append(keystrokes)
    root.update()

# Popup Window Operator
class ShortcutOrganizerPopupOperator(bpy.types.Operator):
    bl_idname = "object.shortcut_organizer_popup"
    bl_label = "Shortcut Organizer Popup"
    key_stroke = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        # Always active
        return True

    def modal(self, context, event):
        if event.type == 'ESC':  # Cancel
            return {'CANCELLED'}
        elif event.type == 'RET':  # Confirm
            return {'FINISHED'}
        
        if event.value == 'PRESS':
            if self.key_stroke == "Press key to assign.  Type F11 to finish.":
                self.key_stroke = ""
            self.key_stroke += event.type
            print("User pressed:", event.type)
        else:  # Capture any other key
            self.report({'INFO'}, f"Captured key: {event.type}")
            return {'RUNNING_MODAL'}
        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)  # Add this line to initiate the modal operation
        self.key_stroke = "Press key to assign.  Type F11 to finish."
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        self.layout.label(text=f"key: {self.key_stroke}")  # Display proposed keys
        # layout.operator("object.reload_addon", text="Reload Addon")
        self.layout.operator("object.assign_key", text="Assign")  # Add Assign button

    def execute(self, context):
        global keystrokes
        # Initialize Tkinter window
        root = tk.Tk()
        root.title("Keystroke Captor")
        root.bind("<Key>", on_key)
        root.mainloop()
        
        self.key_stroke = keystrokes

        # self.report({'INFO'}, "Popup Opened")
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
        layout.label(text="Press key to assign")
        layout.operator("object.reload_addon", text="Reload Addon")
        layout.operator("object.assign_key", text="Assign")  # Add Assign button

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

# Registration/Unregistration
classes = [ShortcutOrganizer, OBJECT_PT_ShortcutOrganizerPropertyPanel, ReloadAddonOperator, AssignKeyOperator, ShortcutOrganizerPopupOperator]

def register():
    bpy.types.Scene.debug_mode = bpy.props.BoolProperty(name="Debug Mode")
    
    for cls in classes:
       bpy.utils.register_class(cls)

    # Dynamically add from all context menus
    for menu_type in context_menu_types:
        getattr(bpy.types, menu_type, None).append(add_context_menu) if getattr(bpy.types, menu_type, None) is not None else None

def unregister():
    for cls in reversed(classes):
       bpy.utils.unregister_class(cls)

    # Dynamically remove from all context menus
    for menu_type in context_menu_types:
        getattr(bpy.types, menu_type, None).remove(add_context_menu) if getattr(bpy.types, menu_type, None) is not None else None

if __name__ == "__main__":
    register()
