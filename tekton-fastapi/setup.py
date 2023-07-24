import setuptools

with open('requirements.txt') as f:
    REQUIRES = f.readlines()

setuptools.setup(
    name='tekton-fastapi',
    version='0.1.0',
    license="Apache License Version 2.0",
    url="https://github.com/oasis9217/tekton-python-client.git",
    description="FastAPI server for Tekton API",
    packages=[
    ],
    package_data={'': ['requirements.txt']},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=REQUIRES,
)
