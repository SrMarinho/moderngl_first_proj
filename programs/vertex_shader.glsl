#version 330

in vec3 vert;
out vec3 vertPos;

uniform float iTime;
uniform float angle;

uniform mat4 matProj;

// uniform float znear;
// uniform float zfar;
// uniform float fovy;
// uniform float ratio;

// mat4 perspective() {
//     float zmul = (-2.0 * znear * zfar) / (zfar - znear);
//     float ymul = 1.0 / tan(fovy * 3.14159265 / 360);
//     float xmul = ymul / ratio;

//     return mat4(
//         xmul, 0.0, 0.0, 0.0,
//         0.0, ymul, 0.0, 0.0,
//         0.0, 0.0, -1.0, -1.0,
//         0.0, 0.0, zmul, 0.0
//     );
// }

vec3 multPointMatrix(vec3 i, mat4 M) 
{ 
    //out = in * Mproj;
    vec3 o;
    o.x   = i.x * M[0][0] + i.y * M[1][0] + i.z * M[2][0] + /* i.z = 1 */ M[3][0]; 
    o.y   = i.x * M[0][1] + i.y * M[1][1] + i.z * M[2][1] + /* i.z = 1 */ M[3][1]; 
    o.z   = i.x * M[0][2] + i.y * M[1][2] + i.z * M[2][2] + /* i.z = 1 */ M[3][2]; 
    float w = i.x * M[0][3] + i.y * M[1][3] + i.z * M[2][3] + /* i.z = 1 */ M[3][3]; 
 
    // normalize if w is different than 1 (convert from homogeneous to Cartesian coordinates)
    if (w != 0) { 
        o.x /= w; 
        o.y /= w; 
        o.z /= w; 
    }

    return o; 
} 
vec4 perspective(mat4 m, vec4 i) {
    vec4 o = m * i;

    if (o.w != 0) { 
        o.x /= o.w; 
        o.y /= o.w; 
        o.z /= o.w; 
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
    float fTheta = radians(angle);
    vec4 vertex = vec4(vert, 1.0);
    float scale = 2;
    float time = iTime;


    vertex *= translate(0, 0, -0.5);
    vertex *= rotateX(angle);
    vertex = vec4(multPointMatrix(vec3(vertex), matProj), 1.0);

    gl_Position = vertex;
}