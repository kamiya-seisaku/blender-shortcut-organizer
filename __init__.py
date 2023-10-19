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

# Popup Window Operator
class ShortcutOrganizerPopupOperator(bpy.types.Operator):
    bl_idname = "object.shortcut_organizer_popup"
    bl_label = "Shortcut Organizer Popup"

    @classmethod
    def poll(cls, context):
        # Always active
        return True

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.label(text="Shortcut Organizer Popup")
        layout.operator("object.reload_addon", text="Reload Addon")

    def execute(self, context):
        self.report({'INFO'}, "Popup Opened")
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
class ShortcutOrganizerPropertyPanel(bpy.types.Panel):
    bl_idname = "object.shortcut_organizer_property_panel"
    bl_label = "Shortcut Organizer"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Shortcut Organizer in Property Panel")
        layout.operator("object.shortcut_organizer_popup", text="Open Shortcut Organizer")

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
    bpy.utils.register_class(ShortcutOrganizerPropertyPanel)
    bpy.types.Scene.debug_mode = bpy.props.BoolProperty(name="Debug Mode")
    bpy.utils.register_class(ReloadAddonOperator)
    bpy.types.VIEW3D_MT_object_context_menu.append(add_context_menu)

    try:
        bpy.utils.unregister_class(ShortcutOrganizerPopupOperator)
    except:
        pass
    bpy.utils.register_class(ShortcutOrganizerPopupOperator)

def unregister():
    bpy.utils.unregister_class(ShortcutOrganizer)
    bpy.utils.unregister_class(ShortcutOrganizerPropertyPanel)
    bpy.utils.unregister_class(ReloadAddonOperator)
    bpy.types.VIEW3D_MT_object_context_menu.remove(add_context_menu)

if __name__ == "__main__":
    register()
