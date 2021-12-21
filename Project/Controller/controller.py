import bpy
import os

def init_objects_data():
    for id_data in bpy.data.objects:
        bpy.data.objects.remove(id_data)

def fbx_export(name):
    bpy.ops.export_scene.fbx(filepath=str(os.path.dirname(os.path.realpath(__file__)))+ "\\..\\Output\\" + name+".fbx", object_types={'MESH'}, use_mesh_modifiers=False, add_leaf_bones=False, bake_anim=False)
    #bpy.ops.export_scene.fbx(filepath="C:\\Users\\user\\Desktop\\output\\"+name+".fbx", object_types={'MESH'}, use_mesh_modifiers=False, add_leaf_bones=False, bake_anim=False)
