"""
This script collects all potentially assignable keymaps in Blender from both the active and default key configurations.
It saves this data as a JSON file, allowing for comprehensive analysis and modification of keymap configurations.

Author: [Your Name]
Version: 1.1
"""

import bpy
import json

keymap_data = {}
keymap_categories = []

# Include both active and default key configurations
key_configs = [bpy.context.window_manager.keyconfigs.active, bpy.context.window_manager.keyconfigs.default]

for config in key_configs:
    for category in config.keymaps:
        if category.name not in keymap_data:
            keymap_data[category.name] = []

        for km_item in category.keymap_items:
            operator_info = {
                "operator": km_item.idname,
                "key": km_item.type,
                "modifier": km_item.shift,
                "key_config": config.name
            }
            keymap_data[category.name].append(operator_info)

# Save as JSON
with open('all_blender_keymaps.json', 'w') as json_file:
    json.dump(keymap_data, json_file, indent=4)

print("All keymap data saved as 'all_blender_keymaps.json'")
