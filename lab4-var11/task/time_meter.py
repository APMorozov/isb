import time
from task.CrackHash import CrackHash


def time_meter(bins: str, last_four: str, target_hash: str) -> list[list[int | float]] | None:
    cores_count = CrackHash.get_count_cores()
    result = []
    crack_result = None

    for current_cores_count in range(1, int(cores_count * 1.5) + 1):
        start_time = time.time()
        for bin in bins:
            crack_result = CrackHash.find_collision(bin, last_four, target_hash, current_cores_count)
            if crack_result is not None:
                break

        result_time = time.time() - start_time
        if crack_result is None:
            return None
        pair = [current_cores_count, result_time]
        result.append(pair)

    return result

