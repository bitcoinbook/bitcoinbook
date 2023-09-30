# Guide to contributing

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/ethereumbook/Lobby)

This book is developed collaboratively and openly, here on GitHub. We accept comments, contributions and corrections from all.

## Current Project STATUS
**CONTENT FREEZE - FIRST EDITION IN PRODUCTION**

## Contributing with a Pull Request

Before contributing with a Pull Request, please read the current **PROJECT STATUS**.

If the current **PROJECT STATUS** is **CONTENT FREEZE**, please keep these points in mind;

* Please submit only PRs for errors that a non-domain-expert copy editor might miss. Do not submit PRs for typos, grammar and syntax, as those are part of the copy editors job.
* Please don't merge code. Any changes will have to be applied manually (by the Author) after copy edit and before final proof, if the copy editor doesn't catch the same errors.


## Chat with the authors

You can chat with the authors and editors on [Gitter chat](https://gitter.im/ethereumbook/Lobby).

## License and attribution

All contributions must be properly licensed and attributed. If you are contributing your own original work, then you are offering it under a CC-BY license (Creative Commons Attribution). You are responsible for adding your own name or pseudonym in the Acknowledgments section in the [Preface](preface.asciidoc), as attribution for your contribution.

If you are sourcing a contribution from somewhere else, it must carry a compatible license. The book will initially be released under a CC-BY-NC-ND license which means that contributions must be licensed under open licenses such as MIT, CC0, CC-BY, etc. You need to indicate the original source and original license, by including an asciidoc markup comment above your contribution, like this:

```asciidoc
////
Source: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20-token-standard.md
License: CC0
Added by: @aantonop
////
```

The best way to contribute to this book is by making a pull request:

1. Login with your GitHub account or create one now
2. [Fork](https://github.com/ethereumbook/ethereumbook#fork-destination-box) the `ethereumbook` repository. Work on your fork.
3. Create a new branch on which to make your change, e.g. `git checkout -b my_code_contribution`, or make the change on the `develop` branch.
4. Please do one pull request PER asciidoc file, to avoid large merges. Edit the asciidoc file where you want to make a change or create a new asciidoc file in the `contrib` directory if you're not sure where your contribution might fit.
5. Edit `preface.asciidoc` and add your own name to the list of contributors under the Acknowledgment section. Use your name, or a GitHub username, or a pseudonym.
6. Commit your change. Include a commit message describing the correction.
7. Submit a pull request against the ethereumbook repository.

Here's a video tutorial to help you make your first pull request:

[![Ethereum Book Pull Request Tutorial](https://img.youtube.com/vi/IBYHohWm_5w/0.jpg)](https://www.youtube.com/watch?v=IBYHohWm_5w)

## Contributing with an issue

If you find a mistake and you're not sure how to fix it, or you don't know how to do a pull request, then you can file an Issue. Filing an Issue will help us see the problem and fix it.

Create a [new Issue](https://github.com/ethereumbook/ethereumbook/issues/new) now!

## Heading styles normalization across the book

Adjust heading style in each section as follows:

1. Only the chapter/section should be level 2, everything else should be level 3 and below (level 1 is the book title itself). Each asciidoc file should start with a "==" heading.
2. All lower case, except for first letter, proper nouns and acronyms. "What is this thing?", "What is the Ethereum sprocket?" "Who created the Ethereum Name Service (ENS)"
3. Acronyms are spelled out, capitalized, with the acronym in parentheses. Once you have spelled out an acronym in one heading, we can keep it as an acronym in subsequent headings.
4. No period at the end. Question mark if it is a question (generally avoid question headings, unless really appropriate)
5. Should include a unique anchor (see #279), all lower case, underscore separated.
6. Headings should be followed by a blank line.
7. Heading should be followed by a paragraph of text, not a lower-level heading without any text. If you find one like this, add a TODO comment (line of 4 slashes "////", line with "TODO: add paragraph", line of 4 slashes)

## Line endings

All submission should use Unix-like line endings: LF (not CR, not CR/LF). All the postprocessing is done on Unix-like systems. Incorrect line endings, or changes to line endings cause confusion for the diff tools and make the whole file look like it has changed.

If you are unsure or your OS makes things difficult, consider using a developer's text editor such as Atom.

## Thanks

We are very grateful for the support of the entire Ethereum community. With your help, this will be a great book that can help thousands of developers get started and eventually "master" Ethereum. Thank you!
