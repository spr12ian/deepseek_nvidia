from pathlib import Path
from deepseek_nvidia.classes.deepseek_nvidia import DeepseekNvidia
import tomllib as toml
from deepseek_nvidia.classes.prompt import Prompt

def get_prompts(file_path:Path)->list[Prompt]:
    data = toml.loads(file_path.read_text(encoding="utf-8"))

    if "prompts" not in data:
        raise ValueError(f"'prompts' section missing in {file_path}")

    return [Prompt(**item) for item in data["prompts"]]

def strip_multiline_string(multiline_string:str) -> str:
    lines = multiline_string.splitlines()
    stripped_lines = [line.strip() for line in lines if line.strip()]
    return "\n".join(stripped_lines)


def main() -> None:
    deepseek_nvidia = DeepseekNvidia()
    private_prompts=get_prompts(Path('data/private_prompts.toml'))
    public_prompts=get_prompts(Path('data/public_prompts.toml'))
    prompts=private_prompts+public_prompts
    print(f"📄 Loaded {len(prompts)} prompts from private + public TOML files")

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
