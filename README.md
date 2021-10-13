FRANKENBODY challenge
=====================

Preparing for the challenge
---------------------------

We recommend using conda, and we provide a ready to use environment.

1. If needed, [install conda](https://docs.conda.io/en/latest/miniconda.html)
2. Clone [the repository](https://github.com/bayer-science-for-a-better-life/mlr-challenges-frankenbody)
3. Create the environment
4. Run the sanity checks

In commands, steps 2-4 should translate to:

```shell
git clone https://github.com/bayer-science-for-a-better-life/mlr-challenges-frankenbody.git
cd mlr-challenges-frankenbody
conda env create -f environment.yml
conda activate frankenbody
frankenbody smoke
# If all worked, you should see printed "SMOKE TESTS HAVE PASSED 
```

During the challenge day
------------------------
We will provide you with a key to access the secret parts of the challenge.
You will need to add it to ```frankenbody/private_key.py```.

Submitting your solution
------------------------

Please email us when the solution is ready.

Our preferred way to share the results would be via a private GitHub/GitLab repository.
You could even do already before the challenge date. Please add a tag for the final submission
and share it with us in the email.

You can also send the results by email, but please beware of large attachement sizes
(for example if you send us notebooks).

Getting help
------------
Do not hesitate to email us, we are happy to help!
