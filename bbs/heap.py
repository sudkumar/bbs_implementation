#!/usr/bin/ python

from heapq import *

class Heap():
	"""Priprity heap for Skyline"""
	def __init__(self, rootNode):
		self.heap = []
		for key in rootNode.keys:
			heappush(self.heap, (key.mbr.priority(), key))

	'''
	remove the most priority element and returns it from heap
	'''
	def deleteMin(self):
		return heappop(self.heap)

	'''
	inserts a node into heap
	'''
	def enqueue(self, node):
		for key in node.keys:
			heappush(self.heap, (key.mbr.priority(), key))


	'''
	Heap size
	'''
	def size(self):
		return len(self.heap)