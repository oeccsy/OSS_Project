import bpy
import random

import bmesh # bmesh 오류로 인해 진행 불가능


def init_objects_data():
  for id_data in bpy.data.objects:
      bpy.data.objects.remove(id_data)

def createBottom(ranVert, index):
  bpy.ops.mesh.primitive_circle_add(vertices=ranVert, location=(0, 0, 0))
  new_object = bpy.context.active_object
  new_object.name = "object" + str(index)

  bpy.ops.object.mode_set(mode='EDIT') #EDIT 모드로 변경    
  bpy.ops.mesh.select_all(action='SELECT')
  bpy.ops.mesh.edge_face_add()

def selectNewClone(randVert, count):
  faceCount = randVert+2
  bpy.ops.object.mode_set(mode = 'OBJECT')
  obj = bpy.context.active_object
  bpy.ops.object.mode_set(mode = 'EDIT')  
  bpy.ops.mesh.select_mode(type = 'FACE')
  bpy.ops.mesh.select_all(action = 'DESELECT')
  bpy.ops.object.mode_set(mode = 'OBJECT')
  #for i in range(randVert * count, )

def setRandomPos():
  global ranX, ranY, ranZ
  ranX = random.uniform(-0.1, 0.1)
  ranY = random.uniform(-0.1, 0.1)
  ranZ = random.uniform(0.5, 1)

def setRandomValue():
  global ranVal
  ranVal = random.uniform(0.7, 1.1)

def extrude(ranVal):
  # 평면의 normal 방향으로 extrude

  bpy.ops.mesh.extrude_region_shrink_fatten(
    TRANSFORM_OT_shrink_fatten={
      "value":ranVal * 2, 
    }
  )

  # 오류
  '''
  bpy.ops.mesh.extrude_region_shrink_fatten(
    MESH_OT_extrude_region={
      "use_normal_flip":False, 
      "use_dissolve_ortho_edges":False, 
      "mirror":False}, 
    TRANSFORM_OT_shrink_fatten={
      "value":2.95368, 
      "use_even_offset":False, 
      "mirror":False, 
      "use_proportional_edit":False, 
      "proportional_edit_falloff":'SMOOTH', 
      "proportional_size":1, 
      "use_proportional_connected":False, 
      "use_proportional_projected":False, 
      "snap":False, 
      "snap_target":'CLOSEST', 
      "snap_point":(0, 0, 0), 
      "snap_align":False, 
      "snap_normal":(0, 0, 0), 
      "release_confirm":False, 
      "use_accurate":False})
  '''

  #아래는 일반 extrude
  '''
  global ranX, ranY, ranZ
  bpy.ops.mesh.extrude_region_move(
    MESH_OT_extrude_region={
      "use_normal_flip":False, 
      "use_dissolve_ortho_edges":False, 
      "mirror":False}, 
    TRANSFORM_OT_translate={
      "value":(ranX, ranY, ranZ), 
      "orient_type":'GLOBAL', 
      "orient_matrix":(
        (1, 0, 0), 
        (0, 1, 0), 
        (0, 0, 1)), 
      "orient_matrix_type":'GLOBAL', 
      "constraint_axis":(True, True, True), 
      "mirror":False, "use_proportional_edit":False, 
      "proportional_edit_falloff":'SMOOTH', 
      "proportional_size":1, 
      "use_proportional_connected":False, 
      "use_proportional_projected":False, 
      "snap":False, 
      "snap_target":'CLOSEST', 
      "snap_point":(0, 0, 0), 
      "snap_align":False, 
      "snap_normal":(0, 0, 0), 
      "gpencil_strokes":False, 
      "cursor_transform":False, 
      "texture_space":False, 
      "remove_on_cancel":False, 
      "release_confirm":False, 
      "use_accurate":False, 
      "use_automerge_and_split":False})
  '''

def rotate(ranX, ranY):
  bpy.ops.transform.rotate(value=ranX, orient_axis='X')
  bpy.ops.transform.rotate(value=ranY, orient_axis='Y')

def scaleResize(ranVal):
  bpy.ops.transform.resize(value=(ranVal, ranVal, ranVal))


