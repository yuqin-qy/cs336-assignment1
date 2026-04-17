from __future__ import annotations

from pathlib import Path
import multiprocessing

def train_bpe(
    input_path: str | Path,
    vocab_size: int,
    special_tokens: list[str],
) -> tuple[dict[int, bytes], list[tuple[bytes, bytes]]]:
    # Pre-tokenization
    pass