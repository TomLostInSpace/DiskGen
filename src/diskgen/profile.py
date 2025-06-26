import numpy as np


class Profile:
    def __init__(self, radius, intensity):
        self.radius = np.array(radius)
        self.intensity = np.array(intensity)
        if len(radius) != len(intensity):
            raise ValueError("radius and intensity must have the same length")

    def __repr__(self):
        return f"Profile(radius: {self.radius.shape}, intensity: {self.intensity.shape})"

    def add_ring(self, ring_radius, amplitude=1.0, width=1.0):
        """
        Add a Gaussian-shaped ring to the profile.
        """
        ring = amplitude * np.exp(-0.5 * ((self.radius - ring_radius) / width) ** 2)
        self.intensity += ring

    @classmethod
    def powerlaw(cls, radius, i_0=1.0, r_0=20.0, gam=0.8):
        """
        Create a Profile from a power-law intensity distribution.
        """
        radius = np.array(radius)
        with np.errstate(divide="ignore"):
            intensity = i_0 * (radius / r_0) ** (-gam)
            intensity[radius == 0] = 1e-10  # Avoid division by zero
        return cls(radius, intensity)
