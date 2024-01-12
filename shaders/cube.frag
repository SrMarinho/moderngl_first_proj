#version 330

in vec3 normal;
in vec3 vertPos;

uniform vec2 u_resolution;

struct Light {
    vec3  position;
    vec3  direction;
    vec3 color;

    float Ka;
    float Kd;
    float Ks;

    vec3 ambientColor;
    vec3 diffuseColor;
    vec3 specularColor;
};

void main() {
    Light light;
    vec3 color;
    vec2 u_resolution = u_resolution;
    vec3 norm = normalize(normal);
    vec3 vert = vertPos;
    vec3 FragPos = -vec3(gl_FragCoord);
    vec3 fragColor = vec3(1);

    light.position = vec3(5, 0, 5);
    light.direction = vec3(1, 1, 0);
    light.color = vec3(0, 1, 1);
    light.Ka = 0.1;
    light.Kd = 0.5;
    light.Ks = 0.5;
    light.ambientColor = vec3(0, 0, 1);
    light.diffuseColor = vec3(1, 1, 0);
    light.specularColor = vec3(1, 1, 1);

    vec3 N = norm;
    vec3 L = normalize(light.position - vertPos);

    // Lambert's cosine law
    float lambertian = max(dot(N, L), 0.0);
    float specular = 0.0;
    if(lambertian > 0.0) {
        vec3 R = reflect(-L, N);      // Reflected light vector
        vec3 V = normalize(-vertPos); // Vector to viewer
        // Compute the specular term
        float specAngle = max(dot(R, V), 0.0);
        specular = pow(specAngle, 64);
    }

    color = vec3(light.Ka * light.ambientColor +
            light.Kd * lambertian * light.diffuseColor +
            light.Ks * specular * light.specularColor);

    gl_FragColor = vec4(color, 1.0);
}