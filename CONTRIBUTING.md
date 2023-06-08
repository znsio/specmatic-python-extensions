# Contributing

Thanks for being willing to contribute!

## Project setup

1. Fork and clone the repo
2. Install Python > 3.8
3. Run `pip install -r requirements.txt` project root folder to install dependencies
4. Create a branch for your PR with `git checkout -b your-branch-name`

> Tip: Keep your `main` branch pointing at the original repository and make
> pull requests from branches on your fork. To do this, run:
>
> ```
> git remote add upstream https://github.com/znsio/specmatic-python-extensions.git
> git fetch upstream
> git branch --set-upstream-to=upstream/main main
> ```
>
> This will add the original repository as a "remote" called "upstream," Then
> fetch the git information from that remote, then set your local `main`
> branch to use the upstream main branch whenever you run `git pull`. Then you
> can make all of your pull request branches based on this `main` branch.
> Whenever you want to update your version of `main`, do a regular `git pull`.


## Committing and Pushing changes

Please make sure to run the tests before you commit your changes by using the command

```pytest test -v -s```


## Build and Release Process
There are two builds as of now:
- A CI build named: 'Run tests on different Python 🐍 versions and operating systems.' which is run on every checkin into the main branch.
- A 'publish' build named: 'Publish Python 🐍 distributions 📦 to PyPI and TestPyPI' which creates a python distribution for the current release and uploads it to PyPI.
### To create a new release:
1. Update the `````__version__````` property in `````specmatic/version.py````` file to the required version and check it in.
2. Ensure that the subsequent CI build is green.
3. Navigate to the 'Releases' page: https://github.com/znsio/specmatic-python-extensions/releases
4. Click on 'Draft a new release'
5. Click on the 'Choose Tag' dropdown list and manually enter the version that was used in Step1.
6. Set the Release title as 'v<Version>' ( For example: v0.4.7)
7. Add release notes.
8. Click on 'Publish Release' (This will kick off the 'publish' build).


## Help needed

Please checkout the [the open issues](https://github.com/znsio/specmatic-python-extensions/issues?q=is%3Aopen+is%3Aissue)

Also, please watch the repo and respond to questions/bug reports/feature
requests! Thanks!
