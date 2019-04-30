#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function inserts a number into a sorted singly linked list
 * @head: head of list
 * @number: new number to add to list
 *
 * Return: address of new node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *new;

	if (number < tmp->n)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);
		new->n = number;
		new->next = tmp;
		tmp = new;
		return (new);
	}
	while (tmp->next && number > tmp->next->n)
		tmp = tmp->next;
	printf("Im here: %d\n", tmp->n);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = tmp->next;
	tmp->next = new;
	return (new);
}
