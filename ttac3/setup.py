from setuptools import setup

package_name = 'ttac3'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'setuptools',
        'pyautogui',
        'opencv-python',
        'python-xlib'],
    zip_safe=True,
    maintainer='shikito',
    maintainer_email='shikito.aos@gmail.com',
    description='Control library for TTA_C3',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server = ' + package_name + '.ttac3_action_server:main',
            'client = ' + package_name + '.ttac3_action_client:main',
        ],
    },
)
