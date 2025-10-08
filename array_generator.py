"""Generate an array of numbers from 100 to 1000 incrementing by 50."""

from typing import List


def generate_array(start: int = 100, stop: int = 1000, step: int = 50) -> List[int]:
    """Return a list of integers from ``start`` to ``stop`` inclusive incrementing by ``step``.

    Parameters
    ----------
    start: int
        The value to begin the sequence from. Defaults to ``100``.
    stop: int
        The upper bound of the sequence (inclusive). Defaults to ``1000``.
    step: int
        The step size between elements in the sequence. Defaults to ``50``.

    Returns
    -------
    List[int]
        A list containing numbers from ``start`` to ``stop`` with the provided increment.
    """

    if step <= 0:
        raise ValueError("step must be a positive integer")
    if stop < start:
        raise ValueError("stop must be greater than or equal to start")
    # ``range`` is inclusive of the start value and exclusive of the stop value.
    # To include the ``stop`` value itself we extend the stop by ``step``.
    return list(range(start, stop + step, step))


if __name__ == "__main__":
    array = generate_array()
    print(array)
