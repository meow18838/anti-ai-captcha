import sys

def poison_captcha(clean_solution: str, chunk_size: int = 3) -> str:
    special_char = '\u2067'
    
    chunks = []
    for i in range(0, len(clean_solution), chunk_size):
        chunks.append(clean_solution[i:i + chunk_size])
    
    result = []
    for chunk in reversed(chunks):
        result.append(special_char + chunk)
    
    return ''.join(result)

def main():
    if len(sys.argv) > 1:
        solution = sys.argv[1]
    else:
        solution = input().strip()
    
    poisoned = poison_captcha(solution)
    
    print(f"solution: {solution}")
    print(f"captcha: {poisoned}")

if __name__ == "__main__":
    main()
