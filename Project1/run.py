import subprocess
import time
import os

def run_command(command):
    start_time = time.time()
    result = subprocess.run(command, capture_output=True, text=True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, result.stdout.strip()

def main():
    # 设置命令参数
    command1 = [
        "python", "IEMP_Heur.py",
        "-n", r"D:\\Files\\2024Fall\\Artifical Intelligence\\Practice\\Lab3\\Testcase (localtest)\\Heuristic\\map3\\dataset2",
        "-i", r"D:\\Files\\2024Fall\\Artifical Intelligence\\Practice\\Lab3\\Testcase (localtest)\\Heuristic\\map3\\seed2",
        "-b", r"D:\\Files\\2024Fall\\Artifical Intelligence\\Practice\\Lab3\\Testcase (localtest)\\Heuristic\\map3\\seed_balanced",
        "-k", "15"
    ]
    
    command2 = [
        "python", "Evaluator.py",
        "-n", r"D:\\Files\\2024Fall\\Artifical Intelligence\\Practice\\Lab3\\Testcase (localtest)\\Heuristic\\map3\\dataset2",
        "-i", r"D:\\Files\\2024Fall\\Artifical Intelligence\\Practice\\Lab3\\Testcase (localtest)\\Heuristic\\map3\\seed2",
        "-b", r"D:\\Files\\2024Fall\\Artifical Intelligence\\Practice\\Lab3\\Testcase (localtest)\\Heuristic\\map3\\seed_balanced",
        "-k", "5",
        "-o", r"D:\\Files\\2024Fall\\Artifical Intelligence\\Practice\\Lab3\\Testcase (localtest)\\Heuristic\\map3\\ans"
    ]

    num_runs = 10  # 设置运行次数
    total_time1 = 0
    total_time2 = 0
    results = []

    for _ in range(num_runs):
        time1, _ = run_command(command1)
        time2, result = run_command(command2)
        
        total_time1 += time1
        total_time2 += time2
        results.append(result)

    avg_time1 = total_time1 / num_runs
    avg_result = sum(map(float, results)) / num_runs  # 假设结果可以转换为浮点数

    print(f"Average Time for IEMP_Heur for dataset2: {avg_time1:.2f} seconds")
    print(f"Average Result: {avg_result:.2f}")

if __name__ == "__main__":
    main()
