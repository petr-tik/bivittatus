#include <stdio.h>

#include <Python.h>

static char module_docstring[] = "Toy extension module for CPython";
static char myfun_docstring[] = "Performs maths on numbers";

static PyObject *toymod_myfun(PyObject *self, PyObject *args)
{
	int first, second;
	if (!PyArg_ParseTuple(args, "ii", &first, &second))
		// expects 2 int in args, parses them into first and second;
		return NULL;
	int interim_power = 1;
	for (int i = 0; i < first; ++i) {
		interim_power *= second;
	}
	int result = first * second + interim_power;
	PyObject *ret = Py_BuildValue("i", result);
	return ret;
}

static PyMethodDef module_methods[] = {
    {"myfun", toymod_myfun, METH_VARARGS, myfun_docstring},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef toymod = {PyModuleDef_HEAD_INIT, "toy_mod",
				    module_docstring, -1, module_methods};

PyMODINIT_FUNC PyInit_toymod(void) { return PyModule_Create(&toymod); };
