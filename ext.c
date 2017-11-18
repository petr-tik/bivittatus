#include <stdio.h>

#include <Python.h>

static char module_docstring[] = "Trie extension module for CPython";

/*

Make a trie class, so we can add and look up words in the trie. Delete later -
who ever uses delete?

>>> trie = Trie()
>>> trie.add("bob")
>>> trie.find("bob")
>>> True
>>> trie.find("alice")
>>> False


*/

static char add_docstring[] = "Adds a word to the trie";

static PyObject *trie_add(PyObject *self, PyObject *args) {
  // Adds the word to the trie
  char word[20];
  if (!PyArg_ParseTuple(args, "s", &word))
    return NULL;

  return Py_BuildValue("i", 1);
}

static PyMethodDef module_methods[] = {
    {"add", trie_add, METH_VARARGS, add_docstring}, {NULL, NULL, 0, NULL}};

static struct PyModuleDef trie = {PyModuleDef_HEAD_INIT, "trie",
                                  module_docstring, -1, module_methods};

PyMODINIT_FUNC PyInit_trie(void) { return PyModule_Create(&trie); };
