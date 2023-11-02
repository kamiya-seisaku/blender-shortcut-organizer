import bpy

keystrokes = []
modifier = ""

def wrap_text(text, line_length):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        if len(line + word) > line_length:
            lines.append(line.strip())
            line = ""
        line += word + " "
    lines.append(line.strip())
    return '\n'.join(lines)


class KeystrokeCaptorPanel(bpy.types.Panel):
    bl_label = "Keystroke Captor"
    bl_idname = "OBJECT_PT_keystroke_captor"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        global keystrokes
        layout = self.layout
        col = layout.column()
        col.scale_y = 2.0  # Make the text box bigger
        wrapped_text = wrap_text(f"Keystrokes: {', '.join(keystrokes)}", 50)
        col.label(text=wrapped_text)
        col.label(text=f"Keystrokes: {', '.join(keystrokes)}")
        col.operator("wm.keystroke_captor_operator")


class KeystrokeCaptorOperator(bpy.types.Operator):
    bl_idname = "wm.keystroke_captor_operator"
    bl_label = "Capture Keystrokes"

    def modal(self, context, event):
        global keystrokes, modifier
        if event.type == 'ESC':  # Cancel
            return {'CANCELLED'}
        
        # Capture modifier keys
        if event.type in {'LEFT_SHIFT', 'RIGHT_SHIFT', 'LEFT_ALT', 'RIGHT_ALT', 'LEFT_CTRL', 'RIGHT_CTRL', 'OSKEY'}:
            if event.value == 'PRESS':
                modifier = f"{{{event.type.lower()}}}+"
        
        # Capture regular keys
        if event.value == 'PRESS' and event.type not in {'LEFT_SHIFT', 'RIGHT_SHIFT', 'LEFT_ALT', 'RIGHT_ALT', 'LEFT_CTRL', 'RIGHT_CTRL', 'OSKEY', 'ESC'}:
            combined_key = f"{modifier}{event.type.lower()}"
            if len(keystrokes) < 10:
                keystrokes.append(combined_key)
            else:
                keystrokes.pop(0)
                keystrokes.append(combined_key)
                
            modifier = ""  # Reset the modifier

        context.area.tag_redraw()
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

def register():
    bpy.utils.register_class(KeystrokeCaptorOperator)
    bpy.utils.register_class(KeystrokeCaptorPanel)

def unregister():
    bpy.utils.unregister_class(KeystrokeCaptorOperator)
    bpy.utils.unregister_class(KeystrokeCaptorPanel)

if __name__ == "__main__":
    register()
