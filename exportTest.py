import bpy

def init_objects_data():
    for id_data in bpy.data.objects:
        bpy.data.objects.remove(id_data)

if __name__ == '__main__':
    init_objects_data()

    index = 1

    bpy.ops.mesh.primitive_cylinder_add(location=(0.0, 0.0, 0.0)) # newObj == Set
    new_object = bpy.context.active_object
    new_object.name = "cylinder" + str(index)

    bpy.ops.export_scene.fbx(filepath='C:\\Users\\user\\Desktop\\new_mesh.fbx', object_types={'MESH'}, use_mesh_modifiers=False, add_leaf_bones=False, bake_anim=False)
  
    #bpy.ops.outliner.delete()
    #bpy.ops.object.delete(use_global=False, confirm=False)