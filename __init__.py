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
# from bpy.types import Operator
# from bpy.props import FloatVectorProperty
# from bpy_extras.object_utils import AddObjectHelper, object_data_add
# from mathutils import Vector

# New Popup Window Operator
class HelloWorldPopupOperator(bpy.types.Operator):
    bl_idname = "object.hello_world_popup"
    bl_label = "Hello World Popup"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello World")
        layout.operator("object.reload_addon", text="Reload Addon")

    def execute(self, context):
        self.report({'INFO'}, "Hello World")
        return {'FINISHED'}

# Main Class for the Addon
class ShortcutOrganizer(bpy.types.Operator):
    bl_idname = "object.shortcut_organizer"
    bl_label = "Shortcut Organizer"
    
    # Intuitive UI
    def draw(self, context):
        layout = self.layout
        # UI elements go here
        pass

    # Direct Assignment
    def assign_shortcut(self, button):
        # Code for direct assignment
        pass
    
    # Shortcut Input Prompt
    def input_prompt(self):
        # Code for input prompt
        pass
    
    # Conflict Resolution
    def resolve_conflict(self, key):
        # Code for conflict resolution
        pass
    
    # Alternative Suggestions
    def suggest_alternatives(self, key):
        # Code for alternative suggestions
        pass
    
    # Final Assignment
    def finalize_assignment(self, key):
        # Code for finalizing assignment
        pass

# New Panel class for the mock window
class HelloWorldPanel(bpy.types.Panel):
    bl_label = "Hello World"
    bl_idname = "OBJECT_PT_hello_world"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    # bl_space_type = 'VIEW_3D'
    # bl_region_type = 'UI'
    bl_category = "Object"
    bl_context = "object"
 
    def draw(self, context):
        layout = self.layout  # Define layout here
        layout.label(text="Hello World")

        # Add Debug Mode checkbox
        layout.prop(context.scene, "debug_mode", text="Debug Mode")

        # Conditionally show Reload Addon button
        if context.scene.debug_mode:
            layout.operator("object.reload_addon", text="Reload Addon")

        # Add button to trigger HelloWorldPopupOperator
        layout.operator("object.hello_world_popup", text="Show Hello World")

# New Reload Addon Operator
class ReloadAddonOperator(bpy.types.Operator):
    bl_idname = "object.reload_addon"
    bl_label = "Reload Addon"

    def execute(self, context):
        bpy.ops.preferences.addon_disable(module="blender-shortcut-organizer")
        bpy.ops.preferences.addon_enable(module="blender-shortcut-organizer")
        return {'FINISHED'}

# Registration

def register():
    # ... rest of your code
    bpy.utils.register_class(ShortcutOrganizer)
    bpy.utils.register_class(HelloWorldPanel)
    bpy.types.Scene.debug_mode = bpy.props.BoolProperty(name="Debug Mode")
    bpy.utils.register_class(ReloadAddonOperator)

    try:
        bpy.utils.unregister_class(HelloWorldPopupOperator)
    except:
        pass  # Class is not registered
    bpy.utils.register_class(HelloWorldPopupOperator)  # Register the new Popup Operator

def unregister():
    bpy.utils.unregister_class(ShortcutOrganizer)
    bpy.utils.unregister_class(HelloWorldPanel)
    bpy.utils.unregister_class(ReloadAddonOperator)  # Unregister the new class


if __name__ == "__main__":
    register()
