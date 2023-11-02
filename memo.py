#   import bpy
# - import tkinter as tk
# - import subprocess
# - import sys
#   import keystroke_captor2

#   # Initialize variables
#   keystrokes = ""
#   modifier = ""

#   context_menu_types = [menu for menu in dir(bpy.types) if menu.endswith('_context_menu')]

# - # check for Tkinter availability
# - def check_tkinter_availability():
# -     ...
# - # Call the function to check for Tkinter
# - check_tkinter_availability()

# - # Function to handle keystrokes in Tkinter
# - def on_key(event):
# -     ...
  
  # Popup Window Operator
  class ShortcutOrganizerPopupOperator(bpy.types.Operator):
      ...
      def execute(self, context):
          global keystrokes
          # Initialize Tkinter window
-         root = tk.Tk()
-         root.title("Keystroke Captor")
-         root.bind("<Key>", on_key)
-         root.mainloop()
+         # Removed Tkinter part
          self.key_stroke = keystrokes
          return {'FINISHED'}

  # Assign Key Operator
  class AssignKeyOperator(bpy.types.Operator):
      ...

  # Main Class for the Addon
- class ShortcutOrganizer(bpy.types.Operator):
+ class ShortcutOrganizerMain(bpy.types.Operator):  # Renamed
      ...

  # Panel class for the Property Window
  class OBJECT_PT_ShortcutOrganizerPropertyPanel(bpy.types.Panel):
      ...

  # Context menu to add Popup
  def add_context_menu(self, context):
      ...

  # Reload Addon Operator
  class ReloadAddonOperator(bpy.types.Operator):
      ...

  # New operator to assign a shortcut
  class WM_OT_AssignShortcut(bpy.types.Operator):
      ...

  # Registration/Unregistration
  classes = [ShortcutOrganizerMain, OBJECT_PT_ShortcutOrganizerPropertyPanel, ReloadAddonOperator, AssignKeyOperator, ShortcutOrganizerPopupOperator, WM_OT_AssignShortcut]
