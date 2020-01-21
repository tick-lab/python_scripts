#!/usr/bin/env python
'''Read in newick formatted tree, midpoint root.
Use: python tree_midpoint_root.py mynewick.tre output.tre'''

import sys
import dendropy

tree = dendropy.Tree.get(path=sys.argv[1], schema="newick")

tree.reroot_at_midpoint(update_bipartitions=False)
tree.write(path=sys.argv[2], schema="newick")
