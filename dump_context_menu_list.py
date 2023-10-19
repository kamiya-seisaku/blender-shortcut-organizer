# List entities of bpy.types that has "_context_menu" at the end.

import json
import bpy

context_menu_types = [menu for menu in dir(bpy.types) if menu.endswith('_context_menu')]

# Save to JSON
with open('context_menu_types.json', 'w') as json_file:
    json.dump(context_menu_types, json_file, indent=4)
