"""AWOT: Airborne Weather Observations Toolkit.

AWOT is a toolkit of utilities to analyze and visualize weather
observations taken by aircraft.  


"""

#from numpy.distutils.core import setup
from setuptools import setup
import os
import glob

#- Pull the header into a variable
doclines = __doc__.split("\n")

#- Set variables for setup
packages = ['awot',
            'awot.io',
            'awot.display',
            'awot.graph']
package_dirs = {'awot'}
#datafiles = glob.glob(os.path.join(pathout, '*'))
#datafiles = [os.path.join('data', os.path.basename(f)) for f in datafiles]
#package_data = {'awot': datafiles}

#- Run setup
setup(name='awot',
      version='0.1.0',
      author='Nick Guy',
      author_email='nick.guy@noaa.gov',
      packages=packages,
#      package_dir=package_dirs,
#      package_data=package_data,
      url='https://github.com/nguy/AWOT',
      license='LICENSE.txt',
      description=doclines[0],
      long_description="""A toolkit that contains utilities to analyze and 
      visualize observational data by aircraft.
        """,
      install_requires=['Numpy>=1.7.2',
                        'SciPy>=0.13.3',
                        'matplotlib>=1.3.1',
                        'pyart'],
      )