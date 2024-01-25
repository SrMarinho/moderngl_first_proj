from vbo import VBO
from shader_program import ShaderProgram
import moderngl as mgl

class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['cube'],
            vbo = self.vbo.vbos['cube'])
        
        self.vaos['sphere'] = self.get_vao(
            program=self.program.programs['sphere'],
            vbo = self.vbo.vbos['sphere'])

        self.vaos['teapot'] = self.get_vao(
            program=self.program.programs['teapot'],
            vbo = self.vbo.vbos['teapot'])

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()