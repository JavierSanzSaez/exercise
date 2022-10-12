from setuptools import setup

setup(
   name='Unimover',
   version='1.0',
   description='An exercise module that moves file of a group to an archive folder',
   author='Javier Sanz Sáez',
   author_email='javiersse@gmail.com',
   packages=['unimover'],
   url='https://github.com/JavierSanzSaez/exercise',
   entry_points = {
    'console_scripts': [
        'unimover=main:main',
    ]
   }
)