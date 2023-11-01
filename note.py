v  import bpy
v+ import tkinter as tk

v+ # Initialize variables
v+ keystrokes = ""
v+ modifier = ""

v+ # Function to handle keystrokes in Tkinter
  + def on_key(event):
  +     global keystrokes, modifier
  +     if event.keysym == 'Escape':
  +         root.quit()
  +     else:
  +         if event.keysym in ['Shift_L', 'Shift_R', 'Control_L', 'Control_R', 'Alt_L', 'Alt_R']:
  +             modifier = event.keysym + "+"
  +         else:
  +             combined_key = f"{modifier}{event.keysym}"
  +             keystrokes += f"{combined_key}, "
  +             modifier = ""
  +     root.clipboard_clear()
  +     root.clipboard_append(keystrokes)
  +     root.update()

v  # Existing Popup Window Operator
    class ShortcutOrganizerPopupOperator(bpy.types.Operator):
        bl_idname = "object.shortcut_organizer_popup"
        bl_label = "Shortcut Organizer Popup"
        key_stroke = bpy.props.StringProperty()

        @classmethod
        def poll(cls, context):
            return True

        def execute(self, context):
  +         global keystrokes
  +         # Initialize Tkinter window
  +         root = tk.Tk()
  +         root.title("Keystroke Captor")
  +         root.bind("<Key>", on_key)
  +         root.mainloop()
  +         
            # Your existing code to handle the captured keystrokes
  +         self.key_stroke = keystrokes
            # ... (rest of the existing code)
            return {'FINISHED'}

  # ... (rest of the existing code)
