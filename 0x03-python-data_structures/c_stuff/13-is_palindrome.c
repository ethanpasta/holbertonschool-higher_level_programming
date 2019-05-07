#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * list_len - function returns the length of a singly linked list
 * @head: head of list
 *
 * Return: length of list
 */
void reverse_list(listint_t **head)
{
	listint_t *tmp = *head, *next = NULL, *prev = NULL;

	while (tmp != NULL)
	{
		next = tmp->next;
		tmp->next = prev;
		prev = tmp;
		tmp = next;
	}
	*head = prev;
}

/**
 * is_palindrome - function checks if a singly linked list is a palindrome
 * @head: head of list
 *
 * Return: 1 if it is, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *mid = *head;

	if (!*head || (*head)->next == NULL)
		return (1);
	while (mid && fast && fast->next)
	{
		mid = mid->next;
		fast = fast->next->next;
	}
	reverse_list(&mid);
	fast = *head;
	while (fast && mid)
	{
		if (fast->n != mid->n)
			return (0);
		fast = fast->next;
		mid = mid->next;
	}
	return (1);
}
