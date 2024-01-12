#version 330

in vec3 normal;
in vec3 vertPos;

uniform vec2 u_resolution;
uniform float iTime;

#define ONE_OVER_GAMMA (0.45454545454545454545454545454545)

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

vec3 phong_color(
    in vec3 pixel_pos, in vec3 normal, in vec3 camera_pos,      // Scene
    in vec3 light_pos, in vec3 ambient_color,                   // Lights
    in vec3 diffuse_color, in vec3 specular_color,              // Lights
    in float shininess)                                         // Material
{   // Compute pixel color using Phong shading.  Modified from
    // https://en.wikipedia.org/wiki/Blinn%E2%80%93Phong_shading_model
    // normal must be normalized on input.  All inputs are world coords.
    // Set shininess <=0 to turn off specular highlights.
    // Objects are one-sided.

    vec3 light_dir = normalize(light_pos - pixel_pos);
    vec3 eye_dir = normalize(camera_pos - pixel_pos);

    if(dot(light_dir, eye_dir) < 0.0) {
        return ambient_color;       // Camera behind the object
    }

    float lambertian = max(0.0, dot(light_dir, normal));        // Diffuse

    float specular = 0.0;
    if((lambertian > 0.0) && (shininess > 0.0)) {               // Specular
        vec3 reflectDir = reflect(-light_dir, normal);
        float specAngle = max(dot(reflectDir, eye_dir), 0.0);
        specular = pow(specAngle, shininess);
    }
    /*
    return pow(ambient_color + lambertian*diffuse_color + specular*vec3(1.0),
                vec3(ONE_OVER_GAMMA));
        // TODO Do I need this?
    */
    lambertian = pow(lambertian, ONE_OVER_GAMMA);
    specular = pow(specular, ONE_OVER_GAMMA);

    vec3 retval = ambient_color + lambertian*diffuse_color + 
        specular*specular_color;

    return clamp(retval, 0.0, 1.0);     // no out-of-range values, please!

} //phong_color

void main() {
    Light light;
    vec3 color;
    vec2 u_resolution = u_resolution;
    vec3 norm = normalize(normal);
    vec3 vert = vertPos;
    vec3 FragPos = -vec3(gl_FragCoord);
    vec3 fragColor = vec3(1);

    light.position = vec3(5 * cos(iTime), 10, 5 * sin(iTime));
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
        specular = pow(specAngle, 32);
    }

    color = vec3(light.Ka * light.ambientColor +
            light.Kd * lambertian * light.diffuseColor +
            light.Ks * specular * light.specularColor);

    // color = vec3(light.Ks * specular * light.specularColor);

    vec3 ambient_color = vec3(0.1);
    vec3 specular_color = vec3(1.0);

    vec3 color1 = phong_color(
        vertPos, norm, vec3(0, 0, 0), light.position, 
        ambient_color, fragColor, specular_color,  // Light colors
        32);

    gl_FragColor = vec4(color1, 1.0);
}