create database az CHARACTER set utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 回放表结构
CREATE TABLE `vod_list` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `app_id` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '微吼云ID',
  `vod_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `status` tinyint(3) unsigned DEFAULT '0' COMMENT '0 待执行 1 成功 2 失败',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_vod_id` (`vod_id`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='回放列表';

-- 流媒体导入数据
CREATE TABLE `vod_info`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `app_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '应用ID',
  `vod_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '点播ID',
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `room_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `source` tinyint(1) NOT NULL DEFAULT 0 COMMENT '类型 0（直播生成回放），1（上传视频点播）',
  `status` tinyint(1) NOT NULL DEFAULT 0 COMMENT '点播状态，0已发布',
  `record_status` tinyint(1) NOT NULL DEFAULT 0 COMMENT '回放是否生成成功，0:默认值，没有回调或者进行中；1：成功；2：失败',
  `duration` int(11) NOT NULL DEFAULT 0 COMMENT '时长,单位：秒',
  `storage` int(11) NOT NULL DEFAULT 0 COMMENT '占据空间大小KB',
  `msg_path` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '文档消息文件路径',
  `snapshot_path` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '封面图片文件路径',
  `audit_status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '审核状态:0 上线  1待审核 2下线',
  `video_points` int(4) NOT NULL DEFAULT 0 COMMENT '视频鉴黄分数',
  `transcode_status` tinyint(4) NOT NULL DEFAULT 0 COMMENT '转码状态:0新增排队中 1转码成功 2转码失败 3转码中 4转码部分成功',
  `transcode_code` int(4) NOT NULL DEFAULT 0 COMMENT '转码流媒体返回code码',
  `is_edited` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否是剪辑点播，0不是，1为是',
  `record_mode` tinyint(1) NOT NULL DEFAULT 0 COMMENT '回放场景类型 0（通过接口生成），1（直播录制自动生成），2（临时预览生成）',
  `is_deleted` tinyint(1) NOT NULL DEFAULT 0 COMMENT '1为已删除,默认为零',
  `cate_id` int(11) UNSIGNED NOT NULL DEFAULT 0 COMMENT '视频分类id',
  `has_subtitle` tinyint(4) NOT NULL DEFAULT 0 COMMENT '点播是否含有字幕,0: 无,1:有',
  `is_safe` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否开启加密, 0不加密，1开启加密',
  `doc_title_status` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否包含文档章节, 0:不包含，1:包含',
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `deleted_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '删除时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `vodid`(`vod_id`) USING BTREE,
  INDEX `type`(`source`) USING BTREE,
  INDEX `vod_list_index`(`is_deleted`, `app_id`, `room_id`, `status`, `created_at`) USING BTREE,
  INDEX `vod_statistics_index`(`is_deleted`, `created_at`, `app_id`) USING BTREE
) ENGINE = InnoDB  CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '点播记录表 ' ROW_FORMAT = Compact;

CREATE TABLE `rooms`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `room_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '房间ID',
  `app_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL DEFAULT '' COMMENT '应用ID',
  `is_disable` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否封闭 默认 0 未封闭 1 封闭',
  `is_demo` tinyint(1) UNSIGNED NULL DEFAULT 0 COMMENT '是否演示房间: 0 否 1 是',
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  `push_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '推流时间',
  `type` tinyint(1) NOT NULL DEFAULT 0 COMMENT '房间类型 0 普通房间 1 答题卡房间',
  `stream_status` tinyint(1) UNSIGNED NOT NULL DEFAULT 2 COMMENT '流状态,  1为推流中,2为未推流',
  `end_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '推流结束时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `rooms_room_id_index`(`room_id`) USING BTREE,
  INDEX `rooms_app_id_index`(`app_id`) USING BTREE,
  INDEX `is_disable`(`is_disable`) USING BTREE,
  INDEX `is_demo`(`is_demo`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Compact;

-- use mysql -uroot -p
-- source /Users/nelsonking/Downloads/rooms_20541bf7.sql;
-- source /Users/nelsonking/Downloads/rooms_bca53047.sql;

-- source /Users/nelsonking/Downloads/vod_info_20541bf7.sql;
-- source /Users/nelsonking/Downloads/vod_info_bca53047.sql;

INSERT INTO vod_list(`app_id`,`vod_id`) select `app_id`,`vod_id` FROM vod_info;



-------------- dev -----------------

-- 测试初始化
-- update vod_list set status = 0;

-- 查看剩余数量
-- select count(*) from vod_list where status = 0;