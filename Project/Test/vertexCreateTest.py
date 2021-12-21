import bpy

def init_objects_data():
    for id_data in bpy.data.objects:
        bpy.data.objects.remove(id_data)

def point_cloud(ob_name, coords, edges=[], faces=[]):
    me = bpy.data.meshes.new(ob_name + "Mesh")
    ob = bpy.data.objects.new(ob_name, me)
    me.from_pydata(coords, edges, faces)
    ob.show_name = True
    me.update()
    return ob

if __name__ == '__main__':
    init_objects_data()

    pc = point_cloud("point-cloud", [(0.0, 0.0, 0.0)])
    bpy.context.collection.objects.link(pc)
    