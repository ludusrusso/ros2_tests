from setuptools import setup

package_name = 'ros2_test'

setup(
    name=package_name,
    version='0.1.0',
    packages=[],
    py_modules=[
        'pub',
        'sub',
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    author='Ludovico O. Russo',
    keywords=['ROS'],
    description='Test of minimal pub/sub rclpy.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub = pub:main',
            'sub = sub:main'
        ],
    },
)
