# Image Captioning

## Description
Image Captioning is the task of describing the content of an image in words. This task lies at the intersection of computer vision and natural language processing. 


We used an encoder-decoder framework, where an input image is encoded into an intermediate representation of the information in the image, and then decoded into a descriptive text sequence


### Input
We need to specify the path of the image.
Example :
```
$env:IMAGE_PATH = "data/image1.jpg"
```
### Output
Caption of the image.

## Docker
Using Dockerfile you can :
- Build the project 
` docker build -t image-captioning .`
- Run the container using the correct paths on env variables.   
For instance:
```
docker run  \
  -v $(pwd)/data_sample:/data_sample \
  -e IMAGE1_PATH="./data/image.jpg" \
  image-captioning:latest 
```

## Requirements
The requirements for the project are the following:
- python3.6+
- make command
    - For windows users, you can download make command following this [link](https://sourceforge.net/projects/gnuwin32/files/make/3.81/make-3.81.exe/download?use_mirror=netix&download=). For more details on other versions, follow [this page](https://gnuwin32.sourceforge.net/packages/make.htm)
    - For linux/mac users, download make command following your ``sudo apt-get update & apt-get -y install make``

To check make is correctly installed, type ``make --version``

## Setup the environment

Start by running ``make --version`` and ``python --version`` to make sure you have all the prerequists, otherwise ``pip install make``.
In case you are on Windows and you could not install make, [install chocolately before](https://chocolatey.org/install)
then ``choco install make``.

In your terminal:
- Run ``make setup``
- activate your environement :
    - Windows: .\wenv\Scripts\activate
    - Linux:   ./venv/bin/activate
- Start developping !

PS: To check that you're on the right envrionnement, type ``python -m image_captioning.src.main``.

## How to run the code
After specifiying the images paths, run :
```
python -m image_captioning.src.main
```

## Dev tools available:

Those command are targeting the **image_captioning** folder and the configuration is [here](setup.cfg).

* Code Quality: You can trigger those commands with `make check`.
  * **Formatting** with `black + isort`: To format use ``make format`` and check with `make black` and `make isort` for `black` and `isort` respectively
  * **type-checking** with `mypy`: You can use `make mypy` to check the types and detect errors
  * **Linting** with `flake8 + pylint`: You can use `make flake8` and `make pylint` to lint your code using `flake8` and `pylint` respectively.
* Tests:
  * For testing we use `pytest` and target the tests in the **image_captioning** using `make test`
  * You can generate a coverage report using `make coverage` and a html version using `make coverage-html`


## Git instructions

``git init``
``git remote add origin https://github.com/siwaar/Project-Template.git``
``git branch -M main``
``git add .``
``git commit -m "first commit"``
``git push -u origin main``