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
    vec3 fragColor = vec3(1);

    light.position = vec3(1, 0, 0);
    light.direction = vec3(0, 0, -1);
    light.color = vec3(0, 1, 1);

    vec3 lightDir = normalize(light.position - fragPos);

    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * light.color;

    // float brightness = dot(norm, normalize(light.direction));

    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * light.color;

    float specularStrength = 0.5;

    vec3 viewDir = normalize(vec3(0, 0, 0) - fragPos);
    vec3 reflectDir = reflect(-lightDir, norm);

    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 64);
    vec3 specular = specularStrength * spec * light.color; 

    color = fragColor * (ambient + diffuse);

    gl_FragColor = vec4(color, 1.0);
}