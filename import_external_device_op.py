# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
import os
import bpy
import io_mesh_stl.stl_utils
from bpy.props import (
        StringProperty,
        BoolProperty,
        CollectionProperty,
        EnumProperty,
        FloatProperty,
        )
from bpy_extras.io_utils import (
        ImportHelper,
        )
from bpy.types import (
        Operator,
        OperatorFileListElement,
        )
# from mathutils import Matrix
# from stl import mesh

class Import_device_STL_Mechanic_Operator(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "mechanic_bones.import_device_stl"
    bl_label = "Import Device STL"

    filename_ext = ".stl"

    filter_glob = StringProperty(
            default="*.stl",
            options={'HIDDEN'},
            )
    files = CollectionProperty(
            name="File Path",
            type=OperatorFileListElement,
            )
    directory = StringProperty(
            subtype='DIR_PATH',
            )

    global_scale = FloatProperty(
            name="Scale",
            soft_min=0.001, soft_max=1000.0,
            min=1e-6, max=1e6,
            default=1.0,
            )

    use_scene_unit = BoolProperty(
            name="Scene Unit",
            description="Apply current scene's unit (as defined by unit scale) to imported data",
            default=False,
            )

    use_facet_normal = BoolProperty(
            name="Facet Normals",
            description="Use (import) facet normals (note that this will still give flat shading)",
            default=False,
            )

    def __init__(self):
        self.device_meshes_name = []
        self.device_meshes = []

    def createMesh(self, name, verts, edges, faces, context):
        add_mesh = bpy.data.meshes.new(name)     # Create mesh and object
        ob = bpy.data.objects.new(name, add_mesh)
        bpy.context.collection.objects.link(ob)
        add_mesh.from_pydata(verts, edges, faces)
        add_mesh.update(calc_edges=True)    # Update mesh with new data
        # add_mesh.transform(Matrix.Scale(0.1, 4, (1, 1, 1)))
        if name[0].isnumeric():
            # if int(name[0]) not in self.device_meshes:
            #     self.device_meshes[int(name[0])] = []
            mesh_data = {'group_index': int(name[0]), 'vertices_count': add_mesh.vertices.__len__()}
            self.device_meshes.append(mesh_data)
        else:
            mesh_data = {'group_index': -1, 'vertices_count': add_mesh.vertices.__len__()}
            self.device_meshes.append(mesh_data)
        return ob

    def load_stl(self, file, name, context):
        # change to blender unit to match the stl file  
        # we can do that in a diffrent way 
        # like set it from the addon
        bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'
        bpy.context.scene.unit_settings.scale_length = 0.001
        bpy.context.space_data.clip_end = 10000
        bpy.context.space_data.overlay.grid_scale = 0.001

        tris, tri_nors, pts = io_mesh_stl.stl_utils.read_stl(file)

        self.createMesh(name.split('.')[0], pts, [], tris, context)
        self.device_meshes_name.append(name.split('.')[0])
    
    def select_activate(self, obj):
        try:
            bpy.ops.object.mode_set(mode="OBJECT")
            bpy.ops.object.select_all(action='DESELECT')
        except RuntimeError:
            pass
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

    def select_device_meshses(self):
        for mesh_name in self.device_meshes_name[1:]:
            bpy.data.objects[mesh_name].select_set(True)

    def get_joined_mesh_index(self, vertice):
        for mesh_vertice in bpy.data.meshes[0].vertices:
            if mesh_vertice.co == vertice.co:
                return mesh_vertice.index
        return 0

    def execute(self, context):
        self.device_meshes_name = []
        self.device_meshes = []
        for file in self.files: 
            path = os.path.join(self.directory, file.name)
            self.load_stl(path, file.name, context)

        # joining into one device
        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        self.select_activate(bpy.data.objects[self.device_meshes_name[0]])
        self.select_device_meshses()
        bpy.ops.object.join()
        
        # Auto weights - ti generate vertex groups - here we create the automatic + vertex group
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[self.device_meshes_name[0]].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects[bpy.context.scene.mechanic_hand_armature.name]
        bpy.ops.object.parent_set(type='ARMATURE_AUTO')

        # now we will connect the bones to its correct (not automatic affected parts)
        vertices_count_insert = 0
        for group in bpy.data.objects[0].vertex_groups:
            vertices_count_all = 0
            for meshes_data in self.device_meshes:
                # if meshes_data['mesh'].name == '1 Base':
                #     continue
                if int(group.name) == meshes_data['group_index']:
                    for curr_vertice_index in range(meshes_data['vertices_count']):
                        group.add([vertices_count_insert],1.0,'REPLACE')
                        vertices_count_insert = vertices_count_insert + 1
                        vertices_count_all = vertices_count_all + 1
                else:
                    for curr_vertice_index in range(meshes_data['vertices_count']):
                        group.add([vertices_count_all],0.0,'REPLACE')
                        vertices_count_all = vertices_count_all + 1
        
        bpy.context.object.data.show_axes = True
        bpy.context.object.show_in_front = True

        return {'FINISHED'}
