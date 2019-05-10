#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_list - function prints info about a python list
 * @p: PyObject
 *
 * Return: none
 */
void print_python_list(PyObject *p)
{
	size_t len = PyList_Size(p), i;
	PyListObject *pl = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", len);
	printf("[*] Allocated = %lu\n", pl->allocated);
	for (i = 0; i < len; i++)
	{
		printf("Element %lu: %s\n", i, pl->ob_item[i]->ob_type->tp_name);
		if (PyBytes_Check((PyObject *)pl->ob_item[i]))
			print_python_bytes((PyObject *)pl->ob_item[i]);
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
	int check = PyBytes_Check(p);
	char *str;
	unsigned long int i, size;

	printf("[.] bytes object info\n");
	if (!check)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %lu\n", size);
	str = PyBytes_AsString(p);
	printf("  trying string: %s\n", str);
	printf("  first %lu bytes:", (size <= 10) ? size + 1 : 10);
	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf(" %02x", str[i] & 0xff);
	}
	printf("\n");
}
