#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * list_len - function returns the length of a singly linked list
 * @head: head of list
 *
 * Return: length of list
 */
int list_len(listint_t *head)
{
	int i;

	for (i = 0; head; i++)
		head = head->next;
	return (i);
}

/**
 * is_palindrome - function checks if a singly linked list is a palindrome
 * @head: head of list
 *
 * Return: 1 if it is, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len, i, *arr;
	listint_t *tmp = *head;

	if (!*head)
		return (1);
	len = list_len(*head);
	if (len == 1)
		return (1);
	arr = malloc(sizeof(int) * len / 2);
	if (!arr)
		return (0);
	for (i = 0; i < len / 2; i++)
	{
		arr[i] = tmp->n;
		tmp = tmp->next;
	}
	if (len % 2 != 0)
		tmp = tmp->next;
	i--;
	while (tmp && i != -1)
	{
		if (tmp->n != arr[i])
			return (0);
		tmp = tmp->next;
		i--;
	}
	return (1);
}
