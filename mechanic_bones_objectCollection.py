import bpy
from bpy.types import (PropertyGroup,
                       Bone)
from bpy.props import (StringProperty, 
                        FloatProperty,
                        PointerProperty, 
                        EnumProperty, 
                        BoolProperty)

# Enum property.
axis_enum = [
    ("X", "x", "", 0),
    ("Y", "y", "", 1),
    ("Z", "z", "", 2),
]

def get_axis_enum(self, context): 
    curr_axis_enum = []
    if not self.x_limit:
        curr_axis_enum.append(("X", "x", "", 0))
    if not self.y_limit:
        curr_axis_enum.append(("Y", "y", "", 1))
    if not self.z_limit:
        curr_axis_enum.append(("Z", "z", "", 2))
    return curr_axis_enum

def update_bone_length(self, context):
    context.object.pose.bones[self.name].scale[1] = self.length

def update_bone_angle(self, context):
    a, b, c, axis_variable = [item for item in axis_enum if self.axis in item][0]
    bpy.context.object.pose.bones[self.name].rotation_mode = 'XYZ'

    if self.axis == 'X':
        if not self.x_limit:
            context.object.pose.bones[self.name].rotation_euler[axis_variable] = self.angle_display
            self.angle_x = self.angle_display
        else: 
            self.angle_x = 0.0
            self.angle_display = 0.0
    elif self.axis == 'Y':  
        if not self.y_limit:
            context.object.pose.bones[self.name].rotation_euler[axis_variable] = self.angle_display
            self.angle_y = self.angle_display 
        else: 
            self.angle_y = 0.0
            self.angle_display = 0.0
    elif self.axis == 'Z':
        if not self.z_limit:
            context.object.pose.bones[self.name].rotation_euler[axis_variable] = self.angle_display
            self.angle_z = self.angle_display
        else: 
            self.angle_z = 0.0
            self.angle_display = 0.0

def update_axis(self, context):
    if self.axis == 'X':
        self.angle_display = self.angle_x

        #TODO: super ugly unify!
        # changing constraint
        if context.mode != 'POSE':
            bpy.ops.object.mode_set(mode='POSE')

        # try:
        #     bpy.context.object.pose.bones[self.name].constraints.remove(bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"])
        # except: 
        #     pass
        # bpy.context.object.pose.bones[self.name].constraints.new('LIMIT_ROTATION')
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_x = False
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_y = True
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].max_y = self.angle_y
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].min_y = self.angle_y
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_z = True
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].max_z = self.angle_z
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].min_z = self.angle_z
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].owner_space = 'LOCAL'
        # bpy.context.object.pose.bones[self.name].rotation_mode = 'XYZ'

    elif self.axis == 'Y':
        self.angle_display  = self.angle_y

        # changing constraint
        if context.mode != 'POSE':
            bpy.ops.object.mode_set(mode='POSE')

        # try:
        #     bpy.context.object.pose.bones[self.name].constraints.remove(bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"])
        # except: 
        #     pass
        # bpy.context.object.pose.bones[self.name].constraints.new('LIMIT_ROTATION')
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_x = True
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].max_x = self.angle_x
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].min_x = self.angle_x
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_y = False
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_z = True
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].max_z = self.angle_z
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].min_z = self.angle_z
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].owner_space = 'LOCAL'
        # bpy.context.object.pose.bones[self.name].rotation_mode = 'XYZ'
    elif self.axis == 'Z':
        self.angle_display = self.angle_z

        # changing constraint
        if context.mode != 'POSE':
            bpy.ops.object.mode_set(mode='POSE')

        # try:
        #     bpy.context.object.pose.bones[self.name].constraints.remove(bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"])
        # except: 
        #     pass
        # bpy.context.object.pose.bones[self.name].constraints.new('LIMIT_ROTATION')
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_x = True
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].max_x = self.angle_x
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].min_x = self.angle_x
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_y = True
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].max_y = self.angle_y
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].min_y = self.angle_y
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_z = False
        # bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].owner_space = 'LOCAL'
        # bpy.context.object.pose.bones[self.name].rotation_mode = 'XYZ'

class MECHANIC_BONES_objectCollection(PropertyGroup):
    name: StringProperty()
    angle_display: FloatProperty(default=0.0, subtype='ANGLE', update=update_bone_angle)
    angle_x: FloatProperty(default=0.0, subtype='ANGLE')
    angle_y: FloatProperty(default=0.0, subtype='ANGLE')
    angle_z: FloatProperty(default=0.0, subtype='ANGLE')
    length: FloatProperty(default=1, min=0.0, soft_min=0, update=update_bone_length)
    axis: EnumProperty(items=get_axis_enum, name='axis', update=update_axis)
    x_limit: BoolProperty(name='axis_x', default=False)
    y_limit: BoolProperty(name='axis_y', default=False)
    z_limit: BoolProperty(name='axis_z', default=False)
