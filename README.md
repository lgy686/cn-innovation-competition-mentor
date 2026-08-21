# 中国大学生创新创业竞赛项目辅导助手

`cn-innovation-competition-mentor` 是一个面向中国高校创新创业、科技创新、商业策划、挑战杯、互联网+、中国国际大学生创新大赛、iCAN、揭榜挂帅和行业专项赛的 Codex Skill。

它以 Codex **当前工作目录**作为一个竞赛项目的根目录，先理解赛事规则、赛道要求、评分标准和官方模板，再读取项目原始材料、成果佐证和参考案例，协助完成或优化：

- 商业计划书、创业计划书和项目申报书；
- 答辩 PPT、路演 PPT 及逐页内容优化；
- 获奖案例页面到当前项目的替换方案；
- 赛事方案、赛道、评分标准和材料缺口分析；
- 专利、合同、收入、技术性能等项目数据的交叉核验；
- 技术路线、商业闭环、系统架构等图示的项目化绘图提示词；
- Word 模板下的样式、图表、表格和编号质量检查。

## 适用边界

适用于有明确高校竞赛背景、需要按赛事规则组织材料的项目。它不是普通公司商业咨询、普通论文润色、无竞赛背景的通用 PPT 设计，也不应被用来凭空创造项目成果。

## 核心工作原则

信息冲突时，始终按以下顺序处理：

> 组委会正式要求 > 赛道专项要求 > 官方商业计划书/PPT 模板 > 项目真实材料与佐证 > 用户明确要求 > 优秀获奖案例 > 外部资料 > 一般经验

因此，该 Skill 会坚持：

- 先看比赛，再看项目；先看证据，再写结论；先看评分，再设计表达。
- 不新增项目材料无法支持的技术、专利、合同、客户、收入、奖项、实验数据或商业模式。
- 不把优秀案例的项目事实迁移到当前项目。案例只可借鉴页面结构、信息层级、文字密度、图文关系和视觉表达逻辑。
- 不把计划、预计、目标或推论写成“已实现”成果；无法核实的精确数值使用 `【待补充真实数据】`。
- 项目自身成果优先使用原始材料和佐证；外部资料只用于行业、市场、政策、技术现状、竞品、标准和公开趋势，并记录来源、日期、数据年份和原始链接。
- 发现计划书、PPT、合同或证书中的同一数据口径冲突时，列出冲突文件、数值和来源，等待核实或以直接佐证为准。

## 准备项目目录

将与一个项目有关的文件放入同一个工作目录。目录名称无需固定，Skill 会结合目录名、文件名和文件内容进行语义识别；推荐的整理方式如下：

```text
当前项目目录/
├── 赛事材料/
│   ├── 比赛通知、赛事方案、赛道方案、评分细则
│   ├── 商业计划书/申报书/PPT 官方模板
│   └── 答辩、页数、字数、匿名、命名和附件要求
├── 项目原始材料/
│   ├── 既有商业计划书、旧版 PPT、技术方案、论文
│   ├── 产品说明、技术路线、市场分析、商业模式
│   └── 实验材料和项目介绍
├── 项目佐证材料/
│   ├── 专利、软著、奖项、合同、合作协议
│   ├── 检测/查新/用户证明、财务凭证、报道
│   └── 产品照片、软件截图、应用现场图片
└── 优秀案例/
    └── 用户提供的获奖 PPT、PDF 或页面图片
```

没有某类文件也可以开始。Skill 会读取已存在的材料，并明确说明缺失的赛事文件、佐证或待核实数据；不需要反复上传已在当前目录中的文件。

## 如何调用

可以显式调用：

```text
使用 $cn-innovation-competition-mentor，扫描当前项目目录，分析本项目的赛事要求、评分项和材料缺口。
```

也可以直接提出带有竞赛语境的任务，Skill 会自动匹配。以下是常用提示词。

### 1. 分析赛事规则和赛道

```text
使用 $cn-innovation-competition-mentor，读取当前目录的赛事方案、赛道方案和评分细则，
输出赛事约束矩阵、评分项映射、硬性格式要求和本项目材料缺口。
```

### 2. 按优秀案例替换指定 PPT 页面

```text
使用 $cn-innovation-competition-mentor，根据当前项目材料、赛事评分标准和优秀案例第 8 页，
输出当前项目对应页面的完整替换方案。不要生成 PPT 文件。
```

默认输出页面定位、页面总体逻辑、逐元素替换表、配图替换方案和内容来源；覆盖标题、模块、数据、图表、图片、箭头、底部结论和页脚，而不是只替换局部文字。

### 3. 逐页优化已有答辩 PPT

```text
使用 $cn-innovation-competition-mentor，逐页分析当前初版答辩 PPT，
结合评分项和参考案例，给出每页的替换前—替换后优化方案。
```

