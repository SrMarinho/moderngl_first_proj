#version 330

in vec4 vertPos;

uniform vec2 iResolution;
uniform float iTime;
// uniform int iFrame;

void mainImage(out vec4 fragColor, in vec3 fragCoord) {
    // vec2 pos = (fragCoord.xy * 2 / iResolution.xy) / iResolution.y;
    float depth = fragCoord.z / vertPos.w;
    fragColor = vec4(1 * depth, 1 * depth, 1 * depth, 1.0);
}

void main() {
    vec2 resolution = iResolution;
    float time = iTime;
    mainImage(gl_FragColor, vec3(gl_FragCoord));
}