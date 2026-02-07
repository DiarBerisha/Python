set1 = {1,2,3}
set2 = {3,4,5}

union_result = set1.union(set2)  # Combines all unique elements from both sets
union_result_operator = set2 | set1  # Union using the | operator

print(union_result)
print(union_result_operator)

intersection_result = set1.intersection(set2)  # Returns elements common to both sets
intersection_result_operator = set1 & set2  # Intersection using the & operator

print(intersection_result)
print(intersection_result_operator)

difference_result = set1.difference(set2)  # Returns elements in set1 that are not in set2
difference_result_operator = set2 - set1  # Returns elements in set2 that are not in set1

print(difference_result)
print(difference_result_operator)

symmetric_difference_result = set1.symmetric_difference(set2)  # Returns elements in either set but not in both
symmetric_difference_operator = set2 ^ set1  # Symmetric difference using the ^ operator

print(symmetric_difference_result)
print(symmetric_difference_operator)




set3 = {1,2,3}

set3.add(4)  # Adds an element to the set
print(set3)

set3.remove(3)  # Removes a specific element from the set (raises an error if not found)
print(set3)

set3.discard(5)  # Removes an element if it exists, without raising an error
print(set3)

set3.clear()  # Removes all elements from the set
print(set3)

my_list = [1,2,3,3,4,4,5]

unique_set = set(my_list)  # Converts the list to a set to remove duplicate values
unique_array = list(unique_set)  # Converts the set back


user1_interests = {"music", "movies", "travel"}
user2_interests = {"movies", "cooking", "reading"}

common_interests = user1_interests.intersection(user2_interests)
print(common_interests)


cooking = "cooking"
movies = "movies"
print(movies in user1_interests)
print(cooking in user1_interests)

print(movies not in user1_interests)
print(cooking not in user1_interests)

customer_names = {"Diar", "Donart", "Alea"}
diar = "Diar"

print(diar in customer_names)
