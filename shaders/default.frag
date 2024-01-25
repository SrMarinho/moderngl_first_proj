#version 330

in vec3 normal;
in vec3 vertPos;

uniform vec2 u_resolution;
uniform float iTime;
uniform float render_mode;

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
    vec3 fragColor = vec3(0.0);
    if (render_mode == 1.0){
        gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);
    } else {
        Light light;
        vec3 color;
        vec2 u_resolution = u_resolution;
        vec3 vert = vertPos;
        
        color += fragColor;

        light.position = vec3(5 * cos(iTime), 2, 0);
        light.ambientColor = vec3(0.1, 0.1, 0.1);
        light.diffuseColor = vec3(0.45);
        light.specularColor = vec3(0.5);
        light.specularExponent = 0;
        vec3 viewPos = vec3(0, 0, 0);
        
        color +=  illumination(light, viewPos);
        gl_FragColor = vec4(color, 1.0);
    }
}