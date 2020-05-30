import bpy

# TODO: not sure Mechanic_Bone_Panel is the right convention - investigate that...
class Mechanic_Bone_Panel(bpy.types.Panel):
    """TODO: add a meaningfull info"""
    bl_label = "Single Mechanic Bone Panel"
    bl_idname = "ARMATURE_PT_mechanic_bone_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Skeleton"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        box = layout.box()
        row = box.row()
        row.prop(obj, "expanded",
            icon="TRIA_DOWN" if obj.expanded else "TRIA_RIGHT",
            icon_only=True, emboss=False
        )
        row.label(text="Active object is: " + obj.name)

        if obj.expanded:
            row = box.row()
            row.prop(obj, "name")

            row = box.row()
            row.label(text="Hello world!", icon='WORLD_DATA')

            row = box.row()
            row.operator("mesh.primitive_cube_add")


def register():
    bpy.utils.register_class(Mechanic_Bone_Panel)
    bpy.types.Object.expanded = bpy.props.BoolProperty(default=True)


def unregister():
    bpy.utils.unregister_class(Mechanic_Bone_Panel)
    del bpy.types.Object.expanded


if __name__ == "__main__":
    register()

# import bpy
# from bpy.types import Panel

# class Mechanic_Bone_Panel(Panel):
#     bl_space_type = "VIEW_3D"
#     bl_region_type = "UI"
#     bl_label = "Single Mechanic Bone Panel"
#     bl_category = "Skeleton"

#     def draw(self, context):
#         # change the mechanical bone name - Mechanic bone + index number - set as global. 
#             #  +  X - delete button
#         # change length
#         # change angle

#         # layout = self.layout
#         # box() // every sun panel should be a box 
#         # row = layout.row()
#         # col = row.column()
#         # col.label(text="Tab Label:")
#         # col.prop(self, "tab_label", text="")

#         # row.prop(context.scene, "bones_count", text="Number of bones")

#         # row = layout.row()
#         # row.operator("object.clear_all", text="clear")

#         # row = layout.row()
#         # row.operator("armature.build_skeleton", text="Generate")