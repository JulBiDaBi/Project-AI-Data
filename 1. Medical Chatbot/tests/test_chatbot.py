import os
import pytest
from utils.preprocessing import clean_text, chunk_and_save_text

def test_clean_text(tmp_path):
    input_file = tmp_path / "test_input.txt"
    output_file = tmp_path / "test_output.txt"

    content = "--- Page 1 ---\nGALE ENCLYCLOPEDIA OF MEDICINE 2\nSome medical text.\nCopyright © 2023. All rights reserved.\nISBN 123-456-789\n\n\nMore text."
    input_file.write_text(content, encoding='utf-8')

    clean_text(str(input_file), str(output_file))

    cleaned_content = output_file.read_text(encoding='utf-8')
    assert "--- Page 1 ---" not in cleaned_content
    assert "GALE ENCLYCLOPEDIA OF MEDICINE 2" not in cleaned_content
    assert "Copyright © 2023" not in cleaned_content
    assert "ISBN 123-456-789" not in cleaned_content
    assert "Some medical text." in cleaned_content
    assert "More text." in cleaned_content

def test_chunk_and_save_text(tmp_path):
    input_file = tmp_path / "test_cleaned.txt"
    output_file = tmp_path / "test_chunks.txt"

    content = "This is a long sentence that will be split into chunks if we set the size small enough. Let's add more content to be sure."
    input_file.write_text(content, encoding='utf-8')

    chunk_and_save_text(str(input_file), str(output_file), chunk_size=50, chunk_overlap=10)

    chunks_content = output_file.read_text(encoding='utf-8')
    assert "--- Chunk 1 ---" in chunks_content
    assert "--- Chunk 2 ---" in chunks_content
