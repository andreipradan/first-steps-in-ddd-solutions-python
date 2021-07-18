# First Steps in Domain-Driven Design - Python Solution
![Build](https://github.com/andreipradan/first-steps-in-ddd-solutions-python/actions/workflows/build.yml/badge.svg)

This is the starter project for the exercises in the "First Steps in Domain-Driven Design" course for O'Reilly.  If you are more of a Java person, take a look at the [Java version of this codebase](https://github.com/First-Steps-in-DDD-Community/first-steps-in-ddd-solutions/blob/main/README.md). If you prefer dotnet, take a look at the [C# version](https://github.com/First-Steps-in-DDD-Community/first-steps-in-ddd-solutions-dotnet/blob/main/README.md) (Thanks to @BAPostma for contributing this).

You should be able to fork and then clone this repo to get an almost-empty python project ready to work with.

## Pre-requisites
* python 3.7+
* IDE of your choice
* Git client (unless you already have one in your IDE)

## What you get
A directory `first-steps-in-ddd-python` containing this README.md, a solution file with the code and test projects.
Source files in `src` and the unit tests that live in `tests` directory containing some example unit tests
(`test_a_police_investigation.py`, `test_a_precharge_decision.py` and `test_a_criminal_case.py`) and associated starter
classes found in `src/justice_app.py` (e.g. `PoliceInvestigation`, `PNCId`, `Suspect.py`) and an Enum, `CriminalOffence`.

## Up and running
The training relies entirely on your writing unit tests (ideally you use test-driven development),
so you want to be able to run them very quickly.

Open the newly checked out project in your IDE (point it at the top-level project directory).
Install the requirements from requirements.txt
Then check you can execute all the tests with the click of a single mouse
button, or ideally a single keyboard shortcut.

Additionally, you can run the tests from the command line. Open a terminal and change to the
top-level project directory. Then run the command `pytest tests/`.
You ought to see your tests running, and all but one of the tests run successfully.

The failing test is where we will start exercise one.

## Get ahead of the game
We're going to work on this code based on a [Domain Expert Statement from a Public Prosecutor](https://docs.google.com/document/d/1HpRJj1lk_M80Xvwzs5F-lZ1oACkVNeWRMG0s7BQxZzk/edit?usp=sharing).  If you want to read it in advance, that'll help you in the first workshop exercise and beyond.
