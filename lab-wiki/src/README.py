"""generates the graphs in README.md for docs"""
from asciitree import LeftAligned
from collections import OrderedDict as OD

# this only preserves ordering for Python 3.6+
tree = {
    'reference_library': OD(
        computer_vision=OD(
            object_classification={},
            object_detection={}),
        machine_learning=OD(
            learning_theory={}
        )
    )
}

tree_cv_classification = {
    'object_classification': OD(
        [('_data  # for storing images, additional notes, etc. for note files', {}),
         ('cnn-residual.ipynb  # notes for ResNet-related papers', {}),
         ('cnn-linear.ipynb  # notes for linear CNN papers, such as AlexNet, VGG', {})]
    )
}

tr = LeftAligned()
print(tr(tree))
print(tr(tree_cv_classification))
