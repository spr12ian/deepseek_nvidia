from cls_deepseek_nvidia import DeepseekNvidia
from queries import queries


if __name__ == "__main__":
    deepseek_nvidia = DeepseekNvidia()
    for query in queries:
        q = query.strip()
        print(f"Query: {q}")
        print("Response:")
        response = deepseek_nvidia.get_response(q)
        deepseek_nvidia.print_response(response)
        print("\n")
