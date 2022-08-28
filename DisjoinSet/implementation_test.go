// https://www.geeksforgeeks.org/disjoint-set-data-structures/
package main

import (
	"testing"
)

func TestDisjoinSet_Find(t *testing.T) {
	type fields struct {
		Items []*DisjoinSetItem
	}

	type args struct {
		itemIdex int
	}

	f1 := fields{
		Items: []*DisjoinSetItem{
			{Value: "1", ParentIdx: 5, Rank: 0}, // parent: 6
			{Value: "2", ParentIdx: 3, Rank: 0}, // parent: 4
			{Value: "3", ParentIdx: 3, Rank: 0}, // parent: 4
			{Value: "4", ParentIdx: 3, Rank: 2}, // parent: 4
			{Value: "5", ParentIdx: 4, Rank: 0}, // parent: 5
			{Value: "6", ParentIdx: 5, Rank: 1}, // parent: 6
			{Value: "7", ParentIdx: 8, Rank: 0}, // parent: 9
			{Value: "8", ParentIdx: 5, Rank: 0}, // parent: 6
			{Value: "9", ParentIdx: 3, Rank: 1}, // parent: 4
		},
	}

	tests := []struct {
		name          string
		fields        fields
		args          args
		wantParentIdx int
	}{
		{
			name:   "case 1.1",
			fields: f1,
			args: args{
				itemIdex: 6, // name: 7
			},
			wantParentIdx: 3,
		},
		{
			name:   "case 1.2",
			fields: f1,
			args: args{
				itemIdex: 2,
			},
			wantParentIdx: 3,
		},
		{
			name:   "case 1.3",
			fields: f1,
			args: args{
				itemIdex: 3,
			},
			wantParentIdx: 3,
		},
		{
			name:   "case 1.4",
			fields: f1,
			args: args{
				itemIdex: 7,
			},
			wantParentIdx: 5,
		},
		{
			name:   "case 1.5",
			fields: f1,
			args: args{
				itemIdex: 4,
			},
			wantParentIdx: 4,
		},
		{
			name:   "case 1.6",
			fields: f1,
			args: args{
				itemIdex: 0,
			},
			wantParentIdx: 5,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			d := &DisjoinSet{
				Items: tt.fields.Items,
			}
			if gotParentIdx := d.Find(tt.args.itemIdex); gotParentIdx != tt.wantParentIdx {
				t.Errorf("DisjoinSet.Find() = %v, want %v", gotParentIdx, tt.wantParentIdx)
			}
		})
	}
}

func TestDisjoinSet_Union(t *testing.T) {
	type fields struct {
		Items []*DisjoinSetItem
	}

	type args struct {
		item1Idx int
		item2Idx int
	}

	f1 := func() fields {
		return fields{
			Items: []*DisjoinSetItem{
				{Value: "1", ParentIdx: 5, Rank: 0}, // parent: 6
				{Value: "2", ParentIdx: 3, Rank: 0}, // parent: 4
				{Value: "3", ParentIdx: 3, Rank: 0}, // parent: 4
				{Value: "4", ParentIdx: 3, Rank: 2}, // parent: 4
				{Value: "5", ParentIdx: 4, Rank: 0}, // parent: 5
				{Value: "6", ParentIdx: 5, Rank: 1}, // parent: 6
				{Value: "7", ParentIdx: 8, Rank: 0}, // parent: 9
				{Value: "8", ParentIdx: 5, Rank: 0}, // parent: 6
				{Value: "9", ParentIdx: 3, Rank: 1}, // parent: 4
			},
		}
	}

	tests := []struct {
		name     string
		fields   fields
		args     args
		want     bool
		wantRoot int
	}{
		{
			name:   "case 1.1",
			fields: f1(),
			args: args{
				item1Idx: 7,
				item2Idx: 6,
			},
			want:     true,
			wantRoot: 3,
		},
		{
			name:   "case 1.2",
			fields: f1(),
			args: args{
				item1Idx: 4,
				item2Idx: 0,
			},
			want:     true,
			wantRoot: 5,
		},
		{
			name:   "case 1.3",
			fields: f1(),
			args: args{
				item1Idx: 7,
				item2Idx: 0,
			},
			want: false,
		},
		{
			name:   "case 1.4",
			fields: f1(),
			args: args{
				item1Idx: 5,
				item2Idx: 7,
			},
			want: false,
		},
		{
			name:   "case 1.5",
			fields: f1(),
			args: args{
				item1Idx: 1,
				item2Idx: 6,
			},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {

			d := &DisjoinSet{
				Items: tt.fields.Items,
			}

			if got := d.Union(tt.args.item1Idx, tt.args.item2Idx); got != tt.want {
				t.Errorf("DisjoinSet.Union() = %v, want %v", got, tt.want)
			}

			if tt.want {
				root1Idx, root2Idx := d.Find(tt.args.item1Idx), d.Find(tt.args.item2Idx)
				if root1Idx != tt.wantRoot || root2Idx != tt.wantRoot {
					t.Errorf("two items are not in the same set %v %v, want %v", root1Idx, root2Idx, tt.wantRoot)
				}
			}
		})
	}
}
