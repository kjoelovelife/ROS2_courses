from setuptools import setup
import os
from glob import glob

package_name = 'part_1'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'wall_following = part_1.wall_following:main',
            'find_wall_service = part_1.find_wall_service:main',
            'test_server = part_1.test_server:main',
            'test_client = part_1.test_client:main',
            'test_action = part_1.test_action:main',
            'record_odometry_action_server = part_1.record_odometry_action_server:main',
        ],
    },
)
