from setuptools import setup

setup(
    name='kinshipsim',
    version='2020.7',
    packages=['kinshipsim', 'kinshipsim.scripts'],
    include_package_data=True,
    url='https://github.com/CompEvoMetu/kinshipsim',
    license='GNU General Public License v3 (GPLv3)',
    author='Team Neogene',
    author_email='imapelli@metu.edu.tr',
    description='A kinship simulation tool',
    long_description="""The **kinshipsim** library has been implemented to infer the genetic relationships between 
    pairs of individuals. It enables the simulation of multiple pedigrees, using both autosomal and X chromosomal data,
    and provides additional pre-processing options, e.g., SNPs reduction, pseudo-haploidization.""",
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
