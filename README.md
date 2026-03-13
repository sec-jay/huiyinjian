# 回音笺 HuiYinJian

把你正在做的事，翻译成可见回报。

## 项目简介

回音笺是一个面向个人成长与职业积累的 AI 反馈系统。  
用户通过文字或语音描述自己最近做的事情，系统将其转译为结构化反馈，包括：

- 做了什么
- 产出了什么
- 提升了哪些能力
- 哪些内容可以写进简历
- 当前投入的回报感如何
- 下一步如何让回报更可见

它试图解决的问题是：  
很多事情并不是没有价值，而是价值没有被看见。  
回音笺希望把这些隐性的成长、成果和职业资产显化出来。

## MVP 目标

第一版 MVP 将完成以下能力：

- 接收用户输入的一段自然语言描述
- 调用模型进行结构化解析
- 输出任务、成果、能力、证据、简历表达和回报评分
- 通过后端接口返回结果

## 技术栈

- Python
- FastAPI
- Pydantic
- requirements.txt

## 当前规划功能

- [x] 项目命名
- [x] 仓库初始化
- [x] 产品与 Prompt 文档
- [ ] 后端基础接口
- [ ] `/analyze` 文本分析接口
- [ ] 模型调用封装
- [ ] 前端输入与结果展示页面

## 仓库结构

```text
.
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ docs/
│  ├─ product.md
│  ├─ mvp-plan.md
│  └─ prompt.md
├─ backend/
│  └─ app/
│     ├─ __init__.py
│     ├─ main.py
│     ├─ schemas.py
│     └─ services/
│        ├─ __init__.py
│        └─ placeholder.py
└─ frontend/
   └─ .gitkeep
