#version 330

in vec3 vert;
out vec3 vertPos;

uniform float iTime;
uniform float angle;

uniform mat4 matProj;

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
    rotxMatrix[1][2]  = -sin(angle);
    rotxMatrix[2][1]  = sin(angle);
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

vec3 rotateZ(vec3 v, float angle)
{
    vec3 vr;
    mat3 rotxMatrix = mat3(0.0);
    rotxMatrix[0][0]  = 1;
    rotxMatrix[1][1]  = cos(angle);
    rotxMatrix[2][1]  = -sin(angle);
    rotxMatrix[1][2]  = sin(angle);
    rotxMatrix[2][2]  = cos(angle);

    vr = mult3x33(v, rotxMatrix);

    return vr;
}

mat4 translate(float x, float y, float z)
{
    return mat4(
        vec4(1.0, 0.0, 0.0, x ),
        vec4(0.0, 1.0, 0.0, y ),
        vec4(0.0, 0.0, 1.0, z ),
        vec4(0.0, 0.0, 0.0, 1.0 )
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
    mat4 aaaMatProj = matProj;
    float fTheta = radians(angle * 30);
    vec4 vertex = vec4(vert, 1.0);
    float size = 0.2;
    float time = iTime;

    mat4 transformations = translate(-0.5, -0.5, -0.5) * rotateY(fTheta) /* * rotateX(fTheta)*/;
    vertex = multM4V4(transformations, vertex);
    vertex = multM4V4(matProj, vertex) * scale(size, size, size);

    if (vertex[3] != 0) {
        vertex[0] /= vertex[3];
        vertex[1] /= vertex[3];
        vertex[2] /= vertex[3];
    }

    // vertex = multM4V4(scale(size, size, size), vertex);

    gl_Position = vertex;
}