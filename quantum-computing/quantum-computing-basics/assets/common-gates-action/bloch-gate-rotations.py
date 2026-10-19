"""X, H, S, T and Rz as rotations of the Bloch vector.

Render from this folder:
    uvx --python 3.14 manimgx@0.1.1 render bloch-gate-rotations.py -o bloch-gate-rotations.mp4 -r 1280x720 --fps 30
"""

import numpy as np
import manimgx as m

PHI, THETA = 70 * m.DEGREES, -60 * m.DEGREES
R = 2.0
X, Y, Z = np.array([1.0, 0, 0]), np.array([0, 1.0, 0]), np.array([0, 0, 1.0])

# (title, start vector, rotation axis, angle)
GATES = [
    (r"X:\ \pi \text{ about } \hat{x},\ \lvert 0\rangle \to \lvert 1\rangle", Z, X, np.pi),
    (r"H:\ \pi \text{ about } (\hat{x}+\hat{z})/\sqrt{2},\ \lvert 0\rangle \to \lvert + \rangle", Z, (X + Z) / np.sqrt(2), np.pi),
    (r"S:\ \pi/2 \text{ about } \hat{z},\ \lvert + \rangle \to \lvert {+i} \rangle", X, Z, np.pi / 2),
    (r"T:\ \pi/4 \text{ about } \hat{z},\ \lvert + \rangle \to (\lvert 0\rangle + e^{i\pi/4}\lvert 1\rangle)/\sqrt{2}", X, Z, np.pi / 4),
    # Rz from a tilted state (theta = pi/3), so the path shows that the height stays fixed.
    (r"R_z(\varphi):\ \varphi \text{ about } \hat{z},\ \text{here } \varphi = 3\pi/2;\ \theta \text{ is unchanged}",
     np.array([np.sin(np.pi / 3), 0, np.cos(np.pi / 3)]), Z, 3 * np.pi / 2),
]


def rotate(v, axis, t):
    """Rodrigues' formula: v turned by angle t about the unit vector axis."""
    return v * np.cos(t) + np.cross(axis, v) * np.sin(t) + axis * np.dot(axis, v) * (1 - np.cos(t))


def facing(mob):
    """Stand a flat label up so it faces the camera."""
    return mob.rotate(PHI, axis=m.RIGHT).rotate(THETA + 90 * m.DEGREES, axis=m.OUT)


class BlochGateRotations(m.ThreeDScene):
    def construct(self) -> None:
        self.set_camera_orientation(phi=PHI, theta=THETA)
        self.add(m.Sphere(radius=R, resolution=(24, 12)).set_opacity(0.12))
        self.add(m.Circle(radius=R, color=m.GREY))
        for d in (X, Y, Z):
            self.add(m.Line3D(-R * d, R * d, color=m.GREY, thickness=0.01))
        for tex, d in (
            (r"\lvert 0\rangle", Z), (r"\lvert 1\rangle", -Z),
            (r"\lvert + \rangle", X), (r"\lvert {+i} \rangle", Y),
        ):
            self.add(facing(m.MathTex(tex).scale(0.8)).move_to(1.25 * R * d))

        for title_tex, start, axis, angle in GATES:
            title = m.MathTex(title_tex).scale(0.7).to_corner(m.UL)
            self.add_fixed_in_frame_mobjects(title)
            axis_line = m.Line3D(-1.1 * R * axis, 1.1 * R * axis, color=m.RED, thickness=0.02)
            arrow = m.Arrow3D(m.ORIGIN, R * start, color=m.YELLOW)
            path = m.ParametricFunction(
                lambda t, s=start, a=axis: R * rotate(s, a, t), t_range=(0, angle), color=m.YELLOW
            )
            self.play(m.FadeIn(title), m.FadeIn(axis_line), m.FadeIn(arrow))
            self.play(
                m.Rotate(arrow, angle, axis=axis, about_point=m.ORIGIN, rate_func=m.smooth),
                m.Create(path, rate_func=m.smooth),
                run_time=2.5,
            )
            self.wait(1)
            self.play(m.FadeOut(title), m.FadeOut(axis_line), m.FadeOut(arrow), m.FadeOut(path))
