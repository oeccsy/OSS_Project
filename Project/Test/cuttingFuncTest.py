import bpy

def init_objects_data():
    for id_data in bpy.data.objects:
        bpy.data.objects.remove(id_data)

def selandface():
    bpy.ops.object.mode_set(mode='EDIT') #EDIT 모드로 변경
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.vertices_smooth(factor=0.5, repeat=1)

    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_random(percent=1)
    bpy.ops.mesh.delete(type='VERT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.edge_face_add()

    #만약 vertex수가 심각하게 많이 차이나는 경우
    # bpy.ops.ed.undo()
    # vertex 깔끔하게 하는거 하고 하는게 좋은듯 하다.

def step1(): 
    obj = bpy.context.active_object # 현재 선택한 오브젝트 정보
    vertCount = len(obj.data.vertices)
    bpy.ops.object.mode_set(mode='EDIT') #EDIT 모드로 변경
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.vertices_smooth(factor=0.5, repeat=1)

    for i in range(1, 10):
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_random(percent=1)
        bpy.ops.mesh.delete(type='VERT')
        if vertCount - 10 > len(obj.data.vertices):
            bpy.ops.ed.undo()
        else:
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.edge_face_add()
            if vertCount - 10 > len(obj.data.vertices):
                bpy.ops.ed.undo()
                bpy.ops.ed.undo()
                bpy.ops.ed.undo()
            vertCount = len(obj.data.vertices)


    
def step2():
    for i in range(1, 10):
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_random(percent=1)
        bpy.ops.mesh.delete(type='VERT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.edge_face_add()


def bisect():
    bpy.ops.mesh.bisect(plane_co=(0, 0, 0), plane_no=(1, 1, 1), use_fill=True, clear_inner=True, clear_outer=False)

    #중심 좌표, 법선벡터 ,채울지 말지, 법선벡터