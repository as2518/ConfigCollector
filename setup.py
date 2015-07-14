from setuptools import setup

setup(
    name='ConfigCollector'
    version='0.1.0'
    packages=[
        'configcollector',
        'ssh_router',
        'file_handler'
    ],
    include_package_data=True,
    install_requires=[
        'Exscript',
    ],
    entry_points=```
        [console_scripts]
        configcollector = configcollector
    ```
)
