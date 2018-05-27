from setuptools import setup

setup(
    name="synapse-public-profile-api",
    version="0.0.1",
    description="Provides a resource for providing public profiles for users on your homeserver",
    packages=["synapse-public-profile-api"],
    install_requires=['twisted']
)
