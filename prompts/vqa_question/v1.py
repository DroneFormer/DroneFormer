prompt_template = """
You are given an objective that requires testing for presence of objects in a given video stream, and your goal is to generate a prioritised list of questions (1 or many)
in order of most relevant or important to achieve the objecting by asking about an image that will help you determine whether the object is present in the image 
as well as justification for the order of the questions based on the relevance and importance of the questions.
The types of questions you can ask are limited to:
    (1) yes/no questions
    (2) questions that ask for a count of objects
    (3) questions that ask for a color of an object
    (4)questions about text in the image

You are given:
    (1) an objective that you are tyring to achieve

You respond with:
    (1) a list of questions (1 or many) to ask about an image
    (2) a list of justifications for each image for why it is relevant and why it is in the given order (importance)


EXAMPLE 1:
==================================================
OBJECTIVE:
------------------
Find the number of red cars in the image

QUESTION:
------------------
1. @How many red cars are there in the image?@

JUSTIFICATION:
------------------
1. This question is relevant because it will help me determine if there are any red cars in the image.

EXAMPLE 2:
==================================================
OBJECTIVE:
------------------
Is there someone wearing a red shirt and a blue hat in the image?

QUESTION:
------------------
1. @Is there a person in the image?@
2. @Is there a red shirt in the image?@
3. @Is there a blue hat in the image?@

JUSTIFICATION:
------------------
1. This question is relevant because it will help me determine if there is a person in the image, which is a prerequisite for the other questions.
2. This question is relevant because it will help me determine if there is a red shirt in the image, given that there is a person in the image.
3. This question is relevant because it will help me determine if there is a blue hat in the image, given that there is a person in the image and a red shirt in the image.

EXAMPLE 3:
==================================================
OBJECTIVE:
------------------
How many bags is the person wearing a red shirt and a blue hat carrying in the image?

QUESTION:
------------------
1. @Is there a person in the image?@
2. @Is there a red shirt in the image?@
3. @Is there a blue hat in the image?@
4. @How many bags are there in the image?@

JUSTIFICATION:
------------------
1. This question is relevant because it will help me determine if there is a person in the image, which is a prerequisite for the other questions.
2. This question is relevant because it will help me determine if there is a red shirt in the image, given that there is a person in the image.
3. This question is relevant because it will help me determine if there is a blue hat in the image, given that there is a person in the image and a red shirt in the image.
4. This question is relevant because it will help me determine if there are any bags in the image, given that there is a person in the image and a red shirt in the image and a blue hat in the image.

==================================================

OBJECTIVE
------------------
$objective

QUESTION:
------------------
"""
