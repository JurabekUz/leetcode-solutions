### Algorithm

* Start DFS from the root with an empty path.
* Add the current node's value to the path.
* If the node is a leaf (`left` and `right` are `None`), add the path to the result.
* Otherwise, recursively visit the left and right children.
* Continue until all root-to-leaf paths are found.
* Return the result.
