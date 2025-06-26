import numpy as np
import matplotlib.pyplot as plt
from src.diskgen.profile import Profile
from src.diskgen.plotting import plot_profile
from src.diskgen.image import create_disk_from_profile
from src.diskgen.io_utils import save_to_fits

# 1. Create a Power-Law Intensity Profile
radius = np.linspace(0.1, 100, 500)
profile = Profile.powerlaw(radius, i_0=100.0, r_0=20.0, gam=0.8)
plot_profile(profile, i_0=100.0, r_0=20.0, gam=0.8)

# 2. Add a Gaussian Ring
profile.add_ring(ring_radius=40, amplitude=50.0, width=5.0)
plot_profile(profile)

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
