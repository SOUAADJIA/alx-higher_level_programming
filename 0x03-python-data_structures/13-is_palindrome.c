#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int length = 0, left = 0, right = 0;
	int arr[4096];

	if (!head)
		return (0);
	current = *head;
	if (!*head || (*head)->next == NULL)
		return (1);

	/* Store values of linked list nodes in an array */
	for (length = 0; current; current = current->next, length++)
		arr[length] = current->n;

	/* Compare array elements to check for palindrome */
	for (left = 0, right = length - 1; left < right; left++, right--)
	{
		if (arr[left] != arr[right])
			return (0);
	}
	return (1);
}
