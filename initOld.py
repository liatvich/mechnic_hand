bl_info = {
    "name": "Build Skeleton",
    "author": "Liat V",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Armature",
    "description": "Build Skeleton",
    "warning": "",
    "wiki_url": "",
    "category": "Add Armature",
}

import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
from bpy.props import (IntProperty)


# def add_object(self, context):
#     scale_x = self.scale.x
#     scale_y = self.scale.y

#     verts = [
#         Vector((-1 * scale_x, 1 * scale_y, 0)),
#         Vector((1 * scale_x, 1 * scale_y, 0)),
#         Vector((1 * scale_x, -1 * scale_y, 0)),
#         Vector((-1 * scale_x, -1 * scale_y, 0)),
#     ]

#     edges = []
#     faces = [[0, 1, 2, 3]]

#     mesh = bpy.data.meshes.new(name="New Object Mesh")
#     mesh.from_pydata(verts, edges, faces)
#     # useful for development when the mesh may be invalid.
#     # mesh.validate(verbose=True)
#     object_data_add(context, mesh, operator=self)


class OBJECT_OT_build_skeleton(Operator, AddObjectHelper):
    """Build Skeleton"""
    bl_idname = "armature.build_skeleton"
    bl_label = "Build Skeleton"
    bl_description = "Build Skeleton"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'REGISTER', 'UNDO'}

    # scale: FloatVectorProperty(
    #     name="scale",
    #     default=(1.0, 1.0, 1.0),
    #     subtype='TRANSLATION',
    #     description="scaling",
    # )
    bones_count: bpy.props.IntProperty(
        name="number of bones",
        description="choosing the number of connected bones", default=3,
        min=1,
        max=10,
        )

    @classmethod
    def poll(cls, context):
        return True

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        # what it does
        # add_object(self, context)

        return {'FINISHED'}

# Registration
def menu_func(self, context):
    self.layout.operator(OBJECT_OT_build_skeleton.bl_idname, text="Build Skeleton")

def register():
    bpy.utils.register_class(OBJECT_OT_build_skeleton)
    bpy.types.VIEW3D_MT_armature_add.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_build_skeleton)
    bpy.types.VIEW3D_MT_armature_add.remove(menu_func)


if __name__ == "__main__":
    register()

