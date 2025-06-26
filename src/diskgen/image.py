import numpy as np


def create_disk_from_profile(profile, image_size=256, scale="linear"):
    """
    Create a 2D circularly symmetric image from a radial intensity profile.
    """
    radius = profile.radius
    intensity = profile.intensity

    # Creating the grid for the image
    y, x = np.indices((image_size, image_size))

    # Calculating the radius from the center of the image
    center = (image_size - 1) / 2
    r = np.sqrt((x - center) ** 2 + (y - center) ** 2)

    # Scaling the radius based on the specified scale
    r = r / np.max(r) * np.max(radius)

    # Fills each pixel in the image with the corresponding intensity value from the profile
    image = np.interp(r, radius, intensity, left=0, right=0)
    return image
