#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info- C func that prints some basic inf about Python lists
 * @p: Python list object
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, allocated, i;
	PyObject *item;

	list = (PyListObject *)p;
	size = Py_SIZE(list);
	allocated = list->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
