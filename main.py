import numpy as np
import matplotlib.pyplot as plt
from src.diskgen.diskprofile import DiskProfile
from src.diskgen.plotting import plot_profile
from src.diskgen.image import create_disk_from_profile
from src.diskgen.io_utils import save_to_fits

# 1. Create a Power-Law Intensity Profile
i_zero = 10**6
r_zero = 20.0
gamma = 0.8

radius = np.linspace(1, 100, 1000)
profile = DiskProfile.powerlaw(radius, i_0=i_zero, r_0=r_zero, gam=gamma)
plot_profile(profile, i_0=i_zero, r_0=r_zero, gam=gamma, logScale=False)

# 2. Add a Gaussian Ring
profile.add_ring(ring_radius=40, amplitude=10**6, width=5.0)
plot_profile(profile, i_0=i_zero, r_0=r_zero, gam=gamma, logScale=False)

# 3. Generate 2D Image from Profile
image = create_disk_from_profile(profile, image_size=256)
plt.imshow(image, origin="lower", cmap="inferno")
plt.colorbar(label="Intensity")
plt.title("2D Disk Image")
plt.xlabel("Pixel X")
plt.ylabel("Pixel Y")
plt.show()

# 4. Save Image to FITS File
save_to_fits(image, filename="test_disk_profile.fits")
