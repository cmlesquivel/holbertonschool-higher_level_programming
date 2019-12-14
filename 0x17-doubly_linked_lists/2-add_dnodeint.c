#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * dlistint_len - function that returns the number of elements in a linked list
 * @h: variable type dlistint_t
 * Return: the number of the nodes
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int number)
{
	dlistint_t *new_node;

	new_node = (dlistint_t)malloc(sizeof(dlistint_t));

	new_node->n = number;
	new_node->next = NULL;
	new_node->prev = NULL;

	if(*head == NULL)
	{
		head = new_node;
	}
	else
	{
		new_node->next= head;
	}

	return (new_node);
}
