An Antibody Property Prediction Challenge
=========================================

:wave: Hello! At Bayer's Machine Learning Research we are very happy with your interest in our work.

In this challenge you will help us predict a couple of important [antibody](https://pdb101.rcsb.org/motm/21)
properties: :adhesive_bandage: [binding to SARS-CoV2](https://academic.oup.com/bioinformatics/article/37/5/734/5893556)
and :pill: [developability as therapeutics](https://www.pnas.org/content/116/10/4025).

We will provide you with some data (antibody sequences :dna:, ground truth and more)
plus code to load them. We also provide features that should be used to build machine
learning models.

*Note: there is no need to review any of the provided links to successfully complete the task.*

<details><summary>Table of contents</summary>

- [Preparing for the challenge day](#preparing-for-the-challenge-day)
- [During the challenge](#during-the-challenge)
- [Time allotment](#time-allotment)
- [Submitting your solution](#submitting-your-solution)
- [Reviewing](#reviewing)
- [Getting help](#getting-help)
- [Providing feedback](#providing-feedback)
- [Acknowledgements](#acknowledgements)

</details>

Preparing for the challenge day
-------------------------------

We recommend using conda to manage code dependencies, and we provide a [ready to use environment](https://github.com/bayer-science-for-a-better-life/mlr-challenges-frankenbody/blob/main/environment.yml).

1. If needed, [install conda](https://docs.conda.io/en/latest/miniconda.html).

2. Clone [the repository](https://github.com/bayer-science-for-a-better-life/mlr-challenges-frankenbody).
```shell
git clone https://github.com/bayer-science-for-a-better-life/mlr-challenges-frankenbody.git
```

3. Create the environment (and add your favorite libraries).
```shell
cd mlr-challenges-frankenbody
conda env create -f environment.yml
# add your favorite software 
# e.g., conda install -c conda-forge jupyter seaborn pytorch biotite -n frankenbody
# or edit environment.yml
```

4. Run the sanity checks
```shell
conda activate frankenbody
frankenbody smoke
# if all this worked, you should see printed "SMOKE TESTS HAVE PASSED"
# otherwise, please drop us an email
```

As an alternative to cloning, you can [download](https://github.com/bayer-science-for-a-better-life/mlr-challenges-frankenbody/archive/refs/heads/main.zip)
the challenge code and data as a zip file.

These data are small enough for the challenge to be solved in a commodity laptop.


During the challenge
--------------------

At the agreed time, you will receive an email with extra information.

1. To allow for last minute changes, please pull or redownload the repository.
```shell
cd mlr-challenges-frankenbody
git pull
```

2. We will provide you with a key to access the secret parts of the challenge (essentially the data).
<br>You will need to add it to [frankenbody/private_key.py](https://github.com/bayer-science-for-a-better-life/mlr-challenges-frankenbody/blob/f43156644439e8c04ac987cd47998010e25707e1/frankenbody/private_key.py#L5-L6) like:
```python
# Hardcode here the key sent to you, should look like:
FRANKENBODY_PRIVATE_KEY = b'FLrMTzp5j-tGSC6T01X-bMW6B1DEitatc6JmUP3Xs6M='
```

3. To verify that everything has worked correctly, please run:

```shell
conda activate frankenbody
frankenbody smoke-challenge
# if all this worked, you should see printed "CHALLENGE SMOKE TESTS HAVE PASSED"
# otherwise, please drop us an email
```

Feel free to use anything, from python files to notebooks, to shape the solution.


Time allotment
--------------

We just want to get a sense of your thought process and skills.

Please, **do not spend more than 4 hours solving the challenge**.

We respect and appreciate your time. The challenge is scoped in a way that allows
for many paths to completion. We are happy to receive solutions within shorter time frames.

If there are features you wish you had time to implement,
feel free to use pseudocode and/or prose to describe them.


Submitting your solution
------------------------

Please email us when the solution is ready. To share the solution you can:

- **Use a private GitHub/GitLab repository**.This is our preference.
You could set it up before the challenge date. Please give us access to the repository
and share the link with us in the email.
<br><br>
- **Add an attachment to the email**. Alternatively, you can also send the results in a compressed file.
Please beware of large attachement sizes. For example if you send us notebooks,
it would be a good idea to clean first variables holding heavy state (e.g., data and models).


Reviewing
---------

Your submission will be reviewed by at least two of our colleagues and discuss it together at later steps during the interview process.


Getting help
------------

Do not hesitate to email us, we are happy to help!


Providing feedback
------------------

We highly appreciate feedback. Please, let us know about any thought you can share with us.


Acknowledgements
----------------

These data have been derived from:
- [CoV-AbDab](http://opig.stats.ox.ac.uk/webapps/covabdab/) ([paper](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btaa739/5893556), [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/))
- [SAbDab, Chen et al.](https://tdcommons.ai/single_pred_tasks/develop/#sabdab-chen-et-al) ([paper](https://www.biorxiv.org/content/10.1101/2020.06.18.159798v1.abstract), [Therapeutic Data Commons](https://tdcommons.ai/), [CC-BY 3.0 license](https://creativecommons.org/licenses/by/3.0/))
- [TAP](https://tdcommons.ai/single_pred_tasks/develop/#tap) ([paper](https://www.pnas.org/content/116/10/4025.short), [Therapeutic Data Commons](https://tdcommons.ai/), [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/))
