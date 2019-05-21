#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <float.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - function prints info about a python list
 * @p: PyObject
 *
 * Return: none
 */
void print_python_list(PyObject *p)
{
	size_t len, i;
	PyListObject *pl = (PyListObject *)p;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}
	len = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %lu\n", len);
	printf("[*] Allocated = %lu\n", pl->allocated);
	for (i = 0; i < len; i++)
	{
		printf("Element %lu: %s\n", i, pl->ob_item[i]->ob_type->tp_name);
		if (PyBytes_Check((PyObject *)pl->ob_item[i]))
			print_python_bytes((PyObject *)pl->ob_item[i]);
		else if (PyFloat_Check((PyObject *)pl->ob_item[i]))
			print_python_float((PyObject *)pl->ob_item[i]);
	}
	fflush(stdout);
}

/**
 * print_python_bytes - function prints info about a Python Bytes object
 * @p: PyObject
 *
 * Return: none
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	unsigned long int i, size;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}
	size = (PyBytes_Size(p) > 10) ? 10 : PyBytes_Size(p);
	printf("  size: %lu\n", size);
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  trying string: %s\n", str);
	printf("  first %lu bytes:", size);
	for (i = 0; i < size; i++)
	{
		printf(" %02x", str[i] & 0xff);
	}
	printf("\n");
	fflush(stdout);
}

/**
 * print_python_float - function prints info about a Python Float Object
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
	double val;
	char *str;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
	fflush(stdout);
}
