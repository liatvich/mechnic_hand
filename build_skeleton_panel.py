import bpy
from bpy.types import Panel

class Build_Skeleton_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Build Skeleton"
    bl_category = "Skeleton"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.prop(context.scene, "bones_count", text="Number of bones")

        row = layout.row()
        row.operator("object.clear_all", text="clear")

        # row = layout.row()
        # row.operator("armature.build_skeleton", text="Generate")

        row = layout.row()
        row.operator("armature.add_mechanic_bone", text="Add new mechanic bone")

        box = layout.box()
        row = box.row()
        row.prop(context.object, "expanded",
            icon="TRIA_DOWN" if context.object.expanded else "TRIA_RIGHT",
            icon_only=True, emboss=False
        )
        row.label(text="Active object is: " + context.object.name)

        if context.object.expanded:
            row = box.row()
            row.prop(context.object, "name")

            row = box.row()
            row.label(text="Hello world!", icon='WORLD_DATA')

            row = box.row()
            row.operator("mesh.primitive_cube_add")

