# Existing imports
import bpy

# ... (existing code)

# List of context menu types
context_menu_types = [
    'VIEW3D_MT_object_context_menu',
    'VIEW3D_MT_armature_context_menu',
    # ... (add more context menu types here)
]

# Registration
def register():
    # ... (existing code)
    
    # Dynamically append to all context menus
    for menu_type in context_menu_types:
        bpy.types.get(menu_type).append(add_context_menu)

# Unregistration
def unregister():
    # ... (existing code)
    
    # Dynamically remove from all context menus
    for menu_type in context_menu_types:
        bpy.types.get(menu_type).remove(add_context_menu)

# ... (existing code)
