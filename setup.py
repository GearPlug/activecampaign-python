import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='activecampaignv3-python',
      version='1.0.0',
      description='ActiveCampaign API written in python',
      long_description=read('README.md'),
      author='Miguel Ferrer',
      author_email='ingferrermiguel@gmail.com',
      url='https://github.com/ingmferrer/activecampaignv3-python',
      packages=['activecampaignv3'],
      install_requires=[
          'requests',
      ],
      keywords='activecampaign',
      zip_safe=False,
      license='MIT',
      )
