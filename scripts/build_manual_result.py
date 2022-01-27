import sys
import os
import json

STORE_DIR_PATH = os.path.join('..', 'RESULTS')
FILE_NAME = "man-{0}-results.json"


def load_results_if_already_exists(file_path):
    results = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            results = json.load(file)
            
    return results


def build_result(params):
    def int_arg(i):
        return int(params[i])
    
    return {
        "duration": int_arg(2),
        "standing_up": int_arg(3),
        "first_walk": int_arg(4),
        "first_turn": int_arg(5),
        "second_walk": int_arg(6),
        "second_turn": int_arg(7),
        "sitting_down": int_arg(8),
        "automatic_end": params[9] == 'true'
    }
    
    
def store_results(file_path, results):
    with open(file_path, 'w') as file:
        json.dump(results, file)


if __name__ == "__main__":
    if len(sys.argv) != 10:
        sys.exit('invalid number of arguments')
             
    file_name = FILE_NAME.format(sys.argv[1])
    file_path = os.path.join(STORE_DIR_PATH, file_name)
    
    results = load_results_if_already_exists(file_path)
    result = build_result(sys.argv)
    results.append(result)
    
    store_results(file_path, results)
    