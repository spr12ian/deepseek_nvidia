from pathlib import Path
from deepseek_nvidia.classes.deepseek_nvidia import DeepseekNvidia
import yaml
from deepseek_nvidia.classes.prompt import Prompt

def get_prompts(file_path:Path)->list[Prompt]:
    with open(file_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return [Prompt(**item) for item in data["prompts"]]

def strip_multiline_string(multiline_string) -> str:
    lines = multiline_string.split("\n")
    stripped_lines = [line.strip() for line in lines]
    return "\n".join(stripped_lines)


def main() -> None:
    deepseek_nvidia = DeepseekNvidia()
    private_prompts=get_prompts(Path('data/private_prompts.yaml'))
    public_prompts=get_prompts(Path('data/public_prompts.yaml'))
    prompts=private_prompts+public_prompts
    for prompt in prompts:
        try:
            stripped_query = strip_multiline_string(prompt.prompt)
            print(f"Title: {prompt.name}")
            print(f"Query: {stripped_query}")

            print("Response:")
            deepseek_nvidia.print_response_to(stripped_query)

            print("\n" + "-" * 50 + "\n")  # Separator for readability
        except Exception as e:
            print(f"Error processing query: {e}")


if __name__ == "__main__":
    main()
