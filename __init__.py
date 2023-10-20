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

context_menu_types = [menu for menu in dir(bpy.types) if menu.endswith('_context_menu')]

# Popup Window Operator
class ShortcutOrganizerPopupOperator(bpy.types.Operator):
    bl_idname = "object.shortcut_organizer_popup"
    bl_label = "Shortcut Organizer Popup"
    proposed_keys = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        # Always active
        return True

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.label(text="Press key to assign")
        layout.label(text=f"Proposed keys: {self.proposed_keys}")  # Display proposed keys
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
        layout.label(text="Press key to assign")
        layout.label(text=f"Proposed keys: {self.proposed_keys}")  # Display proposed keys
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

# Registration
def register():
    bpy.utils.register_class(ShortcutOrganizer)
    bpy.utils.register_class(OBJECT_PT_ShortcutOrganizerPropertyPanel)
    bpy.types.Scene.debug_mode = bpy.props.BoolProperty(name="Debug Mode")
    bpy.utils.register_class(ReloadAddonOperator)
    # bpy.types.VIEW3D_MT_object_context_menu.append(add_context_menu)

    # Dynamically all from all context menus
    for menu_type in context_menu_types:
        getattr(bpy.types, menu_type, None).append(add_context_menu) if getattr(bpy.types, menu_type, None) is not None else None
        # bpy.types.get(menu_type).append(add_context_menu)

    try:
        bpy.utils.unregister_class(ShortcutOrganizerPopupOperator)
    except:
        pass
    bpy.utils.register_class(ShortcutOrganizerPopupOperator)
    bpy.utils.register_class(AssignKeyOperator)

def unregister():
    bpy.utils.unregister_class(ShortcutOrganizer)
    bpy.utils.unregister_class(OBJECT_PT_ShortcutOrganizerPropertyPanel)
    bpy.utils.unregister_class(ReloadAddonOperator)
    for menu_type in context_menu_types:
        getattr(bpy.types, menu_type, None).remove(add_context_menu) if getattr(bpy.types, menu_type, None) is not None else None
    bpy.utils.unregister_class(AssignKeyOperator)

if __name__ == "__main__":
    register()
