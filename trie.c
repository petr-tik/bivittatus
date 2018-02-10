#include <malloc.h>

#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

static char trie_docstring[] = "Trie extension module for CPython";

#define LETTERS 26 // english by default

typedef struct trie_node_t {
  struct trie_node_t *children[LETTERS];
  char letter;  // store the letter
  char is_word; // if sequence up to now is a word - set to 1, else 0
} trie_node_t;

#define trie_node_size sizeof(trie_node_t)

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

trie_node_t *add_node(char letter) {
  /*
     called when children[idx] returns a NULL pointer
     uses the recursive property of add_to_trie. If it fails and returns a
     NULL pointer, it will be written to the relevant index at
     node->children[] and the recursive call will try again.
  */
  trie_node_t *new_node = malloc(trie_node_size);
  if (new_node != NULL) {
    // avoid accessing null pointer
    new_node->is_word = 0;
    new_node->letter = letter;
    for (int idx = 0; idx < LETTERS; ++idx) {
      new_node->children[idx] = NULL;
    }
  }
  return new_node;
}

typedef struct {
  PyObject_HEAD;
  trie_node_t *head;

} trie;

static PyObject *trie_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
  trie *self;
  self = (trie *)type->tp_alloc(type, 0);

  if (self == NULL)
    return NULL;
  return (PyObject *)self;
}

static int trie_init(trie *self, PyObject *args, PyObject *kwds) {
  char empty = 'H';
  trie_node_t *head = add_node(empty);
  if (head == NULL)
    return -1;

  // copied the incref, xdecref pattern from
  // https://docs.python.org/3/extending/newtypes.html

  self->head = head;

  return 0;
}

int char_to_ascii(char letter) {

  int num = letter;
  return num - 97;
}

static char add_docstring[] = "Adds a word to the trie";
static PyObject *trie_add(trie *self, PyObject *args) {
  // Adds the word to the trie
  const char *word;
  int word_length = 0;
  if (!PyArg_ParseTuple(args, "s#", &word, &word_length))
    return NULL;

  trie_node_t *cur = self->head;

  for (int idx_in_word = 0; idx_in_word < word_length - 1; ++idx_in_word) {
    char letter = word[idx_in_word];
    int idx = char_to_ascii(letter);
    if (cur->children[idx] == NULL) {
      cur->children[idx] = add_node(letter);
    }
    cur = cur->children[idx];
  }
  // last letter needs to carry 1
  cur->is_word = 1;

  return Py_BuildValue(""); // returns None
}

static char find_docstring[] = "Returns 1/0 if word in trie or not";
static PyObject *trie_find(trie *self, PyObject *args) {
  const char *word;
  int word_length = 0;
  if (!PyArg_ParseTuple(args, "s#", &word, &word_length))
    return NULL;

  trie_node_t *cur = self->head;

  int ret = 0;
  int idx = 0;

  while (idx < word_length - 1 && cur != NULL) {
    char letter = word[idx];
    cur = cur->children[char_to_ascii(letter)];
    ++idx;
  }
  if (cur != NULL)
    ret = cur->is_word;
  return Py_BuildValue("i", ret);
}

static PyMethodDef trie_methods[] = {
    {"add", (PyCFunction)trie_add, METH_VARARGS, add_docstring},
    {"find", (PyCFunction)trie_find, METH_VARARGS, find_docstring},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef triemodule = {PyModuleDef_HEAD_INIT, "trie",
                                        trie_docstring, -1, trie_methods};

static PyTypeObject TrieType = {
    PyVarObject_HEAD_INIT(NULL, 0) "ctrie.cTrie", /* tp_name */
    sizeof(trie),                                 /* tp_basicsize */
    0,                                            /* tp_itemsize */
    0,                                            /* tp_dealloc */
    0,                                            /* tp_print */
    0,                                            /* tp_getattr */
    0,                                            /* tp_setattr */
    0,                                            /* tp_reserved */
    0,                                            /* tp_repr */
    0,                                            /* tp_as_number */
    0,                                            /* tp_as_sequence */
    0,                                            /* tp_as_mapping */
    0,                                            /* tp_hash  */
    0,                                            /* tp_call */
    0,                                            /* tp_str */
    0,                                            /* tp_getattro */
    0,                                            /* tp_setattro */
    0,                                            /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,     /* tp_flags */
    "Trie objects",                               /* tp_doc */
    0,                                            /* tp_traverse */
    0,                                            /* tp_clear */
    0,                                            /* tp_richcompare */
    0,                                            /* tp_weaklistoffset */
    0,                                            /* tp_iter */
    0,                                            /* tp_iternext */
    trie_methods,                                 /* tp_methods */
    0,                                            /* tp_members */
    0,                                            /* tp_getset */
    0,                                            /* tp_base */
    0,                                            /* tp_dict */
    0,                                            /* tp_descr_get */
    0,                                            /* tp_descr_set */
    0,                                            /* tp_dictoffset */
    (initproc)trie_init,                          /* tp_init */
    0,                                            /* tp_alloc */
    trie_new,                                     /* tp_new */
};

PyMODINIT_FUNC PyInit_ctrie(void) {

  PyObject *m;

  if (PyType_Ready(&TrieType) < 0)
    return NULL;

  m = PyModule_Create(&triemodule);
  if (m == NULL)
    return NULL;

  Py_INCREF(&TrieType);
  PyModule_AddObject(m, "cTrie", (PyObject *)&TrieType);
  return m;
};
