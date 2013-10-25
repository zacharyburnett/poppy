# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Physical Optics Propagation in PYthon (POPPY)

This package implements an object-oriented system for modeling physical optics
propagation with diffraction, particularly for telescopic and coronagraphic
imaging. 

POPPY makes use of python's ``logging`` facility for log messages, using
the logger name "poppy".


"""
#Module-level configuration constants
#------------------------------------
#
#_USE_FFTW3 : bool
#    Should the FFTW3 library be used? Set automatically to True if fftw3 is importable, else False.
#_USE_MULTIPROC : bool
#    Should we use python multiprocessing to spawn multiple simultaneous processes to speed calculations?
#    Note that FFTW3 automatically makes use of multiple cores so this should not be used at the same time as
#    _USE_FFTW3. Default is False.
#_MULTIPROC_NPROCESS : int
#    If the above is set, how many processes should be used? Default is 4. Note that you probably don't want to 
#    set this too large due to memory limitations; i.e. don't just blindly set this to 16 on a 16-core machine unless
#    you have many, many GB of RAM...
#
#_TIMETESTS : bool
#    Print out simple benchmarking of elapsed time to screen. Default False
#_FLUXCHECK : bool
#    Print out total flux after each step of a propagation. Useful for debugging, mostly.
#
#_IMAGECROP : float
#    Default zoom in region for image displays. Default is 5.0
#


try:
    from .version import version as __version__
except ImportError:
    # TODO: Issue a warning using the logging framework
    __version__ = ''
try:
    from .version import githash as __githash__
except ImportError:
    # TODO: Issue a warning using the logging framework
    __githash__ = ''

 

from .poppy_core import (Wavefront, OpticalElement, FITSOpticalElement, Rotation, AnalyticOpticalElement, 
	ScalarTransmission, InverseTransmission, ThinLens, BandLimitedCoron, 
	FQPM_FFT_aligner, IdealFQPM, IdealFieldStop, IdealRectangularFieldStop, IdealCircularOcculter, 
	IdealBarOcculter, ParityTestAperture, CircularAperture, HexagonAperture, 
	MultiHexagonAperture, NgonAperture, SquareAperture, RectangleAperture, SecondaryObscuration, AsymmetricSecondaryObscuration, CompoundAnalyticOptic, 
	Detector, OpticalSystem, SemiAnalyticCoronagraph)

from .utils import (display_PSF, display_PSF_difference, display_EE, display_profiles, radial_profile,
        measure_EE, measure_radial, measure_fwhm, measure_sharpness, measure_centroid, measure_strehl,
        measure_anisotropy, specFromSpectralType, rebin_array)

from .settings import save_config #, autosave_fftw_wisdom

from .instrument import Instrument

# Not yet implemented:
#from .wfe import ZernikeWFE, PowerSpectralDensityWFE, KolmogorovWFE



if settings.autosave_fftw_wisdom():
   # the following will just return if FFTW is not present
   utils.fftw_load_wisdom()



