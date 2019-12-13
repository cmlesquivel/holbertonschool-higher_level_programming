#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
#include <string.h>

/**
 * print_dlistint - prints all elements of a dlistint_s
 * @list: pointer to head of list
 * Return: number of nodes
 */

size_t print_dlistint(const dlistint_t *list)
{
	const dlistint_t *aux;
	size_t size = 0;

	aux = list;

	while (aux != NULL)
	{
		printf("%d\n", aux->n);
		aux = aux->next;
		size++;
	}

	return (size);
}
