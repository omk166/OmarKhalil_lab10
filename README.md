# Lab 10: Jenkins CI/CD

Author: Omar Khalil  
GitHub: omk166  
Repository: https://github.com/omk166/OmarKhalil_lab10

This project completes the code for graded Parts 3 and 4 of Lab 10.
The application prints `Hello, World from Omar Khalil!`.

## Jenkins setup

1. Install Jenkins with a supported Java runtime. Install Git, Pipeline, and
   JUnit plugins (the suggested plugin set normally includes these).
2. Ensure Git and Python 3.10 or newer are on the Jenkins agent's PATH.
   Linux agents also need Python's venv support. The agent needs network
   access to PyPI to install dependencies.
3. Create a Pipeline job named `Python-CI-CD`.
4. Select **Pipeline script from SCM**, choose **Git**, and enter
   `https://github.com/omk166/OmarKhalil_lab10.git`.
5. Set the branch to `*/main` and Script Path to `Jenkinsfile_Omar_Khalil`.
6. Save and select **Build Now**. All six stages must pass.
7. Download the test, coverage, Bandit, and deployment artifacts from the build.
   Add the actual build URL, number, and console output to `REPORT.md`.

The pipeline supports Windows (`bat`) and Linux/macOS (`sh`), using the virtual
environment's Python directly. Each failed command stops the pipeline before
deployment. Builds have a 15-minute timeout and cannot run concurrently.

## Stages

| Stage | Operation |
| --- | --- |
| Setup | Create `.venv` and install pinned dependencies |
| Lint | Run flake8 on application, deployment script, and tests |
| Test | Run pytest and save JUnit XML |
| Coverage | Measure statement and branch coverage; require 100%; export XML/HTML |
| Security Scan | Scan both production Python files with Bandit; fail on findings |
| Deploy | Copy app.py to deployment/app.py and execute the deployed copy |

Local deployment is the lab's permitted simple local deployment option.
The deployed file is archived in Jenkins before workspace cleanup; download
it and run `python app.py` to use it. This CLI application has no server process.
No remote server or SSH credentials are required.

## Run locally

```text
python -m venv .venv
```

On Windows use `.venv\Scripts\python.exe` for `PYTHON` below;
on Linux/macOS use `.venv/bin/python`.

```text
PYTHON -m pip install -r requirements.txt
PYTHON -c "from pathlib import Path; Path('reports').mkdir(exist_ok=True)"
PYTHON -m flake8 app.py deploy.py tests
PYTHON -m pytest -v --junitxml=reports/tests.xml
PYTHON -m coverage run -m pytest -v
PYTHON -m coverage xml -o reports/coverage.xml
PYTHON -m coverage html -d reports/coverage-html
PYTHON -m coverage report
PYTHON -m bandit app.py deploy.py -f json -o reports/bandit.json
PYTHON deploy.py --target deployment
PYTHON deployment/app.py
```

## References

- Lab handout: `lab 10-jenkins.docx`
- [Jenkins Pipeline syntax](https://www.jenkins.io/doc/book/pipeline/syntax/)
- [Coverage execution](https://coverage.readthedocs.io/en/latest/commands/cmd_run.html)
- [Bandit command line](https://bandit.readthedocs.io/en/latest/man/bandit.html)
