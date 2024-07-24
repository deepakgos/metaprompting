from setuptools import setup, find_packages

setup(
    name='metaprompt',
    version='1.0.0',
    author='Deepak Puri Goswami & Ojas Somvanshi',
    author_email='deepak.puri@unifycloud.com',
    description='A library for creating and managing meta prompts for various applications',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/deepakgos/metaprompt',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],
    license='MIT',
    keywords='meta prompts, prompt engineering, natural language processing',
)