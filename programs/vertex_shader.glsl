#version 330

in vec3 vert;
out vec3 vertPos;

uniform float iTime;

uniform mat4 matProj;

vec3 mult3x4(vec3 v, mat4 m)
{
    vec3 u;
    u.x = m[0].x * v.x + m[1].x * v.y + m[2].x * v.z;
    u.y = m[0].y * v.x + m[1].y * v.y + m[2].y * v.z;
    u.z = m[0].z * v.x + m[1].z * v.y + m[2].z * v.z;
    float w = v.x * m[0][3] + v.y * m[1][3] + v.z * m[2][3] + m[3][3];
    if (w != 0.0)
    {
        u.x /= w;
        u.y /= w;
        u.z /= w;
    }
    return u;
}

vec3 mult3x3(vec3 v, mat3 m)
{
    vec3 u;
    u.x = m[0].x * v.x + m[1].x * v.y + m[2].x * v.z;
    u.y = m[0].y * v.x + m[1].y * v.y + m[2].y * v.z;
    u.z = m[0].z * v.x + m[1].z * v.y + m[2].z * v.z;
    return u;
}

vec3 rotateX(vec3 v, float angle)
{
    vec3 vr;
    mat3 rotxMatrix = mat3(0.0);
    rotxMatrix[0][0]  = 1;
    rotxMatrix[1][1]  = cos(angle);
    rotxMatrix[2][1]  = -sin(angle);
    rotxMatrix[1][2]  = sin(angle);
    rotxMatrix[2][2]  = cos(angle);

    vr = mult3x3(v, rotxMatrix);

    return vr;
}

vec3 rotateY(vec3 v, float angle)
{
    vec3 vr;
    mat3 rotxMatrix = mat3(0.0);
    rotxMatrix[0][0]  = 1;
    rotxMatrix[1][1]  = cos(angle);
    rotxMatrix[2][1]  = -sin(angle);
    rotxMatrix[1][2]  = sin(angle);
    rotxMatrix[2][2]  = cos(angle);

    vr = mult3x3(v, rotxMatrix);

    return vr;
}

vec3 translate3d(vec3 v, vec3 t)
{
    vec3 u;
    u.x = v.x + t.x;
    u.y = v.y + t.y;
    u.z = v.z + t.z;

    return u;
}

vec3 rotateZ(vec3 v, float angle)
{
    vec3 vr;
    mat3 rotxMatrix = mat3(0.0);
    rotxMatrix[0][0]  = 1;
    rotxMatrix[1][1]  = cos(angle);
    rotxMatrix[2][1]  = -sin(angle);
    rotxMatrix[1][2]  = sin(angle);
    rotxMatrix[2][2]  = cos(angle);

    vr = mult3x3(v, rotxMatrix);

    return vr;
}

void main()
{
    mat4 aaaMatProj = matProj;
    vec3 vertex;

    vertex = translate3d(vert, vec3(-0.75, 0, 0));
    vertex = rotateX(vertex,  iTime);
    vertex = mult3x4(vertex, matProj);
    vertPos = vertex;
    gl_Position = vec4(vertex, 1.0);
}