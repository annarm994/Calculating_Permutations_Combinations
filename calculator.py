import math

def calculate_permutations(n, r):
    return math.perm(n, r)

def calculate_combinations(n, r):
    return math.comb(n, r)

def main():
    print("Permutations and Combinations Calculator")
    
    while True:
        try:
            n = int(input("Enter the total number of items (n): "))
            r = int(input("Enter the number of items to be chosen or arranged (r): "))

            if n < 0 or r < 0 or r > n:
                print("Error: n and r must be non-negative, and r must not be greater than n.")
                continue

            permutations = calculate_permutations(n, r)
            combinations = calculate_combinations(n, r)

            print(f"\nNumber of permutations P({n},{r}): {permutations}")
            print(f"Number of combinations C({n},{r}): {combinations}\n")
        
        except ValueError:
            print("Invalid input. Please enter integer values for n and r.")
        
        another = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
