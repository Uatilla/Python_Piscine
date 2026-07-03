import os


def ft_tqdm(lst: range) -> None:
    """
    Custom tqdm-like progress bar for an iterable (especially range).

    Displays a dynamic progress bar in the terminal with percentage,
    visual bar, and current/total count. Updates in place using carriage return.

    Args:
        lst (range): The iterable to iterate over (typically a range object).

    Yields:
        Elements from the input iterable one by one.

    Note:
        The progress bar adapts to current terminal width.
    """
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = 80
    total = len(lst)
    if total == 0:
        print("0it [00:00, ?it/s]")
        return
    timing_space = 30
    current_pos = 0
    for n in lst:
        current_pos += 1
        percentage = 100 * (current_pos / total)
        counter = f"{current_pos}/{total}"
        right_len = len(counter) + timing_space + 3
        bar_width = max(1, columns - right_len)
        filled = (current_pos * bar_width) // total
        bar = "█" * filled + " " * (bar_width - filled)
        print(f"\r{percentage:>3.0f}%|{bar}| {current_pos}/{total}", end="")
        yield n
