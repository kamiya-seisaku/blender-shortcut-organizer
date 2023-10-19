# Produce a comprehensive list of blender functions to which user can assign shortcut key/stroke.

import bpy
import json

keymap_data = {}
keymap_categories = bpy.context.window_manager.keyconfigs.user.keymaps

for category in keymap_categories:
    category_operators = []
    for km_item in category.keymap_items:
        operator_info = {
            "operator": km_item.idname,
            "key": km_item.type,
            "modifier": km_item.shift
        }
        category_operators.append(operator_info)
    keymap_data[category.name] = category_operators

# Save as JSON
with open('blender_keymaps.json', 'w') as json_file:
    json.dump(keymap_data, json_file, indent=4)

print("Keymap data saved as 'blender_keymaps.json'")
