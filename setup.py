from setuptools import setup
setup(
    name='GetRouterConfig'
    version='0.9.0'
    packages=[
        'get_router_config',
        'ssh_router',
    ],
    include_package_data=True,
    install_requires=[
        'Exscript',
    ],
    entry_points=```
        [console_scripts]
        get_config = get_router_config
    ```
)

