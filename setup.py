from setuptools import setup, find_packages

setup(name='BraTS',
      version='0.1',
      packages=find_packages(),
      description="BraTS 2018 Challenge",
      author="Jon Deaton, Cam Backes",
      author_email="jdeaton@stanford.edu, cbackes@stanford.edu",
      license='MIT',
      install_requires=[
          "tensorflow",
          "numpy",
          "matplotlib",
          "pandas",
          "nibabel",    # Neuro-Imaging file format library
          "nipype",     # More neuro-imaging libraries
          "nilearn",
          "SimpleITK"   # For normalizing the data
      ],
      zip_safe=False)
