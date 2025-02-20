from cls_deepseek_nvidia import DeepseekNvidia
from queries import queries


if __name__ == "__main__":
    deepseek_nvidia = DeepseekNvidia()
    for query in queries:
        print(f"Query: {query}")
        print("Response:")
        response = deepseek_nvidia.get_response(query)
        deepseek_nvidia.print_response(response)
