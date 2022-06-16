
type node struct {
	char_map [26]*node
	eow bool
}

type Trie struct {
	root *node
}

func Constructor() Trie {
	trie := Trie{root: new(node)}
	return trie
}

func (this *Trie) Insert(word string) {
	trev := this.root
	for _, key := range word {
		if trev.char_map[key - 97] == nil {
			trev.char_map[key - 97] = new(node)
		}
		trev = trev.char_map[key - 97]
	}
	trev.eow = true
}

func (this *Trie) searchPrefix(word string) *node {
	trev := this.root
	for _, key := range word {
		if trev.char_map[key - 97] == nil {
			return nil
		}
		trev = trev.char_map[key - 97]
	}
	return trev
}

func (this *Trie) StartsWith(prefix string) bool {
	target := this.searchPrefix(prefix)
	return target != nil
}

func (this *Trie) Search(word string) bool {
	target := this.searchPrefix(word)
	if target == nil {
		return false
	}
	return target.eow
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */