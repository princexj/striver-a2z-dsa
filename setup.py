import os

folders = [
    "01_learn_the_basics",
    "02_sorting_techniques",
    "03_arrays",
    "04_binary_search",
    "05_strings",
    "06_linked_list",
    "07_recursion",
    "08_bit_manipulation",
    "09_stack_and_queues",
    "10_sliding_window_two_pointer",
    "11_heaps",
    "12_greedy_algorithms",
    "13_binary_trees",
    "14_binary_search_trees",
    "15_graphs",
    "16_dynamic_programming",
    "17_tries",
    "18_strings_advanced"
]

print("START")

for folder in folders:
    print("Creating:", folder)
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "README.md"), "w") as f:
        f.write(f"# {folder}\n")

print("DONE")