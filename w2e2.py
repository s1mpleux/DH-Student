import argparse
import csv
import random
import numpy as np
from datetime import datetime

# ===================== BACKEND =====================
# 负责：数据存储、文件写入（底层IO）
class DataBackend:
    def __init__(self, filename):
        self.filename = filename

    def write_csv(self, rows, headers):
        """写入CSV文件"""
        with open(self.filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)

# ===================== MODEL =====================
# 负责：数据生成逻辑、分布、错误模拟
class DataModel:
    def __init__(self, sample_size=100):
        self.sample_size = sample_size
        self.headers = ["user_id", "age", "score", "test_date", "category"]

    def generate_age(self):
        """年龄：正态分布 + 少量错误值"""
        age = int(np.random.normal(25, 5, 1)[0])
        if random.random() < 0.08:  # 8%错误
            return random.choice([-5, 150, " ", None])
        return max(18, min(60, age))

    def generate_score(self):
        """分数：0-100均匀分布 + 缺失值"""
        score = round(random.uniform(0, 100), 1)
        if random.random() < 0.12:  # 12%缺失
            return None
        return score

    def generate_date(self):
        """日期：正确格式 + 格式错误"""
        base = datetime(2025, 1, 1)
        delta = random.randint(0, 180)
        date = base + datetime.timedelta(days=delta)
        if random.random() < 0.05:
            return date.strftime("%d-%m-%Y")  # 错误格式
        return date.strftime("%Y-%m-%d")     # 正确格式

    def generate_category(self):
        """分类：固定选项 + 脏数据"""
        cats = ["A", "B", "C"]
        if random.random() < 0.06:
            return random.choice(["X", "unknown", 999, ""])
        return random.choice(cats)

    def generate_row(self, user_id):
        return [
            user_id,
            self.generate_age(),
            self.generate_score(),
            self.generate_date(),
            self.generate_category()
        ]

# ===================== PROCESS =====================
# 负责：流程控制、调用Model+Backend
class DataProcess:
    def __init__(self, model, backend):
        self.model = model
        self.backend = backend

    def run(self):
        """执行完整生成流程"""
        print(f"正在生成 {self.model.sample_size} 条数据...")
        rows = [self.model.generate_row(i+1) for i in range(self.model.sample_size)]
        self.backend.write_csv(rows, self.model.headers)
        print(f"完成！文件已保存到：{self.backend.filename}")

# ===================== CLI 入口 =====================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="模拟带错误的实验数据生成器")
    parser.add_argument("--size", type=int, default=100, help="生成样本数量")
    parser.add_argument("--output", default="simulated_data.csv", help="输出文件名")
    args = parser.parse_args()

    # 组装架构
    backend = DataBackend(args.output)
    model = DataModel(sample_size=args.size)
    process = DataProcess(model, backend)

    # 运行
    process.run()
