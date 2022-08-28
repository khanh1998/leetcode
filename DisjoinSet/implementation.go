// https://www.geeksforgeeks.org/disjoint-set-data-structures/
package main

import "strconv"

type DisjoinSetItem struct {
	Value     string
	ParentIdx int // parent index start from 0
	Rank      int
}

type DisjoinSet struct {
	Items []*DisjoinSetItem
}

// NewDisjoinSet create new n sets, each set has just one item.
func NewDisjoinSet(n int) DisjoinSet {
	var ds DisjoinSet

	// init data
	for i := 0; i < n; i++ {
		ds.Items = append(ds.Items, &DisjoinSetItem{
			Value:     strconv.FormatInt(int64(i+1), 10),
			ParentIdx: i, // initially, it doesn't have a parent, its parent is it own
			Rank:      0, // how deep it is from the current item, initially, 0
		})
	}

	return ds
}

// Find the root parent of i'th item
func (d *DisjoinSet) Find(itemIdx int) (parentIdx int) {
	for {
		currParentName := d.Items[itemIdx].ParentIdx
		if currParentName == itemIdx {
			parentIdx = currParentName

			return parentIdx
		}

		itemIdx = currParentName
	}
}

func (d *DisjoinSet) Union(item1Idx int, item2Idx int) bool {
	root1Idx, root2Idx := d.Find(item1Idx), d.Find(item2Idx)

	if root1Idx == root2Idx { // item 1 and item 2 are in the same set already
		return false
	}

	root1, root2 := d.Items[root1Idx], d.Items[root2Idx]
	if root1.Rank < root2.Rank {
		root1.ParentIdx = root2Idx
	}

	if root1.Rank > root2.Rank {
		root2.ParentIdx = root1Idx
	}

	if root1.Rank == root2.Rank {
		root2.ParentIdx = root1Idx
		root1.Rank += 1
	}

	return true
}

func main() {
	ds := NewDisjoinSet(10)
	ds.Find(1)
}
