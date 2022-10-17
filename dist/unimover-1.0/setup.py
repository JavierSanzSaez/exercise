from setuptools import setup

setup(
   name='unimover',
   version='1.0',
   description='An exercise module that moves file of a group to an archive folder',
   author='Javier Sanz Sáez',
   author_email='javiersse@gmail.com',
   url='https://github.com/JavierSanzSaez/exercise',
   entry_points = {
    'console_scripts': [
        'unimover=unimover:main',
    ]
   }
)