# Handles multiple programming languages
SUPPORTED_LANGUAGES = {
    "Python": "python",
    "JavaScript": "javascript",
    "C++": "cpp",
    "Java": "java",
    "Go": "go",
    "Rust": "rust"
}

def get_language_code(language_name):
    return SUPPORTED_LANGUAGES.get(language_name, "python")