def surfacePartition(ranVert, temp): # face Index 일반화 실패
  global branchList
  #face 분할
  bpy.ops.mesh.select_mode(type='FACE')
  bpy.ops.mesh.poke()

  #face 선택
  objData = bpy.data.objects['object1'].data
  curBMesh = bmesh.from_edit_mesh(objData)
  #maxIndex = len(curBMesh.faces)-1
  bpy.ops.mesh.select_all(action='DESELECT')  # 모든 face 선택 해제
  for f in curBMesh.faces[37:40]:
    f.select_set(True)                        # 합칠 face만 선택
  bmesh.update_edit_mesh(objData)             # 선택 반영(update)
  bpy.ops.mesh.edge_face_add()

  bpy.ops.mesh.select_all(action='DESELECT')
  for f in curBMesh.faces[38:41]:
    f.select_set(True)                      # 합침 왜 32번째 index로 바뀌지
  bmesh.update_edit_mesh(objData)
  bpy.ops.mesh.edge_face_add()
  
  branchList.insert(0, 38) # list 0번째 index에 추가
  branchList.insert(0, 32) # list 0번째 index에 추가
  




##### 동작 과정 ##### 
#1. ## 밑단 plane 생성 #vertex range 0:n
#2. ## 아래의 사이클 반복 vertex range 0:n / n:2n . . . 사이클 k회 반복시 최상단 kn:(k+1)n
  #2-1. ## 밑단 Extrude
  #2-2. ## 밑단 scale, #랜덤 변수 추가
  #2-3. ## 밑단 rotate, #랜덤변수 추가
#3. ## 최상단 plane 선택 후 poke 및 병합
  ## 반복 후 평면 분할
    #bpy.ops.mesh.poke()
  ## 일부 병합 
    #select, bpy.ops.mesh.edge_face_add()

if __name__ == '__main__':
    init_objects_data()

    # 만들어진 오브젝트의 수를 나타낼 변수, 오브젝트 이름 뒤에 붙는다.
    index = 1
    
    # 계산용 숫자
    temp = 0

    # 가지가 추가될 평면 list
    branchList = []

    # 랜덤 변수
    ranVert = random.randint(6,6)
    ranVal = random.uniform(0.5, 0.6)
    ranX = random.uniform(-0.1, 0.1)
    ranY = random.uniform(-0.1, 0.1)
    ranZ = random.uniform(0.5, 1)

    # object 정보


    ## 밑단 plane #vertex range 0:n
    createBottom(ranVert, index)
    extrude(ranVal+0.3)
    scaleResize(ranVal)
    rotate(ranX, ranY)
    temp += 1
    
    ### 아래는 한 사이클,
    ### ranVert = n일때, face 범위 1:(1+n) / (1+n):(1+2n) . . .  사이클 k회 반복시 1+(k)n:1+(k+1)n
    ### ranVert = 7일때, 이전단계에서 1회 반복, 현재 단계에서 5회 반복 = 총 6회 반복 -> 43:50

    for i in range(0, 5):
      ## 밑단 Extrude, rotate, #랜덤변수 추가
      setRandomValue()
      extrude(ranVal)
      scaleResize(ranVal)
      
      ## 밑단 scale, #랜덤 변수 추가
      setRandomPos()
      rotate(ranX, ranY)

      temp += 1
      
    objData = bpy.data.objects['object1'].data  
    curBMesh = bmesh.from_edit_mesh(objData)
    branch = 5
    ## 윗단 평면 분할 및 branch 추가 
    surfacePartition(ranVert, temp)
 
    ## 잔가지 insert, 잔가지 생장 끝나면 pop
    #### 오류 ####
    '''
    while True :
      for i in range(0, 5):
        setRandomValue()
        extrude(ranVal)
        scaleResize(ranVal)
        setRandomPos()
        rotate(ranX, ranY)
    
      bpy.ops.mesh.select_all(action='DESELECT')
      branchList.pop()
      if len(branchList) == 0:
        break
      else:
        nextIndex = branchList[len(branchList)-1]
        print(nextIndex)
        print(len(curBMesh.faces))
        curBMesh.faces[nextIndex].select_set(True) # 오류 -> bmesh가 아닌 bpy 활용
    '''
    

      


    #### 완성 ####
    #bpy.ops.export_scene.fbx(filepath='C:\\Users\\user\\Desktop\\output\\new.fbx', object_types={'MESH'}, use_mesh_modifiers=False, add_leaf_bones=False, bake_anim=False)
    