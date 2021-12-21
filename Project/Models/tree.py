import bpy
import random

def init_objects_data():
  for id_data in bpy.data.objects:
      bpy.data.objects.remove(id_data)

def aaaa():
  print("aaaa")

def createBottom(ranVert, objIndex):
  bpy.ops.mesh.primitive_circle_add(vertices=ranVert, location=(0, 0, 0))
  new_object = bpy.context.active_object
  new_object.name = "object" + str(objIndex)

  bpy.ops.object.mode_set(mode='EDIT') #EDIT 모드로 변경    
  bpy.ops.mesh.select_all(action='SELECT')
  bpy.ops.mesh.edge_face_add()

  return new_object


def duplicateMove(ranX, ranY, ranZ): #자동으로 new Clone 선택됨
  bpy.ops.mesh.duplicate_move(TRANSFORM_OT_translate={"value":(ranX, ranY, ranZ)})


def objChanage():
  #Object 모드에서 사용할 object 선택
  bpy.ops.object.mode_set(mode = 'OBJECT')
  obj = bpy.context.active_object #현재 선택된 오브젝트
  
  #Edit 모드 진입
  bpy.ops.object.mode_set(mode = 'EDIT')  


def selectNewClone(obj, randVert, cloneIndex): #Edit 모드에서 사용
  faceCount = randVert+2

  bpy.ops.mesh.select_mode(type = 'FACE')
  bpy.ops.mesh.select_all(action = 'DESELECT')

  #Object 모드에서 선택할 faces 선택
  bpy.ops.object.mode_set(mode = 'OBJECT')
  for i in range(faceCount * cloneIndex, faceCount * (cloneIndex+1)):
    obj.data.polygons[i].select = True
  
  #Edit 모드 진입
  bpy.ops.object.mode_set(mode = 'EDIT')


def selectTopOrBottom(obj, randVert, cloneIndex, isTop):
  faceCount = randVert+2
  if isTop :
    index = (faceCount * cloneIndex) + 1
  else :
    index = (faceCount * cloneIndex)

  bpy.ops.mesh.select_mode(type = 'FACE')
  bpy.ops.mesh.select_all(action = 'DESELECT')

  bpy.ops.object.mode_set(mode = 'OBJECT')
  obj.data.polygons[index].select = True
  
  bpy.ops.object.mode_set(mode = 'EDIT')


def setRandomXYZ():
  global ranX, ranY, ranZ
  ranX = random.uniform(-0.1, 0.1)
  ranY = random.uniform(-0.1, 0.1)
  ranZ = random.uniform(0.6, 0.9)

def setRandomValue():
  global ranVal
  ranVal = random.uniform(0.7, 1.1)

def extrudeNormal(ranVal):
  # 평면의 normal 방향으로 extrude

  bpy.ops.mesh.extrude_region_shrink_fatten(
    TRANSFORM_OT_shrink_fatten={
      "value":ranVal, 
    }
  )

def rotate(ranX=0, ranY=0, ranZ=0):
  bpy.ops.transform.rotate(value=ranX, orient_axis='X')
  bpy.ops.transform.rotate(value=ranY, orient_axis='Y')
  bpy.ops.transform.rotate(value=ranZ, orient_axis='Z')

def tranlate(ranX=0, ranY=0, ranZ=0):
  bpy.ops.transform.translate(value=(ranX, ranY, ranZ))

def scaleResize(valX=1, valY=1, valZ=1):
  bpy.ops.transform.resize(value=(valX, valY, valZ))

def inset(ranVal):
  bpy.ops.mesh.inset(thickness=ranVal, depth=0)

def finalScale():
  bpy.ops.mesh.select_all(action='SELECT')
  ranVal = random.uniform(0.5, 1)
  bpy.ops.transform.resize(value=(ranVal, ranVal, ranVal))
  

def main():
    # 만들어진 오브젝트의 수를 나타낼 변수, 오브젝트 이름 뒤에 붙는다.
    objIndex = 1
    
    # 현재 사용하는 clone
    cloneIndex = 0

    # 랜덤 변수
    ranVert = random.randint(6,6) #(5,7)
    ranVal = random.uniform(0.5, 0.6)
    ranX = random.uniform(-0.1, 0.1)
    ranY = random.uniform(-0.1, 0.1)
    ranZ = random.uniform(0.7, 1.2)

    ## 나무 뿌리 생성
    obj = createBottom(ranVert, objIndex)
    extrudeNormal(ranVal * 3)
    scaleResize(ranVal, ranVal, ranVal)
    rotate(ranX, ranY)


    

    ## 첫번째 clone 생성
    bpy.ops.mesh.select_all(action='SELECT')
    rotate(0, 3.14) # 블렌더에서 실행한것과 다름 -> cmd에서 실행시 보정 해줘야함 블렌더에서 실행시 해당 코드 지움
    duplicateMove(ranX, ranY, ranZ)
    cloneIndex += 1
    ranVal = random.uniform(1.7, 2)
    scaleResize(ranVal, ranVal)

    # clone 추가 생성
    for i in range(2,5):
      setRandomXYZ()
      duplicateMove(ranX, ranY, ranZ)
      cloneIndex += 1
      setRandomXYZ()
      rotate(ranX, ranY, ranZ)
      ranVal = random.uniform(0.85, 0.9)
      scaleResize(ranVal, ranVal, ranVal)
    
    # Top scale 변경
    for i in range(1, 5):
      selectTopOrBottom(obj, ranVert, i, True)
      ranVal = random.uniform(0.2, 0.5)
      scaleResize(ranVal, ranVal, ranVal)

    # Bottom inset 적용
    for i in range(1, 5):
      selectTopOrBottom(obj, ranVert, i, False)
      ranVal = random.uniform(0.2, 0.5)
      inset(ranVal)
      ranVal = random.uniform(0.1, 0.3)
      extrudeNormal(-ranVal) # Bottom이므로 음수처리

    #finalScale()

    #### 완성 ####
    #bpy.ops.export_scene.fbx(filepath='C:\\Users\\user\\Desktop\\output\\new.fbx', object_types={'MESH'}, use_mesh_modifiers=False, add_leaf_bones=False, bake_anim=False)


if __name__ == '__main__':
    main()

