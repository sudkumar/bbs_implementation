#!/usr/bin/ python

from heap import Heap

class BBS():
	"""class for Branch and Bound algorith"""
	def __init__(self, tree):
		self.tree = tree
		
	"""
	Get skylines from tree and return
	"""
	def skyline(self):
		# now create the priority heap for skylines with rTree.root
		prHeap = Heap(self.tree.root)
		# create empty skyline set
		skylines = []

		# initialize the comparision
		comparirions = 0
		# loop through heap untill it's not empty
		while prHeap.size() != 0:
			# 
			dominated = False
			# get the minimum heap key for next iteration
			# this is a (pripority, key) tuple
			heapItem = prHeap.deleteMin()
			
			# get the key value from heap item
			key = heapItem[1]

			# loop through all the skylines for dominance for this key
			for item in skylines:
				# check for dominance of key with items in skyline set
				comparirions += 1
				if(item.mbr.dominates(key.mbr)):
					# key is dominated by a skyline
					# so continue with another key
					dominated = True
					break
			if dominated:
				# key is domintated and is removed from heap
				# so continue with next key
				continue

			# key is not dominated 
			if(key.childNode != None):
				# we are not at leaf node
				# do the expansions
				prHeap.enqueue(key.childNode)
			else:
				# we are at leap and found a tuple, so insert it into skyline set
				skylines.append(key)	

		# now return the skyline set
		return skylines, comparirions
