/*

Author : Shuvam Kumar Singh
Date : 31/01/2024
Problem : Insert and Search in a Trie
Difficulty : Medium

*/


class Solution
{
    public:
        //Function to insert string into TRIE.
        void insert(struct TrieNode *root, string key)
        {
            for(auto i : key){
                if(root -> children[i - 'a']){
                    root = root -> children[i - 'a'];
                }
                else{
                    TrieNode * new_node = getNode();
                    root -> children[i - 'a'] = new_node;
                    root = new_node;
                }
            }
            
            root -> isLeaf = 1;
        }
        
        //Function to use TRIE data structure and search the given string.
        bool search(struct TrieNode *root, string key) 
        {
            for(auto i : key){
                if(root -> children[i - 'a']){
                    root = root -> children[i - 'a'];
                }
                else{
                    return 0;
                }
            }
            
            return root -> isLeaf;
        }
};
