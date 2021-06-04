# Test, Travis + Robots
## Before you begin 

During this assignment you will configure a CI/CD workflow usig Travis CI with PyTest as unit test.



Clone this repository in your working space. 

Take note that the badges are unknown or broken on purpouse. You will be asked to replace them with your own badges during this excercise.

Once you have cloned the repo, take a moment to familiarize with the content, files and structure. What do you think each one of these files are good for?

--------------------------------
## Badges 

[![Build Status](https://travis-ci.com/artexmg/travis-rg6-test.svg?)](https://travis-ci.com/artexmg/travis-rg6s-test)

[![Maintainability](https://api.codeclimate.com/v1/badges/2b298cd450c412a7aaf7/maintainability)](https://codeclimate.com/github/enroute-university/g6-pytest-travis-HazeMSR/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/2b298cd450c412a7aaf7/test_coverage)](https://codeclimate.com/github/enroute-university/g6-pytest-travis-HazeMSR/test_coverage)
----------------

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Test, Travis + Robots](#test-travis--robots)
  - [Before you begin](#before-you-begin)
  - [Badges](#badges)
  - [Install dependencies](#install-dependencies)
  - [Testing](#testing)
    - [important files for testing](#important-files-for-testing)
  - [CI/CD usign Travis](#cicd-usign-travis)
  - [Add Code Climate badge](#add-code-climate-badge)
    - [Get the Test Reporter ID](#get-the-test-reporter-id)
    - [Set Test Reporter ID in Travis](#set-test-reporter-id-in-travis)
    - [Set up test coverage](#set-up-test-coverage)
- [Problems](#problems)
  - [Improve coverage for my_calc](#improve-coverage-for-my_calc)
  - [Test Fibonacci function](#test-fibonacci-function)
  - [Deploy](#deploy)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Install dependencies

Create a new conda environment and activate it; then install pipenv within the new conda environment. You may want to review the instructions from previous assignments.

Just to understand what dependencies are needed, review the content of the *Pipfile* (do not change anything tho!) then install the dependencies with pipenv

```bash
$ pipenv install --dev
```

## Testing

Verify that you are able to run the script by executing 

```python
pipenv run python deploy.py
```

Take a look at the test script file *test_my_calc.py*, try to understand what is happening. Run the test script with pytest executing this command

```python
pipenv run pytest
```

You will get something similar to this output

```bash
---- coverage: platform darwin, python 3.9.4-final-0 ----
Name         Stmts   Miss Branch BrPart  Cover
----------------------------------------------
my_calc.py      24     14     16      4    35%
----------------------------------------------
TOTAL           24     14     16      4    35%
Coverage HTML written to dir htmlcov
```

How can we improve the coverage for my_calc.py? For that, we need to know what lines were not covered in our unit test (missed lines)

We need to get more information. Edit the file *.coveragerc* and add this directive at the end

```
show_missing = true
```

Now you will get the number of lines that were not covered by the unit test.  

Also you can run pytest to generate an html report with this command:

```
pipenv run pytest --cov-report html --cov-report term
```

Let's try to increase the coverage by adding a test case for substraction. Add the following function to *test_my_calc.py* and run pytest coverage after that. You should see an increase on coverage.

```python
def test_subs():
    current_value = my_calc.subs(100,15)
    expected_value = 85

    assert expected_value == current_value    

```

You will be asked to increase the coverage in the problem section.

### important files for testing

pytest.ini

.coveragerc

test_my_calc.py

## CI/CD usign Travis

Once we have a basic test, we can start working on continuos integration. We are going to use Travis CI for that purpose. 

First you will need to create a Travis account; [go to Travis' website](https://travis-ci.com/), sign up using your Github Account as authentication method and follow the instructions for seting up your Travis Account.

**Do not go** to travis-ci.org, this is an old url and will be deprecated on June 15th, 2021

Once your account is configured properly, you should be able to see the your repositories, look for the current one and observe the build badge. What is the build status?

You need to replace the badge at the begining of this README file with your own badge. 

Click on the *build badge* to open the *Status Image* window. Select Format = Markdown and copy the content of *Result*. Paste it to replace the build badge at the begining of this repository.

The content would look similar to this

```html
[![Build Status](https://travis-ci.com/enroute-university/g6-pytest-art-enroute.svg?token=kttCqQm6KZYXJD7qbVsY&branch=main)](https://travis-ci.com/enroute-university/g6-pytest-art-enroute)
```

## Add Code Climate badge

[Go to code climate](codeclimate.com) and create a new account. You need to select **Quality** in the login menue. Then, signup with your github account.

Pic *Enroute University* as your organization, select *Add a repository* and then add this repo. If everything is OK you will be able to see the results of maintability and test coverage.

### Get the Test Reporter ID

Follow the instructions on [Finding Test Coverage ID](https://docs.codeclimate.com/docs/finding-your-test-coverage-token#section-regenerating-a-repos-test-reporter-id) to get the Test Reporter ID, it should look similar to the following string

```
fd15d063181e016bc3168c83cc228116aa0c344517660a348fbc46fdc312e3e6
```

### Set Test Reporter ID in Travis

Now go back to Travis, make sure you are in this repository. From the  "More options" menu select Settings. Create a new Environment Variable named CC_TEST_REPORTER_ID and set the value to the Test Reporter ID you got in the previous step. 

Now we are ready to include our test coverage.

### Set up test coverage 

Open the file .travis.yml and add the following lines in the *before_script* section

```yaml
  - curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > ./cc-test-reporter
  - chmod +x ./cc-test-reporter
  - ./cc-test-reporter before-build
```

and add this line in the **

```yaml
- ./cc-test-reporter after-build --exit-code $TRAVIS_TEST_RESULT
```

Commit your repository and push it to Github. Go to Travis and verify that the repository builds successfully. 

Now go to Code Climate. If everything went OK you should have badges for Maintanability and Test Coverage. 

From Code Climate menu select Repo Settings and then go to Badges. Copy the Markdown code for both badges and replace the values in this README.md 

Commit your repo and push it. 

# Problems

## Improve coverage for my_calc

During a previous step you increased the coverage for my_calc by adding an unit test for substraction.

Now add unit tests for multiplication and division to increase the coverage to at least to 85%, but you should be able to get it to 100%

Recall that you can generate the HTML Report to get more information.

## Test Fibonacci function

So far you've tested only the module *my_calc.py*. But there is another piece of code in this repository that you need to test. 

Look the code in *fibonacci.py* and try to understand what is the purpose of it. 

Add these lines to *deploy.py*. Don't forget to import the module fibonacci at the begining of the script!

```python

    fibo = fibonacci.optimized_fibonacci(sum)
    print(f"The fibonacci sequence for {sum} = {fibo}")
```

Then run pytest. You should be able to see the coverage for fibonacci.py

```
------ coverage: platform darwin, python 3.9.4-final-0 
Name           Stmts   Miss Branch BrPart  Cover
------------------------------------------------
fibonacci.py      28     22     12      1    18%
my_calc.py        24     16     16      1    28%
------------------------------------------------
TOTAL             52     38     28      2    22%
```

create unit tests for fibonacci to increase the coverage at least to 85%

## Deploy
Commit and push your repo. All your badges should be green now.

Also pay attention to the maintainability. Try to fix as many issues as possible. The grade (code climate maintainability) should not get lower than A.


