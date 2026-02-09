import bpy
import json
import os
import math

# --- CONFIGURATION ---
JSON_PATH = r"C:\Users\Riyaz\Downloads\zlendo_project\3d.json"
# The GLB will be saved in your project folder
EXPORT_PATH = r"C:\Users\Riyaz\Downloads\zlendo_project\native_house.glb"

def run_native_engine_complete():
    # 1. Clear Scene
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # 2. Load Data
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)

    layer = data['layers']['layer-1']
    vertices = layer['vertices']
    
    # --- 3. CREATE MATERIALS ---
    # Wall Material (Off-White)
    wall_mat = bpy.data.materials.new(name="WallMat")
    wall_mat.use_nodes = True
    wall_mat.node_tree.nodes.get("Principled BSDF").inputs['Base Color'].default_value = (0.9, 0.9, 0.9, 1.0)
    
    # Floor Material (Light Blue)
    floor_mat = bpy.data.materials.new(name="FloorMat")
    floor_mat.use_nodes = True
    floor_mat.node_tree.nodes.get("Principled BSDF").inputs['Base Color'].default_value = (0.2, 0.5, 0.8, 1.0)

    # --- 4. BUILD WALLS ---
    for line_id, line in layer['lines'].items():
        vS, vE = vertices[line['vertices'][0]], vertices[line['vertices'][1]]
        length = math.sqrt((vE['x'] - vS['x'])**2 + (vE['y'] - vS['y'])**2)
        cx, cy = (vS['x'] + vE['x']) / 2, (vS['y'] + vE['y']) / 2
        angle = math.atan2(vE['y'] - vS['y'], vE['x'] - vS['x'])
        
        bpy.ops.mesh.primitive_cube_add(size=1)
        wall = bpy.context.active_object
        wall.scale = (length, 15, 260) 
        wall.location = (cx, cy, 130)
        wall.rotation_euler[2] = angle
        wall.data.materials.append(wall_mat)

    # --- 5. BUILD FLOORS (AREAS) ---
    for area_id, area in layer['areas'].items():
        mesh_data = bpy.data.meshes.new(f"Floor_{area_id}")
        floor_obj = bpy.data.objects.new(f"Floor_{area_id}", mesh_data)
        bpy.context.collection.objects.link(floor_obj)
        
        # Create coordinates for the floor polygon
        coords = [(vertices[v_id]['x'], vertices[v_id]['y'], 0) for v_id in area['vertices']]
        
        # Connect the dots to make a face
        mesh_data.from_pydata(coords, [], [list(range(len(coords)))])
        mesh_data.update()
        floor_obj.data.materials.append(floor_mat)

    # --- 6. NATIVE EXPORT ---
    # This creates the .glb file the interviewer requested
    bpy.ops.export_scene.gltf(filepath=EXPORT_PATH, export_format='GLB')
    
    print("-" * 30)
    print(f"COMPLETE: Native Model saved to {EXPORT_PATH}")
    print("-" * 30)

run_native_engine_complete()