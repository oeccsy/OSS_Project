import bpy
import random

def subdivision(ranVal_1, ranVal_2):
    #### Subdivision 동작 ####

    bpy.ops.object.mode_set(mode='EDIT') #EDIT 모드로 변경

    bpy.ops.mesh.select_all(action='SELECT') #모든 vertex 선택

    bpy.ops.mesh.bevel(offset=ranVal_1) # 랜덤값 1

    bpy.ops.object.mode_set(mode='OBJECT') #EDIT 모드로 변경

    bpy.ops.object.modifier_add(type='SUBSURF') # 랜덤값 2 함수로 만들어서 default값 랜덤, 아니면 해당값으로 division
    bpy.context.object.modifiers["Subdivision"].levels = ranVal_2
    bpy.context.object.modifiers["Subdivision"].render_levels = ranVal_2
    bpy.ops.object.modifier_apply(modifier="Subdivision")

def displace(ranVal_1, ranVal_2):
    #### Displace 동작 ####

    test1 = bpy.ops.object.modifier_add(type='DISPLACE') # Modifier 추가

    newTexture = bpy.data.textures.new('texture1', 'VORONOI') # data 에서 생성하기 bpy.ops.texture.new()
    bpy.data.textures["texture1"].name = "Texture" # 이름 바꿀일 있으면 바꾸기
    bpy.context.object.modifiers["Displace"].texture = bpy.data.textures["Texture"] # 텍스쳐 적용 

    bpy.data.textures["Texture"].type = 'VORONOI'
    bpy.data.textures["Texture"].distance_metric = 'DISTANCE_SQUARED'
    bpy.data.textures["Texture"].contrast = ranVal_1 # 랜덤변수 3
    bpy.data.textures["Texture"].noise_scale = ranVal_2 # 랜덤변수 4
    

    bpy.ops.object.modifier_apply(modifier="Displace")

def decimate(obj):
    #### Decimate ####

    bpy.ops.object.modifier_add(type='DECIMATE')
    size = len(obj.data.vertices)
    targetVert = random.randint(300, 400)
    targetRatio = targetVert/size
    bpy.context.object.modifiers["Decimate"].ratio = targetRatio  # 랜덤변수 5
    bpy.ops.object.modifier_apply(modifier="Decimate")
    # 현재 버텍스 수에 따라 랜덤변수의 range를 결정할것
    
def cutting(obj):
    vertCount = len(obj.data.vertices)
    bpy.ops.object.mode_set(mode='EDIT') #EDIT 모드로 변경
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.vertices_smooth(factor=0.5, repeat=1)

    for i in range(1, 10):
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_random(percent=1, seed=random.randint(1,10))
        bpy.ops.mesh.delete(type='VERT')
        if vertCount - 10 > len(obj.data.vertices):
            bpy.ops.ed.undo()
        else:
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.edge_face_add()
            if vertCount - 10 > len(obj.data.vertices):
                bpy.ops.ed.undo()
                bpy.ops.ed.undo()
            vertCount = len(obj.data.vertices)


def main():
    index = 1

    bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
    new_object = bpy.context.active_object
    new_object.name = "object" + str(index)

    ranVal_1 = random.uniform(0.4, 0.8)
    ranVal_2 = random.randint(2,4)
    subdivision(ranVal_1, ranVal_2)

    ranVal_1 = random.uniform(0.7,0.85)
    ranVal_2 = random.uniform(1.6, 2)
    displace(ranVal_1, ranVal_2)

    
    decimate(new_object)
    bpy.ops.object.mode_set(mode='EDIT') #EDIT 모드로 변경
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.vertices_smooth(factor=0.5)
    
    cutting(new_object)
    #bpy.ops.export_scene.fbx(filepath='C:\\Users\\user\\Desktop\\output\\new.fbx', object_types={'MESH'}, use_mesh_modifiers=False, add_leaf_bones=False, bake_anim=False)
if __name__ == '__main__':
    main()
