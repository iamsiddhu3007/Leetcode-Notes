TrieNode class:

This is the basic unit of the Trie. Each node:
	•	Has a children dictionary to store the next characters.
	•	Has a endOfWord flag to indicate whether the node represents the end of a valid word.

⸻

Trie class:

This class represents the full Trie data structure. It uses TrieNode objects to store and search words.

⸻

__init__ method:
	•	Initializes the Trie.
	•	Sets self.root as the root node (an empty TrieNode) from which all words will begin.

⸻

insert(word) method:
	•	Takes a word as input.
	•	Goes through each character in the word one by one.
	•	If a character doesn’t exist in the current node’s children, it adds a new TrieNode for it.
	•	After inserting all characters, it marks the final node as the end of the word by setting endOfWord = True.

⸻

search(word) method:
	•	Takes a word as input.
	•	Goes through each character in the word.
	•	If any character is missing in the Trie, it returns False.
	•	If all characters are found, it checks if the last node is marked as the end of a word. If so, it returns True; otherwise, False.

⸻

startsWith(prefix) method:
	•	Takes a prefix as input.
	•	Goes through each character of the prefix.
	•	If any character is missing, it returns False.
	•	If all characters are found, it returns True, meaning there is at least one word in the Trie that starts with this prefix.

⸻

This structure is useful for fast word lookup, autocomplete features, and prefix-based searches.