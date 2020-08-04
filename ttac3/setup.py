from setuptools import setup
import os
cur_dir_p = os.path.abspath(os.path.dirname(__file__))
inner_dir_path = os.path.join(cur_dir_p, 'png')

# from time import sleep
# sleep(1)
# from glob import glob
package_name = 'ttac3'

data_files = [
#         # ('./png1',['cansel_button.png']),
#         # ('./png2',['cansel_button.png']),
#         ('./png',['cansel_button1.png']),
#         ('./png',['cansel_button2.png']),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ]


# data_files = [
#     # ('.',['one.cpp', 'two.cpp', 'a.h', 'b.hpp', 'c.h'])
#     ('./png',['cansel_button.png', 'ok_button.png'])
#     ]
        # +[('./resource/png', [file_name]) for file_name in os.listdir(inner_dir_path)]
# import ipdb; ipdb.set_trace()

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    # package_data = {
    #     'png': ['cansel_button.png']
    # },
    # include_package_data=True, # 
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
