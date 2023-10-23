# minimum value product features
#  0 context menu
#  1 key stroke input
#  2 conflict check
#  3 assign
#   10/21 text box not sufficient, need modifiers
#   10/22 looking into nutti's code at https://github.com/nutti/Screencast-Keys
#   10/23 state machine introduced

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

from .shortcut_organizer_classes import context_menu_types, classes

# Registration
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
