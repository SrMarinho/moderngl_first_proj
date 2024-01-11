#version 330

in vec3 normal;
in vec3 vertPos;

uniform vec2 u_resolution;

struct Light {
    vec3  position;
    vec3  direction;
    vec3 color;
};

void main() {
    Light light;
    vec3 color;
    vec2 u_resolution = u_resolution;
    vec3 norm = normalize(normal);
    vec3 vert = vertPos;
    vec3 fragPos = vec3(gl_FragCoord);
    vec3 fragColor = vec3(0.0);


    light.color = vec3(0, 1, 1);
    light.direction = -vec3(-1, -1, -1);

    float brightness = dot(norm, normalize(light.direction));

    color = (fragColor + brightness);

    gl_FragColor = vec4(color, 1.0);
}