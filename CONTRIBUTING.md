# Guide to contributing

This book is developed collaboratively and openly, here on GitHub. We accept comments, contributions and corrections from all.

## Current Project STATUS

**THIRD EDITION PUBLISHED**


## License and attribution

All contributions must be properly licensed and attributed. If you are contributing your own original work, then you are offering it under a CC-BY license (Creative Commons Attribution). You are responsible for adding your own name or pseudonym in the [Github Contributors](github_contrib.asciidoc) section, as attribution for your contribution.

If you are sourcing a contribution from somewhere else, it must carry a compatible license. The book will initially be released under a CC-BY-NC-ND license which means that contributions must be licensed under open licenses such as MIT, CC0, CC-BY, etc. You need to indicate the original source and original license, by including an asciidoc markup comment above your contribution, like this:

```asciidoc
////
Source: https://example.com/originaltext
License: CC0
Added by: @aantonop
////
```


## Contributing with a Pull Request

Please submit only PRs for errors that a non-domain-expert copy editor might miss. Do not submit PRs for typos, grammar and syntax, as those are part of the copy editors job. 

The best way to contribute to this book is by making a pull request:

1. Login with your GitHub account or create one now
2. [Fork](https://github.com/bitcoinbook/bitcoinbook#fork-destination-box) the `bitcoinbook` repository. Work on your fork.
3. Create a new branch on which to make your change, e.g. `git checkout -b my_code_contribution`, or make the change on the `develop` branch.
4. Please do one pull request *per asciidoc file*, to avoid large merges. Edit the asciidoc file where you want to make a change.
5. If you want attribution for your contribution, edit the file `meta/github_contrib.adoc` and add your own name to the list of contributors under the Acknowledgment section. Use your name, or a GitHub username, or a pseudonym. You are responsible for creating an attribution.
6. Commit your change. Include a commit message describing the correction.
7. Submit a pull request against the bitcoinbook repository.

## Contributing with an issue

If you find a mistake and you're not sure how to fix it, or you don't know how to do a pull request, then you can file an Issue. Filing an Issue will help us see the problem and fix it.

## Line endings

All submissions should use Unix-like line endings: LF (not CR, not CR/LF). All the postprocessing is done on Unix-like systems. Incorrect line endings, or changes to line endings cause confusion for the diff tools and make the whole file look like it has changed.

If you are unsure or your OS makes things difficult, consider using a developer's text editor such as VSCode.

## Thanks

We are very grateful for the support of the entire Bitcoin community. Thank you!
