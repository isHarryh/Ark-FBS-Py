Ark-FBS-Py
==========
Complied Arknights FlatBuffers Schema for Python.  
Forked from [MooncellWiki/OpenArknightsFBS](https://github.com/MooncellWiki/OpenArknightsFBS).

本仓库包含了已经编译到 **Python** 的《明日方舟（CN）》[FlatBuffers](https://flatbuffers.dev) 二进制数据格式的 Schema 架构文件（FBS）。

### OpenArknightsFBS

本仓库使用的源 FBS 文件均来源于 [OpenArknightsFBS](https://github.com/MooncellWiki/OpenArknightsFBS) 仓库，其所有 Schema 定义均为从游戏内部结构解析生成的。

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
