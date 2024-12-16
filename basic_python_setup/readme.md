# How to start a project from scratch
### Requirements:
- conda
- text-editor (VScode, Vim, sublime, ++)

## How to create environment:
First set up your basic needs in the 'environment.yml' and 'requirements.txt' file. In the environment.yml file you need to specify the name of the environment and python version and pip. In the requirement.txt file you need to specify the python packages that you want to use. This is a evolving process where the requironment for the env is developed as you go. When you do a 'pip install package', you can write:

    conda list

to see your packages in the enviroment. 
When you update the requirements.txt file it is important to write both the package and the version number, i.e:
### God:
    numpy==1.24.1

This is to recreate the exact same env as you use. If you only write:
### Bad:
    numpy

it will pick up the newest one, which might induse breaking changes into the enviroment. 

To create your enviroment and start using the env you have these terminal commands:

    conda env create -f environment.yml
    conda activate CONDA_PROJECT_NAME

It is also a good practice to remove the environment and rebuild it on occations. This is to verify that you don't have any breaking changes. The terminal input for this is:

    conda deactivate
    conda env remove -n CONDA_PROJECT_NAME

Then rebuild it with:

    conda env create -f environment.yml

If your code or env is not working, you must go through the env and req files and make sure there is nothing wrong. Also the error message in the terminal usualy is good and easy to google.