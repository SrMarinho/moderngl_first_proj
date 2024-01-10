#version 330

layout (location = 0) in vec3 in_normal;
layout (location = 1) in vec3 in_position;

out vec3 normal;
out vec3 vertPos;

struct Obj {
    vec3 position;
    vec3 rotation;
    vec3 scale;
};

uniform Obj obj;

uniform float iTime;

uniform mat4 m_proj;

vec4 multM4V4(mat4 m, vec4 v) 
{ 
    vec4 o;
    
    for(int row = 0; row < 4; row++){
        for(int col = 0; col < 4; col++){
            o[row] += m[row][col] * v[col];
        }    
    }

    return o; 
}

vec3 mult3x33(vec3 v, mat3 m)
{
    vec3 u;
    u.x = m[0][0] * v.x + m[0][1] * v.y + m[0][2] * v.z;
    u.y = m[1][0] * v.x + m[1][1] * v.y + m[1][2] * v.z;
    u.z = m[2][0] * v.x + m[2][1] * v.y + m[2][2] * v.z;
    return u;
}

mat4 rotateX(float angle)
{
    mat4 rotxMatrix = mat4(0.0);
    rotxMatrix[0][0]  = 1;
    rotxMatrix[1][1]  = cos(angle);
    rotxMatrix[2][1]  = -sin(angle);
    rotxMatrix[1][2]  = sin(angle);
    rotxMatrix[2][2]  = cos(angle);
    rotxMatrix[3][3]  = 1;

    return rotxMatrix;
}

mat4 rotateY(float angle)
{
    mat4 rotxMatrix = mat4(0.0);
    rotxMatrix[0][0]  = cos(angle);
    rotxMatrix[0][2]  = sin(angle);
    rotxMatrix[1][1]  = 1;
    rotxMatrix[2][0]  = -sin(angle);
    rotxMatrix[2][2]  = cos(angle);
    rotxMatrix[3][3]  = 1;

    return rotxMatrix;
}

mat4 rotateZ(float angle)
{
    mat4 rotxMatrix = mat4(0.0);
    rotxMatrix[0][0]  = cos(angle);;
    rotxMatrix[1][0]  = -sin(angle);
    rotxMatrix[0][1]  = sin(angle);
    rotxMatrix[1][1]  = cos(angle);
    rotxMatrix[2][2]  = 1;
    rotxMatrix[3][3]  = 1;

    return rotxMatrix;
}

mat4 translate(float x, float y, float z)
{
    return mat4(
        vec4(1.0, 0.0, 0.0, 0.0 ),
        vec4(0.0, 1.0, 0.0, 0.0),
        vec4(0.0, 0.0, 1.0, 0.0 ),
        vec4(x, y, z, 1.0 )
    );
}


mat4 scale(float x, float y, float z)
{
    return mat4(
        vec4(  x, 0.0, 0.0, 0.0 ),
        vec4(0.0,   y, 0.0, 0.0 ),
        vec4(0.0, 0.0,   z, 0.0 ),
        vec4(0.0, 0.0, 0.0, 1.0 )
    );
}

void main()
{

    mat4 aaaaproj = m_proj;
    Obj aaaaobj = obj;
    
    float time = iTime;

    vec4 vertex = vec4(in_position, 1.0);

    mat4 model_transforms = (
        translate(obj.position.x, obj.position.y, obj.position.z - 0.5) *
        scale(obj.scale.x, obj.scale.y, obj.scale.z) *
        rotateZ(radians(obj.rotation.z)) *
        rotateY(radians(obj.rotation.y)) *
        rotateX(radians(obj.rotation.x)) *
        translate(-0.5, -0.5, -0.5) *
        1
    );

    vertex = (
        m_proj *
        model_transforms *
        vertex
    );

    model_transforms = transpose(inverse(model_transforms));
    normal = vec3(
        model_transforms *
        vec4(in_normal, 1.0)
    );

    vertPos = in_position;
    
    gl_Position = vertex;
}