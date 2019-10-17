from setuptools import setup, find_packages


setup(
    name='task-diary',
    version='1.0.0',
    description='Console diary.',
    license='Apache License 2.0',
    author='Myadzel Vladislav',
    author_email='capybarralt@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'diary = task_diary:main',
        ],
    },
    package_data={
        'task_diary': ['resources/*']
    }
)
