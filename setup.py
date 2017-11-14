from setuptools import setup


setup(name='ActiveCampaign',
      version='0.1',
      description='ActiveCampaigs API written in python',
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