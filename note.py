# Popup Window Operator

    def draw(self, context):
        layout = self.layout
        layout.label(text="Press key to assign or ESC to finish.")
        for key in self.proposed_keys:
            layout.label(text=f"Alternative: {key.name}")
        layout.operator("object.assign_key", text="Assign")


############################
# Assign Key Operator
class AssignKeyOperator(bpy.types.Operator):
    bl_idname = "object.assign_key"
    bl_label = "Assign Key"

    def execute(self, context):
        # Your code to assign the key stroke
        return {'FINISHED'}


#########################
    def draw(self, context):
        layout = self.layout
        layout.label(text="Press key to assign")
        layout.label(text=f"Proposed keys: {self.proposed_keys}")  # Display proposed keys
        layout.operator("object.reload_addon", text="Reload Addon")
        layout.operator("object.assign_key", text="Assign")  # Add Assign button

# New Operator for Assigning Key
class AssignKeyOperator(bpy.types.Operator):
    bl_idname = "object.assign_key"
    bl_label = "Assign Key"

    def execute(self, context):
        # Your logic to assign the key goes here
        return {'FINISHED'}

# Registration
def register():
    # ... (existing registration code)
    bpy.utils.register_class(AssignKeyOperator)  # Register the new operator

# Unregistration
def unregister():
    # ... (existing unregistration code)
    bpy.utils.unregister_class(AssignKeyOperator)  # Unregister the new operator
