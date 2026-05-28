#!/bin/bash
# 库存管理系统 v3.0 启动脚本
cd "$(dirname "$0")"

echo "=========================================="
echo "  库存管理系统 v3.0 - Web可视化版"
echo "=========================================="

# 生成模板（首次运行）
if [ ! -d "templates" ]; then
    echo ""
    echo "[1/3] 生成模板文件..."
    python3 create_templates.py
fi

# 导入数据（首次运行且数据库不存在）
if [ ! -f "stock.db" ]; then
    echo ""
    echo "[2/3] 导入 Excel 数据..."
    python3 import_excel.py
fi

echo ""
echo "[3/3] 启动 Web 服务器..."
echo ""
echo "  访问地址: http://127.0.0.1:5000"
echo "  默认账号: admin / admin123"
echo "  按 Ctrl+C 停止服务器"
echo ""
echo "=========================================="

python3 app.py