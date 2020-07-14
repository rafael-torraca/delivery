from setuptools import setup, find_packages


#para instalar com -> pip install . deve ter o setup()

def read(filename):
    return [
        req.strip()
        for req in open(filename).readlines()
        ]



setup(
    name="delivery",
    version="0.1.0", #major(grande), minor(minima), patchfix(correção) #semver.org -> semantic version
    description="Delivery App",
    packages=find_packages(), #toda pasta que tiver __init__ ele coloca como instalador (exclude="./.env)"
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt") #pode ter outros ambientes, ex: "stage": read(requirements-stage.txt)
    }
)