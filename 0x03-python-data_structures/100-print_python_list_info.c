#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function prints info about a python list
 * @p: PyObject
 *
 * Return: none
 */
void print_python_list_info(PyObject *p)
{
	size_t len = PyList_Size(p), i;
	PyListObject *pl = (PyListObject *)p;

	printf("[*] Size of the Python List = %lu\n", len);
	printf("[*] Allocated = %lu\n", pl->allocated);
	for (i = 0; i < len; i++)
		printf("Element %lu: %s\n", i, Py_TYPE(pl->ob_item[i])->tp_name);
}
