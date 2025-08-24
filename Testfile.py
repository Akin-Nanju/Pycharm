# even_filter.py

def get_even_numbers(numbers):
    """Return a list of even numbers from the input list."""
    return [num for num in numbers if num % 2 == 0]

def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_nums = get_even_numbers(nums)

    print(f"Even numbers: {even_nums}")

    # Save to file
    with open("even_numbers.txt", "w") as f:
        for num in even_nums:
            f.write(f"{num}\n")

    print("Even numbers saved to even_numbers.txt!")

if __name__ == "__main__":
    main()
