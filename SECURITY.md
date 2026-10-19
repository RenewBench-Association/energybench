# Security policy

## Supported versions

Security fixes are released for the latest minor version of `energybench`. Please upgrade to the
newest release before reporting a problem.

## Reporting a vulnerability

Please **do not** open a public issue for a security problem. Instead, report it privately through
[GitHub's private vulnerability reporting](https://github.com/RenewBench-Association/energybench/security/advisories/new).
If you cannot use GitHub, email renewbench@lists.kit.edu.

Please include:

- a description of the issue and its impact
- the steps or code needed to reproduce it
- the affected versions, if known

We aim to acknowledge reports within five working days and keep you informed until the issue is
resolved. With your permission, we will credit you in the advisory.

## Verifying releases

Every release on PyPI is published from GitHub Actions with
[Trusted Publishing](https://docs.pypi.org/trusted-publishers/) and carries
[PEP 740 attestations](https://docs.pypi.org/attestations/), which link each file to the exact
workflow run that built it.
