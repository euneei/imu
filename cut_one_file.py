import os

def split_file(input_file, chunk_size):
    base_name, _ = os.path.splitext(os.path.basename(input_file))

    with open(input_file, 'r') as infile:
        file_content = infile.readlines()

    num_chunks = (len(file_content) + chunk_size - 1) // chunk_size

    for i in range(num_chunks):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, len(file_content))

        # 새로운 파일명 생성 (예: 'acc_01.txt')
        output_file = f"{base_name}_{str(i+1).zfill(2)}.txt"

        with open(output_file, 'w') as outfile:
            outfile.writelines(file_content[start:end])
            print(f"Chunk {i+1} has been written to {output_file}")


input_file = '.../acc.txt'
chunk_size = 301

split_file(input_file, chunk_size)