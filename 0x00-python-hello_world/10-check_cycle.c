#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	const listint_t *current;

	if (list != NULL)
	{
		current = list;
		while (current != NULL)
		{
			current = current->next;
			if (current == list)
			{
				return (1);
			}
		}
		return (0);

	}
	return (0);
}
