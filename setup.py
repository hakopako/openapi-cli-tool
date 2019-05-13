from setuptools import setup, find_packages

setup(
    name='openapi-cli-tool',
    description="openapi cli tool - scaffold",
    long_description=open('README.md').read(),
    author="Ayaka Shimada",
    author_email='aya.a.shimada@gmail.com',
    url='https;//web.hakopako.net',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'openapi-cli-tool = src.sample:main',
        ],
    },
    zip_safe=False
)
