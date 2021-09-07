#include "lists.h"
/**
* check_cycle - Checks if a singly linked list has a cycle in it
*
* @list: Singly Linked List
*
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *now = list;
	listint_t *tmp = list;

	while (tmp && tmp->next)
	{
		now = now->next;
		tmp = tmp->next->next;
		if (now == tmp)
			return (1);
	}
	return (0);
}
