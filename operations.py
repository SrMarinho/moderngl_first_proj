import numpy as np

def create_perspective_matriz(fov, aspect_ratio, near_plane, far_plane):
    tan_half_fovy = np.tan(np.radians(fov * 0.5))
    return np.array([
        [1 / (aspect_ratio * tan_half_fovy), 0.0, 0.0, 0.0],
        [0.0, 1 / (tan_half_fovy), 0.0, 0.0],
        [0.0, 0.0, -(far_plane + near_plane) / (far_plane - near_plane), -1],
        [0.0, 0.0, -(2 * far_plane * near_plane) / (far_plane - near_plane), 0.0]
    ])