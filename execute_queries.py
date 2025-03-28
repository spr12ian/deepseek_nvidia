from cls_deepseek_nvidia import DeepseekNvidia
from _queries import queries

def strip_multiline_string(multiline_string)->str:
    lines = multiline_string.split('\n')
    stripped_lines = [line.strip() for line in lines]
    return '\n'.join(stripped_lines)

def main() -> None:
    deepseek_nvidia = DeepseekNvidia()
    for q in queries:
        print(f"Type of q: {type(q)}")
        print(f"Content of q: {q}")
        try:
            # Handle different types of `q`
            if isinstance(q, dict):
                title = q.get("title", "Untitled Query")
                query = q.get("query", "")
            elif hasattr(q, "title") and hasattr(q, "query"):
                title = q.title
                query = q.query
            elif isinstance(q, str):
                title = "Untitled Query"
                query = q
            else:
                raise ValueError("Unsupported query format")

            stripped_query = strip_multiline_string(query)
            print(f"Title: {title}")
            print(f"Query: {stripped_query}")
            print("Response:")

            response = deepseek_nvidia.get_response(stripped_query)
            deepseek_nvidia.print_response(response)
            print("\n" + "-" * 50 + "\n")  # Separator for readability
        except Exception as e:
            print(f"Error processing query: {e}")

if __name__ == "__main__":
    main()