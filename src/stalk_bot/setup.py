from setuptools import setup

package_name = 'stalk_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='william',
    maintainer_email='william.dumez@skynet.be',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'movement = stalk_bot.movement_controller:main',
            'camera = stalk_bot.camera_controller:main',
            'main = stalk_bot.main_controller:main'
        ],
    },
)
