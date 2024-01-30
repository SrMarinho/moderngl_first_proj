class ShaderProgram:
    def __init__(self, ctx):
        self.ctx = ctx
        self.programs = {}
        self.programs['cube'] = self.get_program('tess_default', tessellation=True)
        # self.programs['cube'] = self.get_program('default')
        self.programs['sphere'] = self.get_program('default')
        self.programs['teapot'] = self.get_program('default')
        self.programs['triangle'] = self.get_program('tess_default', tessellation=True)
        self.programs['square'] = self.get_program('tess_default', tessellation=True)

    def get_program(self, shader_program_name, tessellation=False):
        shaders = {}
        with open(f'shaders/{shader_program_name}.vert') as file:
            shaders['vertex_shader'] = file.read()
        
        if tessellation == True:
            with open(f'shaders/{shader_program_name}.vert') as file:
                shaders['vertex_shader'] = file.read()
            
            with open(f'shaders/{shader_program_name}.tc') as file:
                shaders['tess_control_shader'] = file.read()
                
            with open(f'shaders/{shader_program_name}.te') as file:
                shaders['tess_evaluation_shader'] = file.read()
                
            with open(f'shaders/{shader_program_name}.frag') as file:
                shaders['fragment_shader'] = file.read()
        else:
            with open(f'shaders/{shader_program_name}.vert') as file:
                shaders['vertex_shader'] = file.read()
            with open(f'shaders/{shader_program_name}.frag') as file:
                shaders['fragment_shader'] = file.read()
        
        

        program = self.ctx.program(**shaders)
        return program

    def destroy(self):
        [program.release() for program in self.programs.values()]