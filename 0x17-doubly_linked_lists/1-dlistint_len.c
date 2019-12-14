#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * dlistint_len - function that returns the number of elements in a linked list
 * @h: variable type dlistint_t
 * Return: the number of the nodes
 */

size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *aux;
	size_t my_counter = 0;

	aux = h;

	while (aux != NULL)
	{
		my_counter++;
		aux = aux->next;
	}

	return (my_counter);
}
