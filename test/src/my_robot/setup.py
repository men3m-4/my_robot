from setuptools import setup
from glob import glob

package_name = 'my_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch/', glob('launch/*.py')),
        ('share/' + package_name + '/urdf/', glob('urdf/*')),
        ('share/' + package_name + '/world/', glob('world/*')),
        ('share/' + package_name + '/rviz/', glob('rviz/*')),
        ('share/' + package_name + '/meshes/collision/', glob('meshes/collision/*')),
        ('share/' + package_name + '/meshes/visual/', glob('meshes/visual/*')),
    ],
    install_requires=['setuptools>=58.0.0'],
    zip_safe=True,
    maintainer='ros-industrial',
    maintainer_email='your_email@example.com',
    description='A ROS 2 package for robot simulation and control',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Add your node executables here
        ],
    },
)

