# TODO: I like this specific import - do that all over
import bpy
from bpy.types import (UIList, Panel)

class MECHANIC_BONES_UL_items(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        split = layout.split(factor=0.3)
        # split.label(item.name)
        split.prop(item, "name", emboss=False) # TODO: enable this - delete all logic dependent on name
        # split.prop(item, "length", text="length:", emboss=False)
        split.prop(item, "angle_display", text="angle:", emboss=False)
        split.prop(item, "axis", text="axis:", emboss=False)

    def invoke(self, context, event):
        pass


# TODO: not sure Mechanic_Bone_Panel is the right convention - investigate that...
# TODO: Separate those two? 
# TODO: set the list to open wider
class MECHANIC_BONES_PT_ObjectList(Panel):
    """TODO: add a meaningfull info"""
    bl_label = "Mechanic Hand Panel"
    bl_idname = "ARMATURE_PT_mechanic_bone_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Mechanic Hand"

    def draw(self, context):
        layout = self.layout
        scene = bpy.context.scene

        row = layout.row()
        row.template_list("MECHANIC_BONES_UL_items", "custom_def_list", scene, "mechanic_bones", 
            scene, "mechanic_bones_index")

        # col = row.column(align=True)
        # col.operator("mechanic_bones.list_action", icon='ADD', text="").action = 'ADD'
        # col.operator("mechanic_bones.list_action", icon='REMOVE', text="").action = 'REMOVE'
        row = layout.row()
        col = row.column(align=True)
        col.operator("mechanic_bones.clear_all", text="clear all")
        row = layout.row()
        col = row.column(align=True)
        col.operator("mechanic_bones.import_stl", text="import bones points stl")
        row = layout.row()
        col = row.column(align=True)
        col.operator("mechanic_bones.generate_bones", text="generate bones")
        row = layout.row()
        col = row.column(align=True)
        col.operator("mechanic_bones.import_device_stl", text="import device stl")


        # row = layout.row()
        # col = row.column(align=True)
        # row = col.row(align=True)
        # row.operator("custom.print_items", icon="LINENUMBERS_ON")
        # row = col.row(align=True)
        # row.operator("custom.clear_list", icon="X")


# def register():
#     bpy.utils.register_class(Mechanic_Bone_Panel)
#     bpy.types.Object.expanded = bpy.props.BoolProperty(default=True)


# def unregister():
#     bpy.utils.unregister_class(Mechanic_Bone_Panel)
#     del bpy.types.Object.expanded


# if __name__ == "__main__":
#     register()

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
#         # row.operator("mechanic_bones.clear_all", text="clear")

#         # row = layout.row()
#         # row.operator("armature.build_skeleton", text="Generate")