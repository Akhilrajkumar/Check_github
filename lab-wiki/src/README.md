# lab wiki website

This document explains how to update the website part of the lab wiki.

unless otherwise indicated, `/` means the root of the website. As of 06/12/2017, this refers to <https://github.com/leelabcnbc/lab-wiki/blob/master/src>


## Must read for contributing

* **reference library -> how to contribute**

## How to update website files after content update.

**THIS IS NOT NEEDED ANYMORE, AS WEBSITE BUILDING IS DONE BY CIRCLECI**

This has been tested on Mac OS X 10.12. Should work on Linux as well. The steps below assume the current working directory is the root of the repository, not the root of the website.

### Dependencies

* Python 3.6
* after installation, run `pip install -r requirements.txt`.

### How to run it

Just run `python builder/leelab_wiki_builder.py`. This would update all the non source files of the website, mainly `.html` and `.bib` ones.


## reference library

all the files are stored under `/reference_library`, which I will call "library root" below.

### structure

under library root, there's a tree structure of nested categories, organized as folders.

For example, if the library has some computer vision papers on object detection, object classification, as well as some machine learning papers on learning theory, then the tree structure should look like as follows

~~~
reference_library
 +-- computer_vision
 |   +-- object_classification
 |   +-- object_detection
 +-- machine_learning
     +-- learning_theory
~~~

Under folder of each (intermediate or final) category, there is a set of "note" files storing notes about this particular category. All note files must be of type `.ipynb` (that is, Jupyter Notebook. `.ipynb` doesn't necessarily mean it must be in Python. Most of the time, we just use it for writing MarkDown with MathJax support). For example, under `computer_vision/object_classification`, there can be the following files.

~~~
object_classification
 +-- _data  # for storing images, additional notes, etc. for note files
 +-- cnn-residual.ipynb  # notes for ResNet-related papers
 +-- cnn-linear.ipynb  # notes for linear CNN papers, such as AlexNet, VGG
~~~

folders as `_data` are used to store additional files for `.ipynb` files, such as figures from important papers, hand-drawn schematics, etc. Such folders have to start with `_` so they don't get confused with a subcategory.

#### caveats on structure

It's not the case that all the final, "leaf" categories must end at level 2, or they must end at the same level. For example, it's OK to have more refined categories within `computer_vision/object_classification`, such as `computer_vision/object_classification/SIFT`, `computer_vision/object_classification/CNN`, etc. The only caveats is that, you cannot name a category arbitrarily. Most importantly, you cannot name a category starting with `_`, which will be preserved for other purposes, such as storing image files for note files of a certain category. `_` is used to differentiate a subcategory and a folder for storing files of current category.

### what's inside a note file

A note file is overall free form, containing whatever you want to say about certain papers. However, to facilitate easier searching and organization, as well as easier citation when writing papers, for each paper you talk about, you should also provide a [BibTeX format](https://en.wikipedia.org/wiki/BibTeX) citation entry for it. This would allow the papers to be aggregated into `.bib` files, and these `.bib` files can be presented nicely using services like [BibBase](http://bibbase.org/).

If you use any decent reference manager, it would support exporting citations as BibTeX format. Google Scholar also supports exporting as BibTeX.

#### example

for some example, check files already in it. Such as <https://github.com/leelabcnbc/lab-wiki/blob/master/src/reference_library/machine_learning/neural_networks/notes.ipynb>

#### caveats on BibTeX entry

When putting the BibTeX entry in the note files, you must use a code block starting exactly with `~~~\n@`, and ending exactly with `~~~`, **one for each paper**. Check <https://github.com/leelabcnbc/lab-wiki/blob/master/builder/leelab_wiki_builder.py#L16> on exactly what part of the note file gets interpreted as a BibTeX entry. If your note contains code block, make sure it doesn't get parsed as a BibTeX entry.

### multi category papers

One big problem with the tree structured categories, is that there is no way to assign one paper to two different categories. While you can duplicate a paper's note and the BibTeX entry for different categories, it would be a nightmare to update, and it's inelegant overall.

We can partially solve this problem (<https://github.com/leelabcnbc/lab-wiki/issues/2>), using special fields in the BibTeX entries.

We can have an optional custom field, called **`additional-categories`**, which is a comma separated value, such as `computer_vision/object_classification, machine_learning/neural_network`. We can in theory write some BibTeX parsing program to assign one paper to multiple different `bib` files, based on this field.

#### keywords

A commonly BibTeX field for assigning one entry to multiple categories is `keywords`. This is used by many reference managers as well, such as JabRef and Papers. I don't want to use `keywords` for assigning a paper to multiple categories. Instead, it should be used for what it literally means: keywords, such as `V1`, `V2`, `representation learning`, etc. These keywords are orthogonal to categories, and there's no hierarchy in keywords.

#### example

* For additional categories, check "Wide Residual Networks" in <https://github.com/leelabcnbc/lab-wiki/blob/master/src/reference_library/machine_learning/neural_networks/notes.ipynb>. It has some additional categories, such as `computer_vision/image_classification`.
* For keywords, essentially every paper in the library has one or two.

### how to contribute

1. On the GitHub website, create a new branch for you to work on. Two ways to do this.
   1) create a new branch from `master` branch of the repo.
   2) (recommended) fork the the whole repo into your personal account, and work on the `master` branch of your forked repo.
2. `git clone` the repo locally (either this repo or your forked one),
    and then `git checkout` to the branch you just create online (only if you don't fork).
3. update note files in that branch locally on your computer, and update the data on GitHub by `git push`.
4. create a pull request merging your branch into `master`. It must pass two types of checks before getting merged.
   * There is a system to automatically check that, after your update, the website can build.
      * In addition, I've configured the repo such that your branch must be up to date.
      This is a workaround to a defect in CircleCI
      See [here](https://discuss.circleci.com/t/pull-requests-not-triggering-build/1213).
      If you fork this repo, then this workaround is unnecessary.
   * Someone will review the content.
      * When reviewing, remember to check the output of the CI (`TEST -> builder/compare.sh`),
        making sure that people don't forget adding BibTeX entries.
   * The results two types of checks can be found on the page about your pull request.
5. Finally, you contribution get merged into `master`, and the website got updated.


#### if you don't have time to write note for some papers.

Then please don't modify the repo, which won't be much useful with a pile of pure references without notes. Instead, create an issue in the lab wiki repo, with label `library`, to make sure you don't forget it later. See <https://github.com/leelabcnbc/lab-wiki/issues/13> for an example.
