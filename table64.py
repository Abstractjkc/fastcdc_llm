import hashlib
from transformers import AutoTokenizer

def generate_gear_table(vocab_size):
    """
    Generate a gear table of predictable "random" 64-bit integers based on the vocabulary size.
    This mimics the behavior of the Rust implementation using MD5 hashes.

    Args:
        vocab_size (int): The size of the tokenizer vocabulary.

    Returns:
        list: A list of 64-bit integers.
    """
    gear_table = []
    seed = bytearray(64)

    for index in range(vocab_size):
        # Convert index to 4 bytes (32-bit integer) and repeat to fill 64 bytes
        index_bytes = index.to_bytes(4, byteorder='big', signed=False)
        for i in range(64):
            seed[i] = index_bytes[i % 4]

        hasher = hashlib.md5()
        hasher.update(seed)
        hash_bytes = hasher.digest()
        num = int.from_bytes(hash_bytes[:8], byteorder='big')
        gear_table.append(num)

    return gear_table

def save_gear_table(gear_table, file_path="gear_table.py"):
    """
    Save the gear table as a Python constant in a file.

    Args:
        gear_table (list): The gear table to save.
        file_path (str): The file path to save the table.
    """
    with open(file_path, "w") as f:
        f.write("GEAR_TABLE = [\n")
        for i, num in enumerate(gear_table):
            f.write(f"    0x{num:016x},\n")
        f.write("]\n")

def main():
    # Load the tokenizer
    tokenizer_name = "/mnt/jfzn/models/Qwen3-0.6B"  # Replace with your desired tokenizer
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name, trust_remote_code=True)

    # Get the vocabulary size
    vocab_size = len(tokenizer)
    print(f"Tokenizer vocabulary size: {vocab_size}")

    # Generate the gear table
    gear_table = generate_gear_table(vocab_size)

    # Save the gear table to a file
    save_gear_table(gear_table)
    print("Gear table generated and saved to 'gear_table.py'.")

if __name__ == "__main__":
    main()