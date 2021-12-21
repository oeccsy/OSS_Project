import Models
import Controller

while True:
    print("1. rock (low poly)")
    print("2. rock")
    print("3. tree (low poly)")

    obj_select = int(input("원하는 오브젝트 입력 (숫자로 입력) :"))
    howmany = int(input("생성하길 원하는 숫자 입력 : "))  
    if obj_select == 1 or obj_select == 2 or obj_select == 3:
        break

for i in range(1, howmany+1):
    Controller.controller.init_objects_data()
    if obj_select == 1:
        Models.rock.main()
    if obj_select == 2:
        Models.rock_high.main()
    if obj_select == 3:
        Models.tree.main()
    Controller.controller.fbx_export("object"+str(i))