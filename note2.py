# In __init__.py or wherever you register the class
def register():
+   if "AssignKeyOperator" not in bpy.types.classes:
        bpy.utils.register_class(AssignKeyOperator)

####

# In the class definition of OBJECT_PT_ShortcutOrganizerPropertyPanel
class OBJECT_PT_ShortcutOrganizerPropertyPanel(bpy.types.Panel):
+   proposed_keys = bpy.props.StringProperty()


# In __init__.py or wherever you unregister the class
def unregister():
+   if "ShortcutOrganizer" in bpy.types.classes:
        bpy.utils.unregister_class(ShortcutOrganizer)
