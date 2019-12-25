## Webapp for object classification using Django and TensorFlow

#### Overview

This project has two parts - 

- make an object classifier. In this case it is simple cats and dogs classifier
- make a webapp for the classifier 

The goal of this project is to create a webapp through which a user will be to able to upload 
an image. It can either be a cat or a dog image. Once an image is uploaded, it will be stored in
the `media` folder. The webapp then processes it and predicts its class. 

Here is an overview of the webapp - 

![Sc1](Screenshots/sc1.jpg)

User can upload an image through the `Upload` tab.

![Sc2](Screenshots/sc2.jpg)

Finally, the output can be viewed from the `Output` tab.

![Sc3](Screenshots/sc3.jpg)

![Sc4](Screenshots/sc4.jpg)

#### How to run

Before running the server, run `tf_classifier.py`. It is inside the `core` folder. You will 
need to define your dataset directory in the code. It will then train the cats and dogs classifier. Convolutional neural network (CNN) is used here. 
Once the training is complete, it will store the model. 

Now, select `mysite` as the current directory in the command prompt or terminal.

To run server, type - 

    python manage.py runserver

To migrate, type -

    python manage.py migrate

#### Dataset

Cats and dogs dataset is available [here](https://www.microsoft.com/en-us/download/details.aspx?id=54765 "cats-&-dogs-dataset") 

#### Reference

Webapp design - 

https://www.youtube.com/playlist?list=PLLxk3TkuAYnpm24Ma1XenNeq1oxxRcYFT

Classifier design - 

https://www.youtube.com/watch?v=j-3vuBynnOE
