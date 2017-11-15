from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
import os
from dyst import VERSION



long_description='''Dyst is a command line tool to visualize histograms in real time''' 
setup(
	name='dyst',

	# Versions should comply with PEP440.  For a discussion on single-sourcing
	# the version across setup.py and the project code, see
	# https://packaging.python.org/en/latest/single_source_version.html
	version=VERSION,

	description='Dyst Dynamic histograms in the terminal',
	long_description=long_description,

	# The project's main homepage.
	url='https://github.com/coelias/dyst',

	# Author details
	author='Carlos del Ojo Elias',
	author_email='deepbit@gmail.com',

	# Choose your license
	license='GPLv3',

	# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers=[
		# How mature is this project? Common values are
		#   3 - Alpha
		#   4 - Beta
		#   5 - Production/Stable
		'Development Status :: 5 - Production/Stable',

		# Indicate who your project is intended for
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering :: Visualization',

		# Pick your license as you wish (should match "license" above)
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

		# Specify the Python versions you support here. In particular, ensure
		# that you indicate whether you support Python 2, Python 3 or both.
		'Programming Language :: Python :: 2',
                "Programming Language :: Python :: 3"
	],

	# What does your project relate to?
	keywords='plotting interactive terminal histogram chart realtime dynamic',

	# You can just specify the packages manually here if your project is
	# simple. Or you can use find_packages().
	packages=find_packages(),

	# List run-time dependencies here.  These will be installed by pip when your
	# project is installed. For an analysis of "install_requires" vs pip's
	# requirements files see:
	# https://packaging.python.org/en/latest/requirements.html
	install_requires=[],

	# List additional groups of dependencies here (e.g. development dependencies).
	# You can install these using the following syntax, for example:
	# $ pip install -e .[dev,test]
	extras_require = {
	},

	# If there are data files included in your packages that need to be
	# installed, specify them here.  If using Python 2.6 or less, then these
	# have to be included in MANIFEST.in as well.
	package_data={},

	# Although 'package_data' is the preferred approach, in some case you may
	# need to place data files outside of your packages.
	# see http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
	# In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
	data_files=[],

	# To provide executable scripts, use entry points in preference to the
	# "scripts" keyword. Entry points provide cross-platform support and allow
	# pip to create the appropriate form of executable for the target platform.
	entry_points={ },
        scripts=['dyst/dyst']
)

