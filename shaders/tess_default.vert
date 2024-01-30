#version 410 core

layout (location = 0) in vec3 in_normal;
layout (location = 1) in vec3 in_position;

out vec3 normal;

void main()
{
    normal = in_normal;
    gl_Position = vec4(in_position, 1.0);
}