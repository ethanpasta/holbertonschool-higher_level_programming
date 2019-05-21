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
	if (!PyList_CheckExact(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	len = ((PyVarObject *)p)->ob_size;
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
}

/**
 * print_python_bytes - function prints info about a Python Bytes object
 * @p: PyObject
 *
 * Return: none
 */
void print_python_bytes(PyObject *p)
{
	int check = ((PyVarObject *)p)->ob_size;
	char *str;
	unsigned long int i, size;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!check)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = p->ob_refcnt;
	printf("  size: %lu\n", size);
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  trying string: %s\n", str);
	printf("  first %lu bytes:", (size <= 10) ? size + 1 : 10);
	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf(" %02x", str[i] & 0xff);
	}
	printf("\n");
}

/**
 * print_python_float - function prints info about a Python Float Object
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
	double val;

	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = PyFloat_AsDouble(p);
	if ((long int)val - val == 0)
		printf("  value: %.1f\n", val);
	else
		printf("  value: %.16g\n", val);
}
