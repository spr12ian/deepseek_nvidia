from cls_deepseek_nvidia import DeepseekNvidia
from queries import queries

def strip_multiline_string(multiline_string):
    lines = multiline_string.split('\n')
    stripped_lines = [line.strip() for line in lines]
    return '\n'.join(stripped_lines)

if __name__ == "__main__":
    deepseek_nvidia = DeepseekNvidia()
    for query in queries:
        stripped_query = strip_multiline_string(query)
        print(f"Query: {stripped_query}")
        print("Response:")
        response = deepseek_nvidia.get_response(stripped_query)
        deepseek_nvidia.print_response(response)
        print("\n")