# blender-json-to-3d-engine
A Python engine for Blender that converts architectural JSON data into 3D GLB models
# 🏠 JSON to Native 3D Engine (Blender)

This project is a technical solution for converting 2D architectural JSON data into a high-fidelity, 3D GLB asset using **Blender's Python API (bpy)**.

## 🛠 Features
- **Procedural Mesh Generation:** Automatically builds walls at 260 units height.
- **Room Mapping:** Identifies and generates floors for the Hall, Bedroom, Kitchen, Bathroom, and Porch.
- **Aesthetic Materials:** Applies a professional architectural color palette.
- **Native Export:** Outputs a `.glb` file compatible with Unreal Engine 5.

## 🚀 How to Run
1. Open **Blender 5.0+**.
2. Open the **Scripting** tab and load `native_engine.py`.
3. Update the `JSON_PATH` variable to point to your `3d.json`.
4. Run the script.

## 📦 Deliverables
- `3d.json`: Input Data
- `native_engine.py`: The Engine Logic
- `native_house.glb`: The Native 3D Asset
