from setuptools import setup

setup(
    name='kinshipsim',
    version='2020.6',
    packages=['kinshipsim', 'kinshipsim.scripts'],
    include_package_data=True,
    url='https://github.com/CompEvoMetu/kinshipsim',
    license='GNU General Public License v3 (GPLv3)',
    author='Team Neogene',
    author_email='imapelli@metu.edu.tr',
    description='A kinship simulation tool',
    long_description="""The **kinshipsim** library has been implemented to infer the genetic relationships between 
    pairs of individuals. Following the estimation of the kinship coefficient (theta) and probabilities of sharing 0, 
    1 or 2 alleles  identical-by-descent (Cotterman coefficients, k0, k1, k2), it is necessary to determine the 
    specific ranges for each degree of relatedness as well as kinship relationships. Given this context, this library 
    allows to simulate multiple pedigrees, using both autosomal and X chromosomal data, to study the distribution of 
    the aforementioned parameters across each degree of interest in the attempt to approximate their boundaries.""",
    install_requires=['pandas', 'numpy', 'fire'],
    python_requires='>=3',
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering"
    ]
)
