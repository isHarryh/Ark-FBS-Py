Ark-FBS-Py
==========
Complied Arknights FlatBuffers Schema for Python.  
Forked from [MooncellWiki/OpenArknightsFBS](https://github.com/MooncellWiki/OpenArknightsFBS).

## 简介

本仓库的 [`dist`](https://github.com/isHarryh/Ark-FBS-Py/tree/dist) 分支内包含了已经编译到 **Python** 的《明日方舟（CN）》[FlatBuffers](https://flatbuffers.dev) 二进制数据格式的 Schema 结构文件（FBS）。

当前分支 `main` 仅用于存储和同步 FBS 源文件和编译所用的脚本。

### 编译方法

1. 安装 Python 3 并克隆本仓库。
2. 下载 FlatBuffers 编译器 [flatc](https://github.com/google/flatbuffers/releases) 到仓库根目录。
3. 运行 `Compile.py` 脚本，等待编译完成。
4. 在生成的目录中查看已编译的文件。

> [!NOTE]
> 
> 为了便于使用编译后的对象，每个对象模块都被额外加入了 `ROOT_TYPE` 常量用于指示根对象的类型。

### 变更日志

- 2026 年 11 月：本仓库编译所用的 FlatBuffers 版本升级到 **24.12.23**，生成的 Python 文件有以下变动：
  - 所有 `Def_` 被更名为 `Def`；
  - 所有 `clz_...AddDef_` 被更名为 `clz_...AddDef`。

- 2024 年 6 月：本仓库的 `dist` 分支已可供使用。编译所用的 FlatBuffers 版本为 **24.3.25**。

---

> [!IMPORTANT]
>
> 下面的内容来自上游仓库 [MooncellWiki/OpenArknightsFBS](https://github.com/MooncellWiki/OpenArknightsFBS) 的 README 说明。

# OpenArknightsFBS

本仓库包含了简中版 2.0.01 版本开始使用的 FlatBuffers 二进制数据格式对应的 Schema 文件。

目前所有 Schema 定义均为从游戏内部结构解析生成。

### 共建指南

感谢您为 OpenArknightsFBS 贡献内容，在您编写或修改对应的 FBS 文件前，请阅读以下的共建指南。

- 1.请阅读[FlatBuffers: Grammer of the schema language](https://flatbuffers.dev/flatbuffers_grammar.html)，学习如何编写正确的 FBS 文件。
- 2.在对 FBS 完成编写后，请使用 [FlatBuffers Compiler](https://github.com/google/flatbuffers/releases) `flatc` 对当前版本的最新数据文件使用来验证您编写的 FBS。
```bash
.\flatc.exe --json --raw-binary ".\FBS\chapter_table.fbs" -- .\chapter_table.json --strict-json --natural-utf8
```
- 3.请验证您编写的 FBS 中的字段名和数量是否与官方 JSON 一致。`JsonPropertyAttribute` `JsonIgnoreAttribute`

目前版本(CN 2.0.40)有以下数据文件使用 FlatBuffers 格式：

**/**
- buff_table

**/excel/**
- activity_table
- building_data
- campaign_table
- chapter_table
- char_meta_table
- char_patch_table
- character_table
- charm_table
- charword_table
- checkin_table
- climb_tower_table
- enemy_handbook_table
- favor_table
- gacha_table
- gamedata_const
- handbook_info_table
- item_table
- medal_table
- mission_table
- open_server_table
- replicate_table
- retro_table
- roguelike_topic_table
- sandbox_table
- shop_client_table
- skill_table
- skin_table
- stage_table
- story_review_meta_table
- story_review_table
- story_table
- token_table
- uniequip_table
- zone_table

**/levels/enemydata/**
- enemy_database

**/battle/**
- ep_breakbuff_table
- extra_battlelog_table

**/levels/**
- \*
