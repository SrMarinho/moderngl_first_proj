#version 410 core

layout (location = 0) in vec3 in_normal;
layout (location = 1) in vec3 in_position;

out vec3 normal;
out vec3 vertPos;

uniform mat4 projection_matrix;

struct Obj {
    vec3 position;
    vec3 rotation;
    vec3 scale;
    vec3 axis;
};

uniform Obj obj;

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
    mat4 view = (
        translate(obj.position.x, obj.position.y, obj.position.z) *
        scale(obj.scale.x, obj.scale.y, obj.scale.z) *
        rotateZ(radians(obj.rotation.z)) *
        rotateY(radians(obj.rotation.y)) *
        rotateX(radians(obj.rotation.x)) *
        translate(obj.axis.x, obj.axis.y, obj.axis.z) *
        1
    );

    normal = mat3(transpose(inverse(view))) *  in_normal;
    vertPos = vec3(view * vec4(in_position, 1));
    gl_Position = projection_matrix * view * vec4(in_position, 1.0);

    // gl_Position = vec4(in_position, 1.0);
}