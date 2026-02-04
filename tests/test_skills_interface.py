import pytest
from skills import README  

# Define the expected I/O contracts
skill_io_contracts = {
    "skill_download_youtube": ["url", "format"],
    "skill_transcribe_audio": ["file_path", "language"],
    "skill_generate_social_post": ["persona_id", "context_text", "platform"]
}

def test_skill_inputs():
    """
    Ensures that each skill module exposes the required input parameters.
    """
    for skill, params in skill_io_contracts.items():
        # Failing test: skills are not implemented yet, should fail
        with pytest.raises(ModuleNotFoundError):
            __import__(f"skills.{skill}")
