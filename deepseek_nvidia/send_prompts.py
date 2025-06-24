from deepseek_nvidia.classes.deepseek_nvidia import DeepseekNvidia
import yaml
from deepseek_nvidia.classes.prompt import Prompt

def get_prompts()->list[Prompt]:
    pass

def strip_multiline_string(multiline_string) -> str:
    lines = multiline_string.split("\n")
    stripped_lines = [line.strip() for line in lines]
    return "\n".join(stripped_lines)


def main() -> None:
    deepseek_nvidia = DeepseekNvidia()
    prompts=get_prompts()
    for prompt in prompts:
        print(f"Type of q: {type(prompt.name)}")
        print(f"Content of q: {prompt.prompt}")
        try:
            stripped_query = strip_multiline_string(prompt.prompt)
            print(f"Title: {prompt.name}")
            print(f"Query: {stripped_query}")
            print("Response:")


            response = deepseek_nvidia.get_response(stripped_query)
            deepseek_nvidia.print_response(response)
            print("\n" + "-" * 50 + "\n")  # Separator for readability
        except Exception as e:
            print(f"Error processing query: {e}")


if __name__ == "__main__":
    main()
