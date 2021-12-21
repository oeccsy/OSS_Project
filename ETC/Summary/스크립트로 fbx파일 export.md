# [스크립트로 fbx 파일 export]

`bpy.ops.export_scene.fbx()` 를 이용한다.

Sample Code에는 자주 사용하는 설정으로 해두었다.

filepath는 문자열이기 때문에 \이 아닌 \\\으로 나타내야함에 주의한다.  

ex) `bpy.ops.export_scene.fbx(filepath='C:\\Users\\test.fbx')`

### [참고링크]

- [https://docs.blender.org/api/current/bpy.ops.export_scene.html](https://docs.blender.org/api/current/bpy.ops.export_scene.html)
- [https://blenderartists.org/t/how-to-export-mesh-object-to-fbx-from-command-line/1144571](https://blenderartists.org/t/how-to-export-mesh-object-to-fbx-from-command-line/1144571)