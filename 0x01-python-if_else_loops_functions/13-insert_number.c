#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function that inserts a number into a sorted singly linked list
 * @number: integer
 * @head: head of the list
 * Return:the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == 0)
	{
		return (0);
	}
	new->n = number;
	if (*head == 0 || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current->next && current->next->n <= number)
		current = current->next;

	new->next = current->next;
	current->next = new;
	return (new);
}
