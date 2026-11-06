# 关键公式到代码模块的映射

[返回入口](README.md)

状态：全部为规划，尚无中间观测器代码。下表路径仅用代码格式展示，不是可点击的现存文件。F-* 是内部追踪号，**不是原论文公式编号**；不可直接把某个式号认定为估计核心。

| 内部 ID | 需从原文提取的内容 | 页码 / 式号 / 完整表达式 | 拟模块与函数（未实现） | 输入 → 输出契约 | 待实施验证 |
| --- | --- | --- | --- | --- | --- |
| F-01 | 状态动力学与输出方程 | 待提供 | simulation/intermediate_observer/model.py: rhs, output | 时间、真值状态、控制/未知输入 → 导数、量测；形状待定 | 手算单点、矩阵尺寸与单位 |
| F-02 | 控制、未知输入及噪声生成 | 待提供 | simulation/intermediate_observer/signals.py: inputs | 时间、配置、随机源 → 各输入信号 | 分段边界、幅值、种子复现 |
| F-03 | 中间变量定义及初值变换 | 待提供 | simulation/intermediate_observer/observer.py: initialize | 合法初始估计、增益 → 内部初值 | 代回定义、变换一致性 |
| F-04 | 中间变量/扩展状态的更新方程 | 待提供 | simulation/intermediate_observer/observer.py: rhs | 时间、内部估计、可测输出、已知输入 → 内部导数 | 手算导数；禁止读取未知真值 |
| F-05 | 状态及未知输入重构 | 待提供 | simulation/intermediate_observer/observer.py: reconstruct | 内部估计、可测量及增益 → 估计量 | 维度、符号、理想一致性 |
| F-06 | 增益设计与稳定性条件 | 待提供 | simulation/intermediate_observer/gains.py: design, validate | 模型与设计约束 → 增益、可行性诊断 | 约束残差、不可行情形 |
| F-07 | 误差及评价指标 | 待提供 | simulation/intermediate_observer/metrics.py: evaluate | 同时间轴的真值、估计与评价窗口 → 指标 | 符号、单位、已知误差样例 |

拟运行编排模块为 simulation/intermediate_observer/run.py（未实现）：加载配置、生成真值/量测、积分观测器、重构、评价、保存。当前不存在可用的观测器运行命令。

逐式补充时必须记录：

1. 原始式子、符号定义及维度，必要的转置、求导阶次与求和范围。
2. 从原文公式到实现式的每一步变换；推导假设引用模型表 A-*。
3. 原文公式间的依赖、初始化顺序与每步可用信息；未知输入真值仅供模型生成和离线评价。
4. 连续方程与数值积分的区别；采样/插值/离散化属于实现设定，注明来源。
5. 实际实现后补充代码提交号、函数及测试路径；未实现不得改成“已验证”。

现有 simulation/minimal.py 的 estimate 仅实现标量 WLS，既不对应 F-03～F-06，也不能作为这些模块的已完成标记。