每页会明确答辩任务、评分项、必须保留的信息、当前问题、可借鉴处和不可机械照搬处，并提出标题、文字密度、数据、图片、图表、逻辑关系和结论栏的调整建议。

### 4. 根据 PPT 撰写商业计划书

```text
使用 $cn-innovation-competition-mentor，根据当前 PPT、项目佐证和官方商业计划书模板，
撰写商业计划书第三章并生成新的 Word 工作版本。不要覆盖原文件。
```

写作会先解析官方模板和篇幅限制，按评分项安排章节内容；Word 文件优先复用模板样式。默认图注置于图下、表注置于表上，正式表格优先三线表，但官方模板另有规定时以模板为准。

### 5. 核验项目数据与成果

```text
使用 $cn-innovation-competition-mentor，核对计划书、PPT 和佐证材料中的专利、合同、客户、营收和技术性能，
建立项目证据矩阵并列出所有口径冲突。
```

项目主张会分为四类：A级为直接佐证，B级为材料中明确陈述但暂缺佐证，C级为合理推论，D级为外部公开资料。C 级内容不能写成项目已实现事实。

### 6. 生成图示提示词

```text
使用 $cn-innovation-competition-mentor，为当前项目的商业闭环和技术路线生成可用于 AI 绘图的详细提示词，
并说明应插入商业计划书的哪个位置。
```

提示词会描述主题、用途、比例、色彩、模块、模块内容、箭头关系、层级、图标、留白、文字要求、行业风格和应避免的错误。没有现成图时，Word 中会保留明确的待绘图占位和图注位置。

## 交付形式

请在请求中明确本次交付形式：

- “只告诉我怎么替换”或“不要生成文件”：只输出内容方案，不生成 PPT 或 Word。
- “生成 Word/PPT 文件”：在源文件基础上复制生成新的工作版本，不覆盖客户原件。
- “需要外部数据”：使用权威来源，并附来源单位、标题、发布日期/数据年份和原始链接。

涉及市场规模、CAGR、客户数、价格、收入、成本、利润、技术性能、专利/合同/奖项数量时，必须给出项目内佐证或可靠外部来源；无可靠来源时保留待补充标记。

## Word 与图表要求

生成正式 Word 时，不应只靠逐段手动调字体；应复用官方模板样式，或使用项目专用的一级标题、二级标题、正文、图注、表注、表头、表正文和参考文献样式。定量数据优先采用可编辑的 Word 原生图表：趋势用折线图，多类别比较用柱状图，构成用饼图/环形图，收入成本利润用柱线组合图。若当前环境无法可靠创建可编辑图表，会保留数据表并说明推荐图表类型，而不会用静态截图冒充可编辑图表。

## 辅助脚本

脚本只负责确定性索引和结构检查，不替代赛事理解、证据判断或内容写作。请使用可用的 Python 运行时执行：

```powershell
# 生成项目文件清单及初步语义分类
python scripts/inventory_project.py <项目根目录>

# 提取 DOCX、PPTX、XLSX、PDF、Markdown 与文本文件的轻量元数据
python scripts/extract_project_metadata.py <项目根目录>

# 检查 DOCX/PPTX 的可确定结构问题
python scripts/validate_document.py <文件或目录>
```

其中 `validate_document.py` 只报告可机械判断的问题，例如重复图表编号、无段落样式或空白幻灯片；赛事符合性、内容真实性、证据充分性和视觉表达仍需结合材料人工复核。

## 安装与更新

将此仓库克隆到 Codex 的技能目录后，重启或刷新 Skills 列表即可使用。例如在 Windows PowerShell 中：

```powershell
git clone https://github.com/lgy686/cn-innovation-competition-mentor.git "$env:USERPROFILE\.codex\skills\cn-innovation-competition-mentor"
```

若该目录已有此 Skill，请进入目录后执行：

```powershell
git pull
```

## 维护指南：修改内容与文件对应关系

不同文件承担不同职责。`SKILL.md` 和 `references/` 决定 Codex 实际如何执行任务；`README.md` 主要面向 GitHub 用户说明使用方法；`agents/openai.yaml` 负责界面信息和调用策略；`scripts/` 只处理确定性自动化。

### 入口、触发和界面

| 想修改的内容 | 应修改的文件 | 说明 |
|---|---|---|
| Skill 名称 | `SKILL.md` 顶部的 `name`，以及技能目录名 | 名称必须使用小写字母、数字和连字符；改名还需同步所有调用示例 |
| 自动触发关键词、适用范围和排除边界 | `SKILL.md` 顶部的 `description` | 这是 Skill 选择阶段最重要的触发描述，应保持简短且有区分度 |
| 全局原则、入口流程、任务路由或交付边界 | `SKILL.md` 正文 | 只放所有任务都需要了解的规则，不要把所有细节重新塞回入口文件 |
| Codex 中显示的中文名称 | `agents/openai.yaml` 的 `interface.display_name` | 只影响界面显示，不改变 Skill 的执行逻辑 |
| Skill 列表中的简短说明 | `agents/openai.yaml` 的 `interface.short_description` | 应与 `SKILL.md` 的实际能力一致 |
| 点击 Skill 后出现的默认提示词 | `agents/openai.yaml` 的 `interface.default_prompt` | 提示词必须显式包含 `$cn-innovation-competition-mentor` |
| 是否允许自动调用 | `agents/openai.yaml` 的 `policy.allow_implicit_invocation` | `true` 允许自动匹配；`false` 时通常需要用户显式调用 |
| GitHub 首页的介绍、安装和使用示例 | `README.md` | 单独修改 README 不会改变 Skill 的实际行为 |

### 详细业务规则

| 想修改的内容 | 应修改的文件 |
|---|---|
| 信息优先级、事实状态词、案例使用边界 | `references/source-priority.md` |
| 首次扫描、文件分类和项目接收流程 | `references/project-intake.md` |
| 赛事方案、评分标准、赛道和硬性约束分析 | `references/competition-rules-analysis.md` |
| 证据等级、成果核验和口径冲突处理 | `references/evidence-matrix.md` |
| 获奖案例页面替换的步骤、表格和文字长度控制 | `references/ppt-case-replacement.md` |
| 初版 PPT 逐页分析和案例化优化方法 | `references/ppt-polishing.md` |
| 商业计划书章节组织、篇幅和写作风格 | `references/business-plan-writing.md` |
| Word 样式、标题、图注、表注和表格格式 | `references/word-formatting.md` |
| 商业数据来源、缺失数据和可编辑图表要求 | `references/charts-and-data.md` |
| 技术路线、商业闭环等 AI 绘图提示词要求 | `references/image-prompt-generation.md` |
| 联网检索的来源优先级和引用记录 | `references/web-research.md` |
| 最终交付前的赛事、证据、PPT 和 Word 检查项 | `references/quality-checklist.md` |

### 自动化脚本

| 想修改的内容 | 应修改的文件 |
|---|---|
| 文件清单、忽略目录、关键词初步分类 | `scripts/inventory_project.py` |
| Office/PDF/Markdown 元数据提取 | `scripts/extract_project_metadata.py` |
| DOCX/PPTX 结构与编号检查 | `scripts/validate_document.py` |

脚本不应代替赛事规则理解、事实可信度判断、页面视觉分析或商业写作。只有可重复、可机械判断的任务才适合放入 `scripts/`。

### 新增一种工作模式

如果以后新增一种相对独立的能力，例如“答辩稿撰写”或“申报书逐项填写”，建议按以下方式维护：

1. 在 `references/` 新建对应的 Markdown 文件，将详细流程写入其中。
2. 在 `SKILL.md` 的“工作流路由”中说明什么情况下读取该文件。
3. 如果新能力改变了触发范围，再简洁更新 `SKILL.md` 顶部的 `description`。
4. 在 README 中补充面向用户的说明和调用示例，但不要用 README 代替运行规则。

### 修改后的检查与发布

修改完成后，先运行 Skill 结构验证：

```powershell
$python = "C:\Users\LGY\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$env:PYTHONUTF8 = "1"

& $python `
  "C:\Users\LGY\.codex\skills\.system\skill-creator\scripts\quick_validate.py" `
  "C:\Users\LGY\.codex\skills\cn-innovation-competition-mentor"
```

如果修改了 Python 脚本，还应进行编译检查并实际运行对应脚本。验证通过后提交到 GitHub：

```powershell
cd C:\Users\LGY\.codex\skills\cn-innovation-competition-mentor
git add .
git commit -m "Update skill requirements"
git push origin main
```

修改规则时尽量只改负责该规则的文件，避免在 `SKILL.md`、reference 和 README 中重复维护同一套详细指令。若某项规则需要每次调用都生效，应放在 `SKILL.md`；若只在特定任务中使用，应放在相应 reference。

## 项目结构

```text
cn-innovation-competition-mentor/
├── SKILL.md                 # 触发边界、入口流程、模式路由和硬性原则
├── README.md                # 面向使用者的说明
├── agents/openai.yaml       # UI 显示名称、描述和默认提示
├── references/              # 按任务类型渐进加载的详细规则
├── scripts/                 # 文件索引、元数据和结构检查辅助脚本
└── assets/                  # 交付物需要使用的资源（当前为空）
```

详细运行规则见 [SKILL.md](SKILL.md)；按任务类型拆分的规则位于 [references](references) 目录。
