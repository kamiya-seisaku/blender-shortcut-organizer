# ... (previous code remains unchanged)

- def register():
-     bpy.utils.register_class(ShortcutOrganizer)
-     bpy.utils.register_class(OBJECT_PT_ShortcutOrganizerPropertyPanel)
-     bpy.types.Scene.debug_mode = bpy.props.BoolProperty(name="Debug Mode")
-     bpy.utils.register_class(ReloadAddonOperator)
-     if "AssignKeyOperator" not in dir(bpy.types):
-         bpy.utils.register_class(AssignKeyOperator)

+ classes = [ShortcutOrganizer, OBJECT_PT_ShortcutOrganizerPropertyPanel, ReloadAddonOperator, AssignKeyOperator]

+ def register():
+     bpy.types.Scene.debug_mode = bpy.props.BoolProperty(name="Debug Mode")
+     for cls in classes:
+         bpy.utils.register_class(cls)

- def unregister():
-     bpy.utils.unregister_class(ShortcutOrganizer)
-     bpy.utils.unregister_class(OBJECT_PT_ShortcutOrganizerPropertyPanel)
-     bpy.utils.unregister_class(ReloadAddonOperator)
-     if "ShortcutOrganizer" in dir(bpy.types):
-         bpy.utils.unregister_class(ShortcutOrganizer)

+ def unregister():
+     for cls in reversed(classes):
+         bpy.utils.unregister_class(cls)

# ... (remaining code remains unchanged)
