class ShaderProgram:
    def __init__(self, ctx):
        self.ctx = ctx
        self.programs = {}
        self.programs['cube'] = self.get_program('default')
        self.programs['sphere'] = self.get_program('default')
        self.programs['teapot'] = self.get_program('default')

    def get_program(self, shader_program_name, tessellation=True):
        shaders = {
            'vertex_shader': None,
            'tess_control_shader': None,
            'tess_evaluation_shader': None,
            'fragment_shader': None,
        }
        with open(f'shaders/{shader_program_name}.vert') as file:
            shaders['vertex_shader'] = file.read()
        
        if tessellation == True:
            with open(f'shaders/{shader_program_name}.tc') as file:
                shaders['tess_control_shader'] = file.read()
                
            with open(f'shaders/{shader_program_name}.te') as file:
                shaders['tess_evaluation_shader'] = file.read()

        with open(f'shaders/{shader_program_name}.frag') as file:
            shaders['fragment_shader'] = file.read()
        
        

        program = self.ctx.program(**shaders)
        return program

    def destroy(self):
        [program.release() for program in self.programs.values()]