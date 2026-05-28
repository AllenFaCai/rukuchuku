# 库存管理系统 v3.0

> Web 可视化界面 + SQLite 数据库 + 条码扫描 + Excel 导入导出

## 快速开始

```bash
# 1. 安装依赖（仅需 openpyxl）
pip install openpyxl

# 2. 一键启动
python3 app.py
# 或使用启动脚本：bash start.sh
```

打开浏览器访问 **http://127.0.0.1:5000**
默认账号：`admin` / `admin123`

首次启动会自动：
- 创建数据库（`stock.db`）
- 从 Excel 文件导入数据

## 功能模块

### 数据仪表盘
- 实时统计：产品总数、库存总量、今日操作、低库存预警
- 最近操作记录
- 产品分类和品牌分布
- 低库存商品预警列表

### 产品管理
- 产品列表：搜索、分类筛选、品牌筛选、分页
- 新增产品：条码、货号、名称、品牌、尺码、分类
- 编辑产品：修改所有产品信息
- 删除产品：确认后删除

### 入库操作
- 条码扫描输入（支持扫码枪）
- 自动识别已有产品
- 未知条码自动弹出手动建档表单
- 实时显示入库结果

### 出库操作
- 条码扫描输入
- 实时库存预览（输入条码后自动显示当前库存）
- 库存不足自动拦截
- 出库结果反馈

### 库存管理
- 库存总览表格
- 搜索和分页
- 库存状态标记（正常/低库存/缺货）
- 手动库存调整（支持填写调整原因）

### 操作日志
- 完整操作记录（入库、出库、调整、检测）
- 多条件筛选：关键词、操作类型、日期范围
- 分页浏览

### 数据导入导出
- **导入**：支持 `.xlsx` / `.xls`，自动识别表头，支持多 Sheet
- **导出**：一键导出全部数据（产品、库存、日志三个 Sheet）
- 拖拽上传支持

## 技术架构

```
pythonProject1/
├── app.py                  # 主程序（Web 服务器 + 路由 + 业务逻辑）
├── import_excel.py         # Excel 数据导入工具
├── create_templates.py     # 模板生成脚本
├── start.sh                # 一键启动脚本
├── requirements.txt        # 依赖列表
├── stock.db                # SQLite 数据库（自动生成）
├── templates/              # HTML 模板
│   ├── base.html           # 基础布局（侧边栏 + 导航）
│   ├── login.html          # 登录页
│   ├── dashboard.html      # 仪表盘
│   ├── products.html       # 产品列表
│   ├── product_edit.html   # 编辑产品
│   ├── stock_in.html       # 入库操作
│   ├── stock_out.html      # 出库操作
│   ├── stock_manage.html   # 库存管理
│   ├── logs.html           # 操作日志
│   ├── import.html         # 数据导入
│   └── 404.html            # 404 页面
├── Stock_table.xlsx        # 原始库存数据（v2 遗留）
├── 库存表.xlsx              # 原始库存数据（v1 遗留）
└── ISBN-货号对照表.xlsx      # 原始对照数据
```

### 技术栈
- **后端**：Python 标准库（`http.server` + `sqlite3`）
- **前端**：Bootstrap 5 + Font Awesome 6（CDN）
- **数据库**：SQLite（WAL 模式，高并发读取）
- **模板**：自定义 Jinja2 风格模板引擎

### 数据库表结构
- `products`：产品信息（条码、货号、名称、品牌、尺码、分类）
- `stock`：库存数量（关联产品，一对一）
- `logs`：操作日志（时间、条码、变动量、操作类型、状态）
- `users`：用户账户

## 从旧版迁移

旧版 Excel 数据会在首次运行时自动导入。如需重新导入：

```bash
python3 import_excel.py
```

支持的 Excel 格式：
- `Stock_table.xlsx`（19-number / Stock / log 三个 Sheet）
- `库存表.xlsx`（ISBN-货号对照表 / 操作日志）
- `ISBN-货号对照表.xlsx`

## 版本历史

- **v3.0**（2026-05）：Web 可视化界面、SQLite 数据库、完整 CRUD
- **v2.0**（2025-12）：增加出库、扫码检测、补录模式
- **v1.0**（2025-12）：基础入库功能
