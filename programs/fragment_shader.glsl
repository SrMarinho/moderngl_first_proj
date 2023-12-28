#version 330

in vec3 vertPos;

uniform vec2 iResolution;
uniform float iTime;
// uniform int iFrame;

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    // vec2 pos = (fragCoord.xy * 2 / iResolution.xy) / iResolution.y;
    fragColor = vec4(1, 1, 1, 1.0);
}

void main() {
    vec2 resolution = iResolution;
    float time = iTime;
    mainImage(gl_FragColor, vec2(gl_FragCoord));
}