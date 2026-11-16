# Lab 10 report

Name: Omar Khalil  
GitHub: omk166  
Repository: https://github.com/omk166/OmarKhalil_lab10

## Changes

The Part 3 pipeline is implemented in `Jenkinsfile_Omar_Khalil`. It creates a
virtual environment, installs dependencies, lints Python code, tests the
personalized greeting, and deploys a runnable copy of the application.
The greeting and its test both use `Hello, World from Omar Khalil!`, correcting
the mismatch between the starter application and the handout's expected test.
The requirements include pytest as well as the added analysis tools.

For Part 4, the Coverage stage measures both statements and branches for
`app.py` and `deploy.py`. It exports XML and HTML reports and enforces 100%
coverage. The Security Scan stage runs Bandit on both production files and
fails on findings. The Deploy stage copies the application into a local
deployment directory and executes that copy. Tests also verify redeployment
replaces an outdated application. Jenkins archives the deployment and reports
before cleaning its workspace.

## Local verification

Run on Windows with Python 3.13.7 using the pinned requirements:

| Check | Observed result |
| --- | --- |
| flake8 | Passed, no violations |
| pytest | 6 passed |
| coverage | 22 statements and 4 branches covered; 100% total |
| Bandit | Passed, no findings |
| deployment | Created deployment/app.py and executed successfully |

Observed coverage output:

```text
Name        Stmts   Miss Branch BrPart  Cover
--------------------------------------------
app.py          6      0      2      0   100%
deploy.py      16      0      2      0   100%
--------------------------------------------
TOTAL          22      0      4      0   100%
```

Observed deployed application output:

```text
Hello, World from Omar Khalil!
```

## Jenkins build

Jenkins build verification is in progress. Local results above are actual
Python command results, rather than Jenkins build output.
