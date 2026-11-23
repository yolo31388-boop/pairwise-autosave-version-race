# pairwise-autosave-version-race

## 领域

游戏、图形与多媒体

## 主题

自动存档版本迁移

## 说明

写盘互斥、原子替换与半写校验。

初始状态下 `gameplay/autosave_version_race.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
