# 电力系统状态估计与中间观测器研究
主仓库：https://github.com/liyahui2345-hub/keyan

## 快速开始
环境：Python 3.11 或 3.12，仅使用标准库。
```sh
python -m venv .venv
python -m simulation.minimal --output results/minimal.json
python -m unittest discover -s tests -v
```
可选激活：Windows PowerShell 使用 .venv/Scripts/Activate.ps1；Linux 使用 source .venv/bin/activate。
示例是单状态线性加权最小二乘（WLS）基线，使用合成量测；不是完整电网模型，也不是中间观测器论文算法。输出包含估计值、真值、误差、配置和 Python 版本。

## 中间观测器论文复现入口

从 [复现入口与缺失输入清单](papers/intermediate_observer/README.md) 开始，按顺序填写 [论文索引](papers/INDEX.md)、模型假设、公式映射、参数、目标图表和实验记录。
当前仅新增资料与规划模板；目标论文尚未确认，中间观测器尚未实现，也没有论文仿真结果。现有 WLS 基线保持独立。

## 目录
- papers/：文献索引、公式推导和论文复现映射
- simulation/：仿真代码和最小运行入口
- experiments/：实验计划、记录模板和基线记录
- data/：数据来源、单位与获取说明
- results/：本地生成结果，不提交
- tests/：数值正确性验证
- .github/workflows/ci.yml：自动运行测试与示例

## 复现流程
1. 在 papers/ 记录论文 DOI、版本、目标图表及模型假设。
2. 固定参数、数据来源、软件版本和随机种子（若使用）。
3. 运行实验，记录命令、Git 提交、指标、失败情况和结论。
4. 对照论文结果填写差异与原因，禁止把示例结果当成论文结论。

## 仓库选择
keyan（公开）适合可分享的代码、合成数据和复现记录，作为唯一代码主线。
keyant（私有）适合未发表稿件或受限资料；如需要保留，仅保存私有材料及对应主仓库提交号，不复制代码主线。
若没有私有材料需求，建议在 keyant 添加指向本仓库的说明后归档；不建议直接删除。
本次仅初始化 keyan，不更改 keyant 设置。

## 发布边界
仅提交原创或具有再分发权限的内容。文献优先存 DOI/链接，不默认上传出版商 PDF。
真实电网数据需确认授权并脱敏。当前尚未选择开源许可证，发布复用版本前由作者确定。
