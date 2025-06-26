import matplotlib.pyplot as plt


def plot_profile(profile, i_0=100.0, r_0=20.0, gam=0.8, logScale=False):
    """
    Plot 1D radial intensity profile from a Profile object.
    """
    radius = profile.radius
    intensity = profile.intensity
    plt.figure(figsize=(8, 5))
    plt.plot(
        radius,
        intensity,
        label=rf"$i_0 = {i_0}$, $R_0 = {r_0}$ au, $\gamma = {gam}$",
        color="black",
        linewidth=1.5,
    )
    plt.axvline(r_0, color="blue", linestyle="--", label=rf"$R_0 = {r_0}$ au")
    plt.title(r"Power-law profile: $I(R) = i_0 \left(\frac{R}{R_0}\right)^{-\gamma}$")
    plt.grid(True, alpha=0.5)
    plt.legend()
    plt.tight_layout()

    plt.xlabel("Radius [au]")
    plt.ylabel("Intensity")

    if logScale:
        plt.yscale("log")

    plt.show()
