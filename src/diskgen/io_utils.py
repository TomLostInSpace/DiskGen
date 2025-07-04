from astropy.io import fits
from pathlib import Path
from datetime import datetime


def save_to_fits(image, filename="disk_image.fits"):
    """
    Save a 2D image to a FITS file under Output/YYYY-MM-DD/

    Parameters:
        image (2D array): the image data to save
        filename (str): output file name (should end with .fits)
    """
    # Get today's date string
    today = datetime.now().strftime("%Y-%m-%d")
    output_dir = Path("../Output") / today
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / filename

    hdu = fits.PrimaryHDU(image)
    hdul = fits.HDUList([hdu])
    hdul.writeto(file_path, overwrite=True)

    print(f"Saved FITS file to: {file_path}")
