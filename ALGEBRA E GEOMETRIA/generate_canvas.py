import os
import json
import re
import math

vault_dir = "/home/rocco/Documenti/MyObsidianLib/ALGEBRA E GEOMETRIA"
appunti_dir = os.path.join(vault_dir, "Appunti")
canvas_file = os.path.join(vault_dir, "Mappa_Algebra_Lineare.canvas.canvas")

files_data = []
# Map from basename (without extension) to relative path
name_to_relpath = {}

# Find all markdown files
for root, dirs, files in os.walk(appunti_dir):
    for f in files:
        if f.endswith(".md"):
            abs_path = os.path.join(root, f)
            rel_path = os.path.relpath(abs_path, vault_dir)
            basename = f[:-3]
            name_to_relpath[basename] = rel_path
            
            with open(abs_path, 'r', encoding='utf-8') as file_obj:
                content = file_obj.read()
            
            # Extract links: [[Link]] or [[Link|Alias]] or [[Link#Heading|Alias]]
            links = re.findall(r'\[\[(.*?)\]\]', content)
            target_names = []
            for link in links:
                target = link.split('|')[0].split('#')[0].strip()
                target_names.append(target)
            
            files_data.append({
                "basename": basename,
                "rel_path": rel_path,
                "folder": os.path.basename(root),
                "targets": target_names
            })

# We'll group them by folder
folders = {}
for data in files_data:
    folder = data['folder']
    if folder not in folders:
        folders[folder] = []
    folders[folder].append(data)

nodes = []
edges = []

node_ids = {}
id_counter = 1

# Generate nodes grouped by folder
current_y = 0
for folder, f_data_list in folders.items():
    current_x = 0
    # Add a group node for the folder maybe? Or just place them together
    for data in f_data_list:
        node_id = f"node_{id_counter}"
        node_ids[data['rel_path']] = node_id
        id_counter += 1
        
        nodes.append({
            "id": node_id,
            "type": "file",
            "file": data['rel_path'],
            "x": current_x,
            "y": current_y,
            "width": 300,
            "height": 200
        })
        current_x += 400
        if current_x > 2000:
            current_x = 0
            current_y += 300
    current_y += 400

edge_counter = 1
for data in files_data:
    source_id = node_ids[data['rel_path']]
    for target in data['targets']:
        if target in name_to_relpath:
            target_relpath = name_to_relpath[target]
            if target_relpath in node_ids:
                target_id = node_ids[target_relpath]
                edges.append({
                    "id": f"edge_{edge_counter}",
                    "fromNode": source_id,
                    "fromSide": "right",
                    "toNode": target_id,
                    "toSide": "left"
                })
                edge_counter += 1

# Load existing canvas if we want to preserve old nodes, but the prompt says 
# "integra la mappa con tutti i punti e i collegamenti presenti nella cartella appunti"
# which implies adding to the existing ones.
try:
    with open(canvas_file, 'r', encoding='utf-8') as cf:
        canvas = json.load(cf)
except:
    canvas = {"nodes": [], "edges": []}

# To avoid id collision, just append. Actually, the old IDs are strings like "n_polinomi".
# We should shift our newly generated nodes to not overlap too much, maybe start x=2000.
offset_x = 2000
for n in nodes:
    n['x'] += offset_x

canvas['nodes'].extend(nodes)
canvas['edges'].extend(edges)

with open(canvas_file, 'w', encoding='utf-8') as cf:
    json.dump(canvas, cf, indent=2)

print(f"Added {len(nodes)} nodes and {len(edges)} edges to the canvas.")
