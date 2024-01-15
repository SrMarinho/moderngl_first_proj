#version 330

in vec3 normal;
in vec3 vertPos;

uniform vec2 u_resolution;
uniform float iTime;

struct Light {
    vec3  position;
    vec3  direction;

    vec3 ambientColor;
    vec3 diffuseColor;
    vec3 specularColor;

    float specularExponent;
};

vec3 illumination(Light L, vec3 viewPos) {
    vec3 ambient = L.ambientColor;

    vec3 norm = normalize(normal);

    vec3 lightDir = normalize(L.position - vertPos);

    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * L.diffuseColor;

    float specularStrength = 0.5;

    vec3 viewDir = normalize(viewPos - vertPos);
    vec3 reflectDir = reflect(-lightDir, norm);

    float spec = pow(max(dot(viewDir, reflectDir), 0.0), L.specularExponent);
    vec3 specular = specularStrength * spec * L.specularColor;

    return ambient + diffuse + specular;
}

void main() {
    Light light;
    vec3 color;
    vec2 u_resolution = u_resolution;
    vec3 vert = vertPos;
    vec3 fragColor = vec3(0.15, 0.09, 0.64);

    light.position = vec3(10 * cos(iTime), 10, 10 * sin(iTime));
    light.ambientColor = vec3(0.1, 0.1, 0.1);
    light.diffuseColor = vec3(0, 0.5, 1);
    light.specularColor = vec3(0.4, 0.4, 0.4);
    light.specularExponent = 32;

    vec3 viewPos = vec3(0, 0, 0);
    // color =  fragColor + illumination(light, viewPos);
    color = fragColor;

    gl_FragColor = vec4(color, 1.0);
}