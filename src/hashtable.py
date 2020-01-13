# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for i in key:
            hash = (hash * 33) + ord(i)
        return hash


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # print("key to insert: ", key)
        # print("value to insert: ", value)
        position = self._hash_mod(key)
        # print("position", position)
        if self.storage[position] is None:
            self.storage[position] = LinkedPair(key, value)
        else:
            current = self.storage[position]
            while current is not None:
                if current.key == key:
                    current.value = value
                    return self
                elif current.next is None:
                    current.next = LinkedPair(key, value)
                    return current.next
                else:
                    current = current.next

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        position = self._hash_mod(key)
        current = self.storage[position]
        while current is not None:
            if current.key == key:
                print("current", current.key)
                current = None
                # self.storage[position] = None
                print("should be None", current)
                return None
            current = current.next
        else: 
            print("Key is not found")
            
        print("Current key still there?", self.storage[position])


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        position = self._hash_mod(key)
        if self.storage[position] is not None:
            current = self.storage[position]
            while current is not None:
                if current.key == key:
                    return current.value
                current = current.next
                
        else: 
            print("Key is not found")
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for key in range(len(self.storage)):
            if self.storage[key]:
                new_storage[key] = self.storage[key]
        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # print(ht.remove("line_1"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
