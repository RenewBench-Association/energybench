# Releasing `energybench`

This guide is for the core release team. Everyone else contributes through pull requests, as
described in [CONTRIBUTING.md](CONTRIBUTING.md).

## Who can release

Publishing is started by pushing to two branches, `release-test` and `release`. GitHub enforces
who may do that:

- **Branch ruleset on `release` and `release-test`.** Nobody can create, update or delete these
  branches except members of the core release team, the
  [`@RenewBench-Association/energybench-release`](https://github.com/orgs/RenewBench-Association/teams/energybench-release)
  GitHub team.
- **The `release` environment** holds the release bot's credentials, and only the `release`
  branch can use it.
- **The `pypi` and `testpypi` environments.** Only the `release` and `release-test` branches
  respectively can publish through them, and a team member approves each PyPI upload. PyPI and
  TestPyPI accept uploads only from these workflows (Trusted Publishing).
- **The gate in `release.yml`** runs before anything is created. A version is only published from
  its own release commit, and only if the release test has passed on exactly that commit.

## Steps

1. **Prepare the release.**

   ```bash
   git switch main && git pull
   git push origin main:release
   ```

   [release-please](https://github.com/googleapis/release-please) opens or updates a release pull
   request against `main`. It contains the new version number and the new `CHANGELOG.md` entry.
   See [How release-please decides what to release](#how-release-please-decides-what-to-release).
   This push publishes nothing, so it needs no release test.

2. **Review and merge** the release pull request. Its squash commit on `main` is the **release
   commit**.

3. **Test the release commit.** This step is required.

   ```bash
   git pull
   release_sha="$(git log -1 --format=%H -- .release-please-manifest.json)"
   git push origin "$release_sha:release-test"
   ```

   This publishes a unique pre-release build of the new version (for example `0.5.0.dev42`) to
   TestPyPI. It then installs that build with pip on Linux, macOS and Windows with every supported
   Python version, and runs the tests against it. Wait until the *Release test* workflow is green.

4. **Publish the release commit.**

   ```bash
   git push origin "$release_sha:release"
   ```

   - Before anything is created, the workflow checks two things: the pushed commit is the release
     commit, and the release test passed on it. Otherwise it stops.
   - release-please then tags the release commit and creates a draft GitHub Release. Its notes are
     the new `CHANGELOG.md` entry.
   - The package is built from that tag, with GitHub build-provenance attestations. After a team
     member approves the `pypi` deployment, it is uploaded to PyPI through Trusted Publishing, with
     PEP 740 attestations.
   - Only after PyPI accepts it, the same wheel and sdist are attached to the GitHub Release and
     the draft is published. Every GitHub Release therefore matches a PyPI version, file for file.
   - Read the Docs publishes the docs for the new version, and Zenodo archives it with a DOI.

Pushing the release commit works even if more pull requests were merged after it. Those changes go
into the next release. If `release` or `release-test` points at a newer commit than the one you
push, add `--force`. Never edit the version number or `CHANGELOG.md` by hand.

### If something fails

- **The gate says the release test has not passed.** Push the release commit to `release-test`
  (step 3) and wait for a green run. Then open the failed *Release* run in the Actions tab and
  click **Re-run all jobs**. Pushing to `release` again does nothing: the branch already points at
  that commit, so Git reports "Everything up-to-date" and no workflow starts.
- **The gate says the pushed commit is not the release commit.** Push the commit it names, as in
  steps 3 and 4.
- **A later job fails** (for example the PyPI upload). The tag and a *draft* GitHub Release
  already exist, but nothing is public. Fix the cause, then click **Re-run failed jobs** on that
  run. Do not push a new version.

## How release-please decides what to release

Merging pull requests into `main` never changes the version. You can merge fifty pull requests and
the version stays the same. release-please only acts when you push to `release`. It then reads the
titles of all pull requests merged since the last release and does three things.

1. **Choose one new version** for all of those changes together. A version has three numbers,
   such as 0.4.2. The most significant change decides which one goes up:
   - any breaking change (`!`): the first number, 1.4.2 → 2.0.0. Before 1.0, the middle number
     instead: 0.4.2 → 0.5.0.
   - otherwise, any `feat`: the middle number, 0.4.2 → 0.5.0
   - otherwise, any `fix`, `perf`, `docs` or `revert`: the last number, 0.4.2 → 0.4.3
   - if only hidden types were merged (`chore`, `ci`, …), there is nothing to release, and no
     release pull request opens

2. **Write the changelog entry**: one line per pull request title, under the headings listed in
   [CONTRIBUTING.md](CONTRIBUTING.md#commit-messages-and-pull-requests), with links to the pull
   request and the commit. The same text becomes the GitHub Release notes.

3. **Put both into the release pull request.** If one is already open, it is updated rather than
   duplicated.

For example, say three pull requests were merged since 0.4.2:

- `feat: add search`
- `feat: add data loading`
- `fix: typo in an error message`

Pushing to `release` opens a release pull request for **0.5.0**. Its changelog lists two Features
and one Bug Fix.

**To use a different version number**, add a line such as `Release-As: 0.4.3` at the end of a
pull request's description before merging it. Squash merging copies the description into the commit
on `main`, and the next release uses exactly that number.

**To reword a changelog line** after its pull request was merged, edit that pull request's
description and add:

```text
BEGIN_COMMIT_OVERRIDE
feat: add Catalog.search with server-side filtering
END_COMMIT_OVERRIDE
```

The next push to `release` uses this text instead of the original title.
