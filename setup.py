import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='activecampaign-python',
      version='0.1.1',
      description='ActiveCampaigs API written in python',
      long_description=read('README.md'),
      author='Lelia Rubiano',
      author_email='lrubiano5@gmail.com',
      url='https://github.com/GearPlug/activecampaign-python',
      packages=['activecampaign'],
      install_requires=[
          'requests',
      ],
      keywords='activecampaign',
      zip_safe=False,
      license='GPL',
     )