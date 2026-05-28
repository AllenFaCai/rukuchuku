"""生成所有 HTML 模板文件（兼容自定义模板引擎）"""
import os

TD = 'templates'
os.makedirs(TD, exist_ok=True)

def W(name, content):
    with open(os.path.join(TD, name), 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  {name}')

print("生成模板...")

# ============================================================
# base.html - 基础布局
# ============================================================
W('base.html', r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{% block title %}库存管理系统{% endblock %}</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
<style>
:root{--sidebar-w:260px;--primary:#6366f1;--sidebar-bg:#0f172a;--sidebar-hover:#1e293b;--body-bg:#f1f5f9}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--body-bg);font-family:'Segoe UI',system-ui,sans-serif}
.sidebar{position:fixed;left:0;top:0;bottom:0;width:var(--sidebar-w);background:var(--sidebar-bg);z-index:1000;overflow-y:auto}
.sidebar-brand{padding:1.5rem 1.25rem;display:flex;align-items:center;gap:.75rem;border-bottom:1px solid rgba(255,255,255,.06)}
.sidebar-brand .icon{width:40px;height:40px;border-radius:10px;background:linear-gradient(135deg,var(--primary),#a855f7);display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.1rem}
.sidebar-brand h5{color:#fff;margin:0;font-size:1rem;font-weight:600}
.sidebar-brand small{color:#94a3b8;font-size:.7rem}
.sidebar-nav{padding:.75rem 0}
.sidebar-nav .nav-section{padding:.5rem 1.25rem;color:#475569;font-size:.7rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;margin-top:.5rem}
.sidebar-nav a{display:flex;align-items:center;gap:.75rem;padding:.6rem 1.25rem;color:#94a3b8;text-decoration:none;font-size:.875rem;transition:all .2s;border-left:3px solid transparent}
.sidebar-nav a:hover{background:var(--sidebar-hover);color:#e2e8f0}
.sidebar-nav a.active{background:rgba(99,102,241,.15);color:var(--primary);border-left-color:var(--primary);font-weight:500}
.sidebar-nav a i{width:20px;text-align:center;font-size:.9rem}
.main-content{margin-left:var(--sidebar-w);min-height:100vh}
.top-bar{background:#fff;padding:.75rem 1.5rem;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #e2e8f0;position:sticky;top:0;z-index:100}
.content-area{padding:1.5rem}
.stat-card{background:#fff;border-radius:12px;padding:1.25rem;box-shadow:0 1px 3px rgba(0,0,0,.04);transition:transform .2s;border:1px solid #e2e8f0}
.stat-card:hover{transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,.08)}
.stat-card .stat-icon{width:48px;height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.25rem}
.stat-card .stat-value{font-size:1.75rem;font-weight:700;color:#1e293b}
.stat-card .stat-label{font-size:.8rem;color:#64748b}
.card-custom{background:#fff;border-radius:12px;border:1px solid #e2e8f0;box-shadow:0 1px 3px rgba(0,0,0,.04);overflow:hidden}
.card-custom .card-header-custom{padding:1rem 1.25rem;border-bottom:1px solid #f1f5f9;display:flex;align-items:center;justify-content:space-between}
.card-custom .card-header-custom h6{margin:0;font-weight:600;color:#1e293b}
.card-custom .card-body-custom{padding:1.25rem}
.table-custom{font-size:.85rem;margin:0}
.table-custom thead th{background:#f8fafc;border-bottom:2px solid #e2e8f0;color:#475569;font-weight:600;font-size:.75rem;text-transform:uppercase;letter-spacing:.03em;padding:.75rem}
.table-custom td{padding:.75rem;vertical-align:middle;border-color:#f1f5f9}
.btn-action{padding:.35rem .75rem;font-size:.8rem;border-radius:8px;display:inline-flex;align-items:center;gap:.3rem}
.scanner-input{font-size:1.25rem;padding:.75rem 1rem;border-radius:10px;border:2px solid #e2e8f0;transition:border-color .2s}
.scanner-input:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(99,102,241,.15)}
.flash-area{position:fixed;top:1rem;right:1rem;z-index:9999;min-width:300px}
.flash-area .alert{border-radius:10px;box-shadow:0 4px 12px rgba(0,0,0,.1)}
.pagination .page-link{border-radius:8px;margin:0 .15rem;font-size:.85rem}
.pagination .page-item.active .page-link{background:var(--primary);border-color:var(--primary)}
.empty-state{text-align:center;padding:3rem;color:#94a3b8}
.empty-state i{font-size:3rem;margin-bottom:1rem;display:block}
@media(max-width:768px){.sidebar{transform:translateX(-100%)}.sidebar.show{transform:translateX(0)}.main-content{margin-left:0}}
</style>
</head>
<body>
<div class="sidebar">
  <div class="sidebar-brand">
    <div class="icon"><i class="fas fa-boxes-stacked"></i></div>
    <div><h5>库存管理系统</h5><small>Inventory Management</small></div>
  </div>
  <nav class="sidebar-nav">
    <div class="nav-section">主要功能</div>
    <a href="/"><i class="fas fa-chart-pie"></i> 数据仪表盘</a>
    <a href="/products"><i class="fas fa-cube"></i> 产品管理</a>
    <a href="/stock/manage"><i class="fas fa-warehouse"></i> 库存管理</a>
    <div class="nav-section">库存操作</div>
    <a href="/stock/in"><i class="fas fa-arrow-down"></i> 入库操作</a>
    <a href="/stock/out"><i class="fas fa-arrow-up"></i> 出库操作</a>
    <a href="/stock/batch"><i class="fas fa-layer-group"></i> 批量出入库</a>
    <div class="nav-section">数据管理</div>
    <a href="/logs"><i class="fas fa-clock-rotate-left"></i> 操作日志</a>
    <a href="/import"><i class="fas fa-file-import"></i> 数据导入</a>
    <a href="/export"><i class="fas fa-file-export"></i> 数据导出</a>
  </nav>
</div>
<div class="main-content">
  <div class="top-bar">
    <span style="font-size:.85rem;color:#64748b">{% block breadcrumb %}首页{% endblock %}</span>
    <div class="d-flex align-items-center gap-3">
      {% if current_user %}
      <span class="text-muted" style="font-size:.85rem"><i class="fas fa-user-circle me-1"></i>{{ current_user.username }}</span>
      <a href="/logout" class="btn btn-sm btn-outline-secondary" style="font-size:.8rem"><i class="fas fa-sign-out-alt me-1"></i>退出</a>
      {% endif %}
    </div>
  </div>
  <div class="content-area">
    {% if flash %}
    <div class="flash-area">
      <div class="alert alert-{{ flash.0 }} alert-dismissible fade show" role="alert">
        {{ flash.1 }}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
      </div>
    </div>
    {% endif %}
    {% block content %}{% endblock %}
  </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script>
setTimeout(function(){
  document.querySelectorAll('.flash-area .alert').forEach(function(el){
    try{new bootstrap.Alert(el).close();}catch(e){el.remove();}
  });
},4000);
</script>
{% block scripts %}{% endblock %}
</body>
</html>''')

# ============================================================
# login.html
# ============================================================
W('login.html', r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>登录 - 库存管理系统</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
<style>
body{margin:0;min-height:100vh;display:flex;font-family:'Segoe UI',system-ui,sans-serif}
.login-left{flex:1;background:linear-gradient(135deg,#6366f1,#a855f7,#ec4899);display:flex;align-items:center;justify-content:center;color:#fff;padding:3rem}
.login-left .content{text-align:center;max-width:400px}
.login-left .content h1{font-size:2.5rem;font-weight:700;margin-bottom:1rem}
.login-left .content p{font-size:1.1rem;opacity:.9;line-height:1.6}
.login-left .features{margin-top:2rem;text-align:left}
.login-left .features div{display:flex;align-items:center;gap:.75rem;margin-bottom:.75rem;font-size:.95rem}
.login-right{flex:1;display:flex;align-items:center;justify-content:center;padding:2rem;background:#f8fafc}
.login-form{width:100%;max-width:400px}
.login-form h3{font-weight:700;color:#1e293b;margin-bottom:.5rem}
.login-form .form-control{padding:.75rem 1rem;border-radius:10px;font-size:.95rem}
.login-form .btn-login{padding:.75rem;border-radius:10px;font-size:1rem;font-weight:600;background:linear-gradient(135deg,#6366f1,#a855f7);border:none}
.login-form .btn-login:hover{opacity:.9}
@media(max-width:768px){.login-left{display:none}}
</style>
</head>
<body>
<div class="login-left">
  <div class="content">
    <h1><i class="fas fa-boxes-stacked me-2"></i>库存管理系统</h1>
    <p>高效、智能的库存管理解决方案<br>支持条码扫描、实时库存追踪</p>
    <div class="features">
      <div><i class="fas fa-check-circle"></i> 条码扫描快速入库/出库</div>
      <div><i class="fas fa-check-circle"></i> 实时库存数据可视化</div>
      <div><i class="fas fa-check-circle"></i> 完整操作日志追踪</div>
      <div><i class="fas fa-check-circle"></i> Excel数据导入导出</div>
    </div>
  </div>
</div>
<div class="login-right">
  <div class="login-form">
    <div class="text-center mb-4">
      <div style="width:60px;height:60px;border-radius:15px;background:linear-gradient(135deg,#6366f1,#a855f7);display:inline-flex;align-items:center;justify-content:center;margin-bottom:1rem">
        <i class="fas fa-boxes-stacked text-white" style="font-size:1.5rem"></i>
      </div>
      <h3>欢迎回来</h3>
      <p class="text-muted">请登录您的账户</p>
    </div>
    {% if flash %}
    <div class="alert alert-{{ flash.0 }} py-2" style="border-radius:10px;font-size:.9rem">{{ flash.1 }}</div>
    {% endif %}
    <form method="POST">
      <div class="mb-3">
        <label class="form-label text-muted" style="font-size:.85rem">用户名</label>
        <div class="input-group">
          <span class="input-group-text bg-white" style="border-radius:10px 0 0 10px"><i class="fas fa-user text-muted"></i></span>
          <input type="text" name="username" class="form-control" placeholder="请输入用户名" required autofocus style="border-radius:0 10px 10px 0">
        </div>
      </div>
      <div class="mb-4">
        <label class="form-label text-muted" style="font-size:.85rem">密码</label>
        <div class="input-group">
          <span class="input-group-text bg-white" style="border-radius:10px 0 0 10px"><i class="fas fa-lock text-muted"></i></span>
          <input type="password" name="password" class="form-control" placeholder="请输入密码" required style="border-radius:0 10px 10px 0">
        </div>
      </div>
      <button type="submit" class="btn btn-login btn-primary w-100"><i class="fas fa-sign-in-alt me-2"></i>登 录</button>
    </form>
    <p class="text-center text-muted mt-3" style="font-size:.8rem">默认账号: admin / admin123</p>
  </div>
</div>
</body>
</html>''')

# ============================================================
# dashboard.html
# ============================================================
W('dashboard.html', r'''{% extends "base.html" %}
{% block title %}仪表盘{% endblock %}
{% block breadcrumb %}数据仪表盘{% endblock %}
{% block content %}
<div class="row g-3 mb-4">
  <div class="col-md-3">
    <div class="stat-card">
      <div class="d-flex justify-content-between align-items-start">
        <div><div class="stat-label mb-1">产品总数</div><div class="stat-value">{{ stats.total_products }}</div></div>
        <div class="stat-icon" style="background:rgba(99,102,241,.1);color:#6366f1"><i class="fas fa-cube"></i></div>
      </div>
    </div>
  </div>
  <div class="col-md-3">
    <div class="stat-card">
      <div class="d-flex justify-content-between align-items-start">
        <div><div class="stat-label mb-1">库存总量</div><div class="stat-value">{{ stats.total_stock }}</div></div>
        <div class="stat-icon" style="background:rgba(16,185,129,.1);color:#10b981"><i class="fas fa-boxes-stacked"></i></div>
      </div>
    </div>
  </div>
  <div class="col-md-3">
    <div class="stat-card">
      <div class="d-flex justify-content-between align-items-start">
        <div><div class="stat-label mb-1">今日操作</div><div class="stat-value">{{ stats.today_scans }}</div></div>
        <div class="stat-icon" style="background:rgba(245,158,11,.1);color:#f59e0b"><i class="fas fa-chart-line"></i></div>
      </div>
    </div>
  </div>
  <div class="col-md-3">
    <div class="stat-card">
      <div class="d-flex justify-content-between align-items-start">
        <div><div class="stat-label mb-1">低库存预警</div><div class="stat-value text-danger">{{ stats.low_stock }}</div></div>
        <div class="stat-icon" style="background:rgba(239,68,68,.1);color:#ef4444"><i class="fas fa-exclamation-triangle"></i></div>
      </div>
    </div>
  </div>
</div>
<div class="row g-3 mb-4">
  <div class="col-md-4"><div class="stat-card text-center"><div class="stat-label">今日入库</div><div class="stat-value" style="color:#10b981">{{ stats.today_in }}</div></div></div>
  <div class="col-md-4"><div class="stat-card text-center"><div class="stat-label">今日出库</div><div class="stat-value" style="color:#f59e0b">{{ stats.today_out }}</div></div></div>
  <div class="col-md-4"><div class="stat-card text-center"><div class="stat-label">日志总条数</div><div class="stat-value">{{ stats.total_logs }}</div></div></div>
</div>
<div class="row g-3">
  <div class="col-lg-8">
    <div class="card-custom">
      <div class="card-header-custom">
        <h6><i class="fas fa-clock-rotate-left me-2 text-primary"></i>最近操作</h6>
        <a href="/logs" class="btn btn-sm btn-outline-primary" style="font-size:.8rem;border-radius:8px">查看全部</a>
      </div>
      <div class="card-body-custom p-0">
        {% if recent_logs %}
        <table class="table table-custom">
          <thead><tr><th>时间</th><th>条码</th><th>商品</th><th>类型</th><th>变动</th><th>状态</th></tr></thead>
          <tbody>
          {% for log in recent_logs %}
          <tr>
            <td class="text-muted" style="font-size:.8rem">{{ log.created_at }}</td>
            <td><code>{{ log.barcode }}</code></td>
            <td>{{ log.product_name }}</td>
            <td>
              {% if log.operation_type == '入库' %}<span class="badge bg-success-subtle text-success">入库</span>{% endif %}
              {% if log.operation_type == '手动入库' %}<span class="badge bg-success-subtle text-success">手动入库</span>{% endif %}
              {% if log.operation_type == '出库' %}<span class="badge bg-warning-subtle text-warning">出库</span>{% endif %}
              {% if log.operation_type == '库存调整' %}<span class="badge bg-info-subtle text-info">调整</span>{% endif %}
            </td>
            <td>
              {% if log.quantity_change > 0 %}<span class="text-success">+{{ log.quantity_change }}</span>{% endif %}
              {% if log.quantity_change == 0 %}<span class="text-muted">0</span>{% endif %}
              {% if log.quantity_change < 0 %}<span class="text-danger">{{ log.quantity_change }}</span>{% endif %}
            </td>
            <td><span class="badge bg-success-subtle text-success">{{ log.status }}</span></td>
          </tr>
          {% endfor %}
          </tbody>
        </table>
        {% else %}
        <div class="empty-state py-4"><i class="fas fa-inbox"></i><p>暂无操作记录</p></div>
        {% endif %}
      </div>
    </div>
  </div>
  <div class="col-lg-4">
    <div class="card-custom mb-3">
      <div class="card-header-custom"><h6><i class="fas fa-tags me-2 text-primary"></i>产品分类</h6></div>
      <div class="card-body-custom">
        {% if categories %}
        {% for cat in categories %}
        <div class="d-flex justify-content-between align-items-center mb-2">
          <span style="font-size:.85rem">{{ cat.category }}</span>
          <span class="badge bg-primary-subtle text-primary">{{ cat.count }}</span>
        </div>
        {% endfor %}
        {% else %}
        <p class="text-muted text-center" style="font-size:.85rem">暂无分类数据</p>
        {% endif %}
      </div>
    </div>
    <div class="card-custom">
      <div class="card-header-custom"><h6><i class="fas fa-exclamation-triangle me-2 text-warning"></i>低库存预警</h6></div>
      <div class="card-body-custom">
        {% if low_stock_items %}
        {% for item in low_stock_items %}
        <div class="d-flex justify-content-between align-items-center mb-2 p-2" style="background:#fef3c7;border-radius:8px">
          <div><div style="font-size:.85rem;font-weight:500">{{ item.name }}</div><small class="text-muted">{{ item.sku }}</small></div>
          <span class="badge bg-danger">{{ item.quantity }}</span>
        </div>
        {% endfor %}
        {% else %}
        <p class="text-muted text-center" style="font-size:.85rem">库存充足</p>
        {% endif %}
      </div>
    </div>
  </div>
</div>
{% endblock %}''')

# ============================================================
# products.html
# ============================================================
W('products.html', r'''{% extends "base.html" %}
{% block title %}产品管理{% endblock %}
{% block breadcrumb %}产品管理{% endblock %}
{% block content %}
<div class="card-custom">
  <div class="card-header-custom">
    <h6><i class="fas fa-cube me-2 text-primary"></i>产品列表 <span class="text-muted fw-normal">({{ total }})</span></h6>
    <button class="btn btn-primary btn-action" data-bs-toggle="modal" data-bs-target="#addModal"><i class="fas fa-plus"></i> 新增产品</button>
  </div>
  <div class="card-body-custom">
    <form class="row g-2 mb-3" method="GET">
      <div class="col-md-4"><input type="text" name="search" class="form-control" placeholder="搜索条码/货号/名称..." value="{{ search }}" style="border-radius:8px"></div>
      <div class="col-md-2">
        <select name="category" class="form-select" style="border-radius:8px">
          <option value="">全部分类</option>
          {% for c in categories %}<option>{{ c }}</option>{% endfor %}
        </select>
      </div>
      <div class="col-md-2">
        <select name="brand" class="form-select" style="border-radius:8px">
          <option value="">全部品牌</option>
          {% for b in brands %}<option>{{ b }}</option>{% endfor %}
        </select>
      </div>
      <div class="col-md-2"><button type="submit" class="btn btn-outline-primary w-100" style="border-radius:8px"><i class="fas fa-search me-1"></i>筛选</button></div>
      <div class="col-md-2"><a href="/products" class="btn btn-outline-secondary w-100" style="border-radius:8px"><i class="fas fa-rotate-left me-1"></i>重置</a></div>
    </form>
  </div>
  <div class="table-responsive">
    <table class="table table-custom">
      <thead><tr><th>条码</th><th>货号</th><th>商品名称</th><th>品牌</th><th>尺码</th><th>分类</th><th>库存</th><th>操作</th></tr></thead>
      <tbody>
      {% if items %}
      {% for item in items %}
      <tr>
        <td><code>{{ item.barcode }}</code></td>
        <td>{{ item.sku }}</td>
        <td><strong>{{ item.name }}</strong></td>
        <td>{{ item.brand }}</td>
        <td>{{ item.size }}</td>
        <td><span class="badge bg-light text-dark">{{ item.category }}</span></td>
        <td>
          {% if item.quantity == 0 %}<span class="badge bg-danger">缺货</span>{% endif %}
          {% if item.quantity > 0 %}{% if item.quantity < 5 %}<span class="badge bg-warning text-dark">{{ item.quantity }}</span>{% endif %}{% endif %}
          {% if item.quantity > 4 %}<span class="badge bg-success">{{ item.quantity }}</span>{% endif %}
        </td>
        <td>
          <a href="/products/{{ item.id }}/edit" class="btn btn-sm btn-outline-primary btn-action"><i class="fas fa-edit"></i></a>
          <form method="POST" action="/products/{{ item.id }}/delete" class="d-inline" onsubmit="return confirm('确定删除？')">
            <button type="submit" class="btn btn-sm btn-outline-danger btn-action"><i class="fas fa-trash"></i></button>
          </form>
        </td>
      </tr>
      {% endfor %}
      {% else %}
      <tr><td colspan="8" class="text-center text-muted py-4">暂无产品数据</td></tr>
      {% endif %}
      </tbody>
    </table>
  </div>
  {% if pages > 1 %}
  <div class="card-body-custom pt-0">
    <nav><ul class="pagination justify-content-center mb-0">
      {% for p in range(1, pages + 1) %}
      <li class="page-item"><a class="page-link" href="?page={{ p }}&search={{ search }}&category={{ category }}&brand={{ brand }}">{{ p }}</a></li>
      {% endfor %}
    </ul></nav>
  </div>
  {% endif %}
</div>
<div class="modal fade" id="addModal" tabindex="-1">
  <div class="modal-dialog"><div class="modal-content" style="border-radius:12px">
    <div class="modal-header"><h5 class="modal-title"><i class="fas fa-plus-circle me-2 text-primary"></i>新增产品</h5><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div>
    <form method="POST" action="/products/add">
      <div class="modal-body">
        <div class="mb-3"><label class="form-label">条码/19码 <span class="text-danger">*</span></label><input type="text" name="barcode" class="form-control" required></div>
        <div class="mb-3"><label class="form-label">货号 <span class="text-danger">*</span></label><input type="text" name="sku" class="form-control" required></div>
        <div class="mb-3"><label class="form-label">商品名称 <span class="text-danger">*</span></label><input type="text" name="name" class="form-control" required></div>
        <div class="row"><div class="col-6 mb-3"><label class="form-label">品牌</label><input type="text" name="brand" class="form-control"></div><div class="col-6 mb-3"><label class="form-label">尺码</label><input type="text" name="size" class="form-control"></div></div>
        <div class="mb-3"><label class="form-label">分类</label><input type="text" name="category" class="form-control" value="未分类"></div>
        <div class="mb-3"><label class="form-label">备注</label><input type="text" name="remark" class="form-control"></div>
      </div>
      <div class="modal-footer"><button type="button" class="btn btn-secondary" data-bs-dismiss="modal">取消</button><button type="submit" class="btn btn-primary"><i class="fas fa-check me-1"></i>添加</button></div>
    </form>
  </div></div>
</div>
{% endblock %}''')

# ============================================================
# product_edit.html
# ============================================================
W('product_edit.html', r'''{% extends "base.html" %}
{% block title %}编辑产品{% endblock %}
{% block breadcrumb %}编辑产品{% endblock %}
{% block content %}
<div class="row justify-content-center">
  <div class="col-lg-8">
    <div class="card-custom">
      <div class="card-header-custom">
        <h6><i class="fas fa-edit me-2 text-primary"></i>编辑产品信息</h6>
        <a href="/products" class="btn btn-sm btn-outline-secondary"><i class="fas fa-arrow-left me-1"></i>返回</a>
      </div>
      <div class="card-body-custom">
        <form method="POST">
          <div class="row g-3">
            <div class="col-md-6"><label class="form-label">条码 <span class="text-danger">*</span></label><input type="text" name="barcode" class="form-control" value="{{ product.barcode }}" required></div>
            <div class="col-md-6"><label class="form-label">货号 <span class="text-danger">*</span></label><input type="text" name="sku" class="form-control" value="{{ product.sku }}" required></div>
            <div class="col-md-12"><label class="form-label">名称 <span class="text-danger">*</span></label><input type="text" name="name" class="form-control" value="{{ product.name }}" required></div>
            <div class="col-md-4"><label class="form-label">品牌</label><input type="text" name="brand" class="form-control" value="{{ product.brand }}"></div>
            <div class="col-md-4"><label class="form-label">尺码</label><input type="text" name="size" class="form-control" value="{{ product.size }}"></div>
            <div class="col-md-4"><label class="form-label">分类</label><input type="text" name="category" class="form-control" value="{{ product.category }}"></div>
            <div class="col-md-12"><label class="form-label">备注</label><input type="text" name="remark" class="form-control" value="{{ product.remark }}"></div>
            <div class="col-md-12"><div class="p-3" style="background:#f8fafc;border-radius:10px"><span class="text-muted">当前库存：</span><span style="font-size:1.5rem;font-weight:700">{{ product.quantity }}</span></div></div>
          </div>
          <div class="mt-4 d-flex gap-2">
            <button type="submit" class="btn btn-primary" style="border-radius:10px"><i class="fas fa-save me-1"></i>保存</button>
            <a href="/products" class="btn btn-outline-secondary" style="border-radius:10px">取消</a>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
{% endblock %}''')

# ============================================================
# stock_in.html
# ============================================================
W('stock_in.html', r'''{% extends "base.html" %}
{% block title %}入库操作{% endblock %}
{% block breadcrumb %}入库操作{% endblock %}
{% block content %}
<div class="row g-3">
  <div class="col-lg-8">
    <div class="card-custom">
      <div class="card-header-custom"><h6><i class="fas fa-arrow-down me-2 text-success"></i>扫码入库</h6></div>
      <div class="card-body-custom">
        <form method="POST">
          <div class="mb-3"><label class="form-label fw-semibold">条码/19码</label><input type="text" name="barcode" id="barcodeInput" class="form-control scanner-input" placeholder="扫码或输入条码..." autofocus autocomplete="off" required></div>
          <div class="mb-3"><label class="form-label fw-semibold">入库数量</label><input type="number" name="quantity" class="form-control" value="1" min="1" style="border-radius:10px"></div>
          <button type="submit" class="btn btn-success btn-lg w-100" style="border-radius:10px"><i class="fas fa-box me-2"></i>确认入库</button>
        </form>
      </div>
    </div>
    <div class="card-custom mt-3" id="manualSection" style="display:none">
      <div class="card-header-custom"><h6><i class="fas fa-user-pen me-2 text-warning"></i>手动建档入库</h6></div>
      <div class="card-body-custom">
        <form method="POST" action="/stock/in/manual">
          <input type="hidden" name="barcode" id="manualBarcode">
          <div class="row g-2">
            <div class="col-md-6 mb-2"><label class="form-label">条码</label><input type="text" id="manualBarcodeDisplay" class="form-control" readonly></div>
            <div class="col-md-6 mb-2"><label class="form-label">货号 <span class="text-danger">*</span></label><input type="text" name="sku" class="form-control" required></div>
            <div class="col-md-6 mb-2"><label class="form-label">名称 <span class="text-danger">*</span></label><input type="text" name="name" class="form-control" required></div>
            <div class="col-md-3 mb-2"><label class="form-label">品牌</label><input type="text" name="brand" class="form-control"></div>
            <div class="col-md-3 mb-2"><label class="form-label">尺码</label><input type="text" name="size" class="form-control"></div>
            <div class="col-md-4 mb-2"><label class="form-label">入库数量</label><input type="number" name="quantity" class="form-control" value="1" min="1"></div>
          </div>
          <button type="submit" class="btn btn-warning mt-2" style="border-radius:10px"><i class="fas fa-save me-1"></i>建档并入库</button>
        </form>
      </div>
    </div>
  </div>
  <div class="col-lg-4">
    <div class="card-custom">
      <div class="card-header-custom"><h6><i class="fas fa-info-circle me-2 text-primary"></i>操作说明</h6></div>
      <div class="card-body-custom">
        <div class="mb-3 p-3" style="background:#f0fdf4;border-radius:10px;border-left:4px solid #10b981">
          <h6 style="color:#10b981;font-size:.9rem"><i class="fas fa-lightbulb me-1"></i>快速入库</h6>
          <p style="font-size:.85rem;margin:0;color:#475569">1. 扫码枪扫描条码<br>2. 系统自动识别<br>3. 确认数量后入库</p>
        </div>
        <div class="p-3" style="background:#fef3c7;border-radius:10px;border-left:4px solid #f59e0b">
          <h6 style="color:#f59e0b;font-size:.9rem"><i class="fas fa-exclamation-triangle me-1"></i>未知条码</h6>
          <p style="font-size:.85rem;margin:0;color:#475569">条码不在系统中时<br>请先手动建档</p>
        </div>
      </div>
    </div>
    {% if result %}
    {% if result.success %}
    <div class="card-custom mt-3">
      <div class="card-body-custom text-center">
        <div style="width:60px;height:60px;border-radius:50%;background:#dcfce7;display:inline-flex;align-items:center;justify-content:center;margin-bottom:.75rem"><i class="fas fa-check text-success" style="font-size:1.5rem"></i></div>
        <h6>{{ result.name }}</h6>
        <p class="text-muted" style="font-size:.85rem">货号: {{ result.sku }}</p>
        <div style="font-size:1.5rem;font-weight:700;color:#10b981">{{ result.before }} → {{ result.after }}</div>
        <p class="text-muted" style="font-size:.8rem">入库 +{{ result.qty }} 件</p>
      </div>
    </div>
    {% endif %}
    {% endif %}
  </div>
</div>
{% endblock %}
{% block scripts %}
<script>
{% if result %}{% if result.unknown %}
document.getElementById('manualSection').style.display='block';
document.getElementById('manualBarcode').value='{{ result.barcode }}';
document.getElementById('manualBarcodeDisplay').value='{{ result.barcode }}';
{% endif %}{% endif %}
document.getElementById('barcodeInput').focus();
</script>
{% endblock %}''')

# ============================================================
# stock_out.html
# ============================================================
W('stock_out.html', r'''{% extends "base.html" %}
{% block title %}出库操作{% endblock %}
{% block breadcrumb %}出库操作{% endblock %}
{% block content %}
<div class="row g-3">
  <div class="col-lg-8">
    <div class="card-custom">
      <div class="card-header-custom"><h6><i class="fas fa-arrow-up me-2 text-warning"></i>扫码出库</h6></div>
      <div class="card-body-custom">
        <form method="POST">
          <div class="mb-3"><label class="form-label fw-semibold">条码/19码</label><input type="text" name="barcode" id="barcodeInput" class="form-control scanner-input" placeholder="扫码或输入条码..." autofocus autocomplete="off" required></div>
          <div class="mb-3"><label class="form-label fw-semibold">出库数量</label><input type="number" name="quantity" class="form-control" value="1" min="1" style="border-radius:10px"></div>
          <button type="submit" class="btn btn-warning btn-lg w-100" style="border-radius:10px"><i class="fas fa-box me-2"></i>确认出库</button>
        </form>
      </div>
    </div>
    <div class="card-custom mt-3" id="previewCard" style="display:none">
      <div class="card-body-custom">
        <div class="d-flex align-items-center gap-3">
          <div style="width:50px;height:50px;border-radius:10px;background:#dbeafe;display:flex;align-items:center;justify-content:center"><i class="fas fa-cube text-primary"></i></div>
          <div><h6 id="previewName" class="mb-0"></h6><small class="text-muted" id="previewInfo"></small></div>
          <div class="ms-auto text-end"><div style="font-size:1.25rem;font-weight:700" id="previewQty"></div><small class="text-muted">当前库存</small></div>
        </div>
      </div>
    </div>
  </div>
  <div class="col-lg-4">
    <div class="card-custom">
      <div class="card-header-custom"><h6><i class="fas fa-info-circle me-2 text-primary"></i>操作说明</h6></div>
      <div class="card-body-custom">
        <div class="mb-3 p-3" style="background:#fef3c7;border-radius:10px;border-left:4px solid #f59e0b">
          <h6 style="color:#f59e0b;font-size:.9rem"><i class="fas fa-lightbulb me-1"></i>出库流程</h6>
          <p style="font-size:.85rem;margin:0;color:#475569">1. 扫描条码<br>2. 确认数量<br>3. 点击出库</p>
        </div>
        <div class="p-3" style="background:#fee2e2;border-radius:10px;border-left:4px solid #ef4444">
          <h6 style="color:#ef4444;font-size:.9rem"><i class="fas fa-exclamation-circle me-1"></i>注意</h6>
          <p style="font-size:.85rem;margin:0;color:#475569">出库数量不能超过当前库存</p>
        </div>
      </div>
    </div>
    {% if result %}
    {% if result.success %}
    <div class="card-custom mt-3">
      <div class="card-body-custom text-center">
        <div style="width:60px;height:60px;border-radius:50%;background:#fef3c7;display:inline-flex;align-items:center;justify-content:center;margin-bottom:.75rem"><i class="fas fa-check text-warning" style="font-size:1.5rem"></i></div>
        <h6>{{ result.name }}</h6>
        <p class="text-muted" style="font-size:.85rem">货号: {{ result.sku }}</p>
        <div style="font-size:1.5rem;font-weight:700;color:#f59e0b">{{ result.before }} → {{ result.after }}</div>
        <p class="text-muted" style="font-size:.8rem">出库 -{{ result.qty }} 件</p>
      </div>
    </div>
    {% endif %}
    {% endif %}
  </div>
</div>
{% endblock %}
{% block scripts %}
<script>
var bi=document.getElementById('barcodeInput');
var pc=document.getElementById('previewCard');
var pn=document.getElementById('previewName');
var pi=document.getElementById('previewInfo');
var pq=document.getElementById('previewQty');
var timer;
bi.addEventListener('input',function(){
  clearTimeout(timer);var v=this.value.trim();
  if(v.length<3){pc.style.display='none';return;}
  timer=setTimeout(function(){
    fetch('/api/barcode/'+v).then(function(r){return r.json();}).then(function(d){
      if(d.found){pn.textContent=d.name;pi.textContent=d.sku+' | '+d.brand+' | '+d.size;pq.textContent=d.quantity;pq.style.color=d.quantity<5?'#ef4444':'#10b981';pc.style.display='block';}
      else{pc.style.display='none';}
    });
  },300);
});
</script>
{% endblock %}''')

# ============================================================
# batch_stock.html - 批量出入库
# ============================================================
W('batch_stock.html', r'''{% extends "base.html" %}
{% block title %}批量出入库{% endblock %}
{% block breadcrumb %}批量出入库{% endblock %}
{% block content %}
<div class="row g-3">
  <div class="col-lg-7">
    <div class="card-custom">
      <div class="card-header-custom"><h6><i class="fas fa-layer-group me-2 text-primary"></i>批量出入库</h6></div>
      <div class="card-body-custom">
        <form method="POST" id="batchForm">
          <div class="mb-3">
            <label class="form-label fw-semibold">操作类型</label>
            <div class="d-flex gap-2">
              <label class="btn btn-outline-success flex-fill" style="border-radius:10px">
                <input type="radio" name="mode" value="in" checked class="d-none"> <i class="fas fa-arrow-down me-1"></i>批量入库
              </label>
              <label class="btn btn-outline-warning flex-fill" style="border-radius:10px">
                <input type="radio" name="mode" value="out" class="d-none"> <i class="fas fa-arrow-up me-1"></i>批量出库
              </label>
            </div>
          </div>
          <div class="mb-3">
            <label class="form-label fw-semibold">默认数量</label>
            <input type="number" name="default_qty" class="form-control" value="1" min="1" style="border-radius:10px">
            <small class="text-muted">每行只写条码时使用此数量。也可在条码后空格加数量，如：<code>6901028001489 5</code></small>
          </div>
          <div class="mb-3">
            <label class="form-label fw-semibold">条码列表 <span class="text-danger">*</span></label>
            <textarea name="barcodes" id="barcodeArea" class="form-control" rows="12" style="border-radius:10px;font-family:monospace;font-size:.9rem" placeholder="每行一个条码，支持格式：&#10;6901028001489&#10;6901028001489 3&#10;6901028001490 2&#10;&#10;可直接用扫码枪连续扫描，条码会自动换行" required></textarea>
            <div class="d-flex justify-content-between mt-1">
              <small class="text-muted" id="lineCount">0 个条码</small>
              <button type="button" class="btn btn-sm btn-outline-secondary" onclick="document.getElementById('barcodeArea').value='';updateCount();" style="font-size:.75rem">清空</button>
            </div>
          </div>
          <button type="submit" class="btn btn-primary btn-lg w-100" style="border-radius:10px">
            <i class="fas fa-play me-2"></i>开始执行
          </button>
        </form>
      </div>
    </div>
  </div>

  <div class="col-lg-5">
    <div class="card-custom mb-3">
      <div class="card-header-custom"><h6><i class="fas fa-info-circle me-2 text-primary"></i>使用说明</h6></div>
      <div class="card-body-custom">
        <div class="mb-3 p-3" style="background:#f0fdf4;border-radius:10px;border-left:4px solid #10b981">
          <h6 style="color:#10b981;font-size:.9rem"><i class="fas fa-lightbulb me-1"></i>快速操作</h6>
          <p style="font-size:.85rem;margin:0;color:#475569">
            1. 选择入库或出库<br>
            2. 设置默认数量<br>
            3. 用扫码枪连续扫描（自动换行）<br>
            4. 或粘贴多个条码<br>
            5. 点击"开始执行"
          </p>
        </div>
        <div class="p-3" style="background:#eff6ff;border-radius:10px;border-left:4px solid #3b82f6">
          <h6 style="color:#3b82f6;font-size:.9rem"><i class="fas fa-keyboard me-1"></i>自定义数量</h6>
          <p style="font-size:.85rem;margin:0;color:#475569">
            每行格式：<code>条码 数量</code><br>
            例如：<code>6901028001489 5</code><br>
            表示该条码出入库 5 件
          </p>
        </div>
      </div>
    </div>

    {% if result %}
    <div class="card-custom">
      <div class="card-header-custom">
        <h6><i class="fas fa-check-circle me-2 text-success"></i>执行结果</h6>
        <span class="badge {% if result.fail == 0 %}bg-success{% else %}bg-warning{% endif %}">
          成功 {{ result.success }} / 失败 {{ result.fail }}
        </span>
      </div>
      <div class="card-body-custom p-0" style="max-height:400px;overflow-y:auto">
        <table class="table table-custom">
          <thead><tr><th>条码</th><th>商品</th><th>数量</th><th>库存变化</th><th>状态</th></tr></thead>
          <tbody>
          {% for r in result.results %}
          <tr>
            <td><code>{{ r.barcode }}</code></td>
            <td style="font-size:.8rem">{{ r.name }}</td>
            <td>
              {% if result.mode == 'in' %}<span class="text-success">+{{ r.qty }}</span>{% endif %}
              {% if result.mode == 'out' %}<span class="text-danger">-{{ r.qty }}</span>{% endif %}
            </td>
            <td style="font-size:.8rem">
              {% if r.status == 'ok' %}{{ r.before }} → {{ r.after }}{% else %}-{% endif %}
            </td>
            <td>
              {% if r.status == 'ok' %}<span class="badge bg-success">成功</span>{% else %}<span class="badge bg-danger">{{ r.msg }}</span>{% endif %}
            </td>
          </tr>
          {% endfor %}
          </tbody>
        </table>
      </div>
    </div>
    {% endif %}
  </div>
</div>
{% endblock %}
{% block scripts %}
<script>
var ta=document.getElementById('barcodeArea');
var lc=document.getElementById('lineCount');
function updateCount(){
  var lines=ta.value.split('\n').filter(function(l){return l.trim();});
  lc.textContent=lines.length+' 个条码';
}
ta.addEventListener('input',updateCount);
// 扫码枪输入自动聚焦
ta.focus();
// 切换按钮样式
document.querySelectorAll('input[name=mode]').forEach(function(radio){
  radio.addEventListener('change',function(){
    document.querySelectorAll('input[name=mode]').forEach(function(r){
      r.parentElement.classList.remove('btn-success','btn-warning');
      r.parentElement.classList.add(r.value==='in'?'btn-outline-success':'btn-outline-warning');
    });
    this.parentElement.classList.remove('btn-outline-success','btn-outline-warning');
    this.parentElement.classList.add(this.value==='in'?'btn-success':'btn-warning');
  });
});
// 初始化选中状态
document.querySelector('input[name=mode][value=in]').parentElement.classList.remove('btn-outline-success');
document.querySelector('input[name=mode][value=in]').parentElement.classList.add('btn-success');
</script>
{% endblock %}''')

# ============================================================
# stock_manage.html
# ============================================================
W('stock_manage.html', r'''{% extends "base.html" %}
{% block title %}库存管理{% endblock %}
{% block breadcrumb %}库存管理{% endblock %}
{% block content %}
<div class="card-custom">
  <div class="card-header-custom">
    <h6><i class="fas fa-warehouse me-2 text-primary"></i>库存总览 <span class="text-muted fw-normal">({{ total }})</span></h6>
  </div>
  <div class="card-body-custom">
    <form class="row g-2 mb-3" method="GET">
      <div class="col-md-6"><input type="text" name="search" class="form-control" placeholder="搜索条码/货号/名称..." value="{{ search }}" style="border-radius:8px"></div>
      <div class="col-md-3"><button type="submit" class="btn btn-outline-primary w-100" style="border-radius:8px"><i class="fas fa-search me-1"></i>搜索</button></div>
      <div class="col-md-3"><a href="/stock/manage" class="btn btn-outline-secondary w-100" style="border-radius:8px"><i class="fas fa-rotate-left me-1"></i>重置</a></div>
    </form>
  </div>
  <div class="table-responsive">
    <table class="table table-custom">
      <thead><tr><th>条码</th><th>货号</th><th>商品名称</th><th>品牌</th><th>尺码</th><th>库存</th><th>状态</th><th>操作</th></tr></thead>
      <tbody>
      {% if items %}
      {% for item in items %}
      <tr>
        <td><code>{{ item.barcode }}</code></td>
        <td>{{ item.sku }}</td>
        <td><strong>{{ item.name }}</strong></td>
        <td>{{ item.brand }}</td>
        <td>{{ item.size }}</td>
        <td style="font-weight:700;font-size:1.1rem">
          {% if item.quantity == 0 %}<span class="text-danger">0</span>{% endif %}
          {% if item.quantity > 0 %}{% if item.quantity < 5 %}<span class="text-warning">{{ item.quantity }}</span>{% endif %}{% endif %}
          {% if item.quantity > 4 %}<span class="text-success">{{ item.quantity }}</span>{% endif %}
        </td>
        <td>
          {% if item.quantity == 0 %}<span class="badge bg-danger">缺货</span>{% endif %}
          {% if item.quantity > 0 %}{% if item.quantity < 5 %}<span class="badge bg-warning text-dark">低库存</span>{% endif %}{% endif %}
          {% if item.quantity > 4 %}<span class="badge bg-success">正常</span>{% endif %}
        </td>
        <td><button class="btn btn-sm btn-outline-primary btn-action" data-bs-toggle="modal" data-bs-target="#adj{{ item.id }}"><i class="fas fa-sliders"></i> 调整</button></td>
      </tr>
      <div class="modal fade" id="adj{{ item.id }}" tabindex="-1">
        <div class="modal-dialog"><div class="modal-content" style="border-radius:12px">
          <div class="modal-header"><h5 class="modal-title">调整库存 - {{ item.name }}</h5><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div>
          <form method="POST" action="/stock/adjust">
            <div class="modal-body">
              <input type="hidden" name="product_id" value="{{ item.id }}">
              <p class="text-muted" style="font-size:.9rem">条码: <code>{{ item.barcode }}</code> | 当前: <strong>{{ item.quantity }}</strong></p>
              <div class="mb-3"><label class="form-label">新库存数量</label><input type="number" name="quantity" class="form-control" value="{{ item.quantity }}" min="0" required></div>
              <div class="mb-3"><label class="form-label">调整原因</label><input type="text" name="remark" class="form-control" placeholder="如：盘点调整"></div>
            </div>
            <div class="modal-footer"><button type="button" class="btn btn-secondary" data-bs-dismiss="modal">取消</button><button type="submit" class="btn btn-primary"><i class="fas fa-check me-1"></i>确认</button></div>
          </form>
        </div></div>
      </div>
      {% endfor %}
      {% else %}
      <tr><td colspan="8" class="text-center text-muted py-4">暂无库存数据</td></tr>
      {% endif %}
      </tbody>
    </table>
  </div>
  {% if pages > 1 %}
  <div class="card-body-custom pt-0">
    <nav><ul class="pagination justify-content-center mb-0">
      {% for p in range(1, pages + 1) %}
      <li class="page-item"><a class="page-link" href="?page={{ p }}&search={{ search }}">{{ p }}</a></li>
      {% endfor %}
    </ul></nav>
  </div>
  {% endif %}
</div>
{% endblock %}''')

# ============================================================
# logs.html
# ============================================================
W('logs.html', r'''{% extends "base.html" %}
{% block title %}操作日志{% endblock %}
{% block breadcrumb %}操作日志{% endblock %}
{% block content %}
<div class="card-custom">
  <div class="card-header-custom">
    <h6><i class="fas fa-clock-rotate-left me-2 text-primary"></i>操作日志 <span class="text-muted fw-normal">({{ total }})</span></h6>
    <a href="/export" class="btn btn-sm btn-outline-success"><i class="fas fa-download me-1"></i>导出</a>
  </div>
  <div class="card-body-custom">
    <form class="row g-2 mb-3" method="GET">
      <div class="col-md-3"><input type="text" name="search" class="form-control" placeholder="搜索条码/货号/名称..." value="{{ search }}" style="border-radius:8px"></div>
      <div class="col-md-2">
        <select name="op_type" class="form-select" style="border-radius:8px">
          <option value="">全部类型</option>
          <option>入库</option><option>手动入库</option><option>出库</option><option>库存调整</option>
        </select>
      </div>
      <div class="col-md-2"><input type="date" name="start_date" class="form-control" value="{{ start_date }}" style="border-radius:8px"></div>
      <div class="col-md-2"><input type="date" name="end_date" class="form-control" value="{{ end_date }}" style="border-radius:8px"></div>
      <div class="col-md-1"><button type="submit" class="btn btn-outline-primary w-100" style="border-radius:8px"><i class="fas fa-filter"></i></button></div>
      <div class="col-md-2"><a href="/logs" class="btn btn-outline-secondary w-100" style="border-radius:8px"><i class="fas fa-rotate-left me-1"></i>重置</a></div>
    </form>
  </div>
  <div class="table-responsive">
    <table class="table table-custom">
      <thead><tr><th>时间</th><th>条码</th><th>货号</th><th>商品</th><th>类型</th><th>变动</th><th>库存变化</th><th>状态</th><th>备注</th></tr></thead>
      <tbody>
      {% if items %}
      {% for item in items %}
      <tr>
        <td class="text-muted" style="font-size:.8rem;white-space:nowrap">{{ item.created_at }}</td>
        <td><code>{{ item.barcode }}</code></td>
        <td>{{ item.sku }}</td>
        <td>{{ item.product_name }}</td>
        <td>
          {% if item.operation_type == '入库' %}<span class="badge bg-success-subtle text-success">入库</span>{% endif %}
          {% if item.operation_type == '手动入库' %}<span class="badge bg-success-subtle text-success">手动入库</span>{% endif %}
          {% if item.operation_type == '出库' %}<span class="badge bg-warning-subtle text-warning">出库</span>{% endif %}
          {% if item.operation_type == '库存调整' %}<span class="badge bg-info-subtle text-info">调整</span>{% endif %}
        </td>
        <td>
          {% if item.quantity_change > 0 %}<span class="text-success fw-bold">+{{ item.quantity_change }}</span>{% endif %}
          {% if item.quantity_change == 0 %}<span class="text-muted">0</span>{% endif %}
          {% if item.quantity_change < 0 %}<span class="text-danger fw-bold">{{ item.quantity_change }}</span>{% endif %}
        </td>
        <td style="font-size:.85rem">{{ item.quantity_before }} → {{ item.quantity_after }}</td>
        <td>{% if item.status == '成功' %}<span class="badge bg-success-subtle text-success">成功</span>{% else %}<span class="badge bg-danger-subtle text-danger">{{ item.status }}</span>{% endif %}</td>
        <td class="text-muted" style="font-size:.8rem">{{ item.remark }}</td>
      </tr>
      {% endfor %}
      {% else %}
      <tr><td colspan="9" class="text-center text-muted py-4">暂无日志记录</td></tr>
      {% endif %}
      </tbody>
    </table>
  </div>
  {% if pages > 1 %}
  <div class="card-body-custom pt-0">
    <nav><ul class="pagination justify-content-center mb-0">
      {% for p in range(1, pages + 1) %}
      <li class="page-item"><a class="page-link" href="?page={{ p }}&search={{ search }}&op_type={{ op_type }}&start_date={{ start_date }}&end_date={{ end_date }}">{{ p }}</a></li>
      {% endfor %}
    </ul></nav>
  </div>
  {% endif %}
</div>
{% endblock %}''')

# ============================================================
# import.html
# ============================================================
W('import.html', r'''{% extends "base.html" %}
{% block title %}数据导入{% endblock %}
{% block breadcrumb %}数据导入{% endblock %}
{% block content %}
<div class="row justify-content-center">
  <div class="col-lg-8">
    <div class="card-custom">
      <div class="card-header-custom"><h6><i class="fas fa-file-import me-2 text-primary"></i>Excel 数据导入</h6></div>
      <div class="card-body-custom">
        <div class="p-3 mb-4" style="background:#eff6ff;border-radius:10px;border-left:4px solid #3b82f6">
          <h6 style="color:#3b82f6;font-size:.9rem"><i class="fas fa-info-circle me-1"></i>导入说明</h6>
          <ul style="font-size:.85rem;color:#475569;margin:0;padding-left:1.2rem">
            <li>支持 <code>.xlsx</code> 和 <code>.xls</code> 格式</li>
            <li>自动识别表头：条码/19码、货号、商品名称、品牌、尺码、库存数量、备注</li>
            <li>已有条码自动更新，新条码自动添加</li>
            <li>支持多 Sheet 导入</li>
          </ul>
        </div>
        <form method="POST" enctype="multipart/form-data">
          <div class="text-center p-5" style="border:2px dashed #cbd5e1;border-radius:12px;background:#f8fafc">
            <i class="fas fa-cloud-upload-alt" style="font-size:3rem;color:#94a3b8;margin-bottom:1rem;display:block"></i>
            <h5 style="color:#475569">选择 Excel 文件</h5>
            <p class="text-muted" style="font-size:.85rem">支持 .xlsx / .xls 格式</p>
            <input type="file" name="file" accept=".xlsx,.xls" class="form-control mt-3" style="max-width:400px;margin:0 auto;border-radius:8px" required>
            <button type="submit" class="btn btn-primary mt-3" style="border-radius:10px;padding:.6rem 2rem"><i class="fas fa-upload me-2"></i>开始导入</button>
          </div>
        </form>
      </div>
    </div>
    <div class="row g-3 mt-3">
      <div class="col-md-6">
        <div class="card-custom"><div class="card-body-custom text-center">
          <i class="fas fa-download text-primary" style="font-size:2rem;margin-bottom:.5rem;display:block"></i>
          <h6>导出数据</h6><p class="text-muted" style="font-size:.85rem">将当前数据导出为 Excel</p>
          <a href="/export" class="btn btn-outline-primary btn-sm" style="border-radius:8px"><i class="fas fa-file-export me-1"></i>导出 Excel</a>
        </div></div>
      </div>
      <div class="col-md-6">
        <div class="card-custom"><div class="card-body-custom text-center">
          <i class="fas fa-history text-success" style="font-size:2rem;margin-bottom:.5rem;display:block"></i>
          <h6>查看日志</h6><p class="text-muted" style="font-size:.85rem">查看所有操作记录</p>
          <a href="/logs" class="btn btn-outline-success btn-sm" style="border-radius:8px"><i class="fas fa-clock-rotate-left me-1"></i>查看日志</a>
        </div></div>
      </div>
    </div>
  </div>
</div>
{% endblock %}''')

# ============================================================
# 404.html
# ============================================================
W('404.html', r'''{% extends "base.html" %}
{% block title %}页面未找到{% endblock %}
{% block content %}
<div class="text-center" style="padding:5rem 0">
  <div style="font-size:5rem;color:#cbd5e1;margin-bottom:1rem"><i class="fas fa-search"></i></div>
  <h2 style="color:#475569">404 - 页面未找到</h2>
  <p class="text-muted">您访问的页面不存在</p>
  <a href="/" class="btn btn-primary" style="border-radius:10px"><i class="fas fa-home me-1"></i>返回首页</a>
</div>
{% endblock %}''')

print(f"\n完成！共生成 {len(os.listdir(TD))} 个模板")
