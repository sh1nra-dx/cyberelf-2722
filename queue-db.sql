DROP TABLE IF EXISTS queue_shop;
CREATE TABLE queue_shop (
    shop_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    region_id INT UNSIGNED NOT NULL,
    shop_name VARCHAR(150) NOT NULL,
    command VARCHAR(20) NOT NULL,
    cabinet_count INT UNSIGNED NOT NULL DEFAULT 1,
    single_max_capacity INT UNSIGNED NOT NULL,
    player_count INT UNSIGNED NOT NULL DEFAULT 0,
    update_time DATETIME NOT NULL,
    PRIMARY KEY (shop_id)
) ENGINE = InnoDB DEFAULT CHARSET = 'utf8';

DROP TABLE IF EXISTS queue_region;
CREATE TABLE queue_region (
    region_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    region_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (region_id)
) ENGINE = InnoDB DEFAULT CHARSET = 'utf8';

DROP TABLE IF EXISTS qun_queue;
CREATE TABLE qun_queue (
    qun_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    region_id INT UNSIGNED NOT NULL,
    qun_uim VARCHAR(50) NOT NULL,
    PRIMARY KEY (qun_id)
) ENGINE = InnoDB DEFAULT CHARSET = 'utf8';

DROP TABLE IF EXISTS qun_maimaidx;
CREATE TABLE qun_maimaidx (
    qun_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    qun_uim VARCHAR(50) NOT NULL,
    PRIMARY KEY (qun_id)
) ENGINE = InnoDB DEFAULT CHARSET = 'utf8';

INSERT INTO queue_region (region_id, region_name) VALUES
(1, '清远'),
(2, '贵阳'),
(3, '贺州');

INSERT INTO queue_shop (shop_id, region_id, shop_name, command, cabinet_count, single_max_capacity, update_time) VALUES
/* 清远 */
(0, 1, '牛仔城舞萌DX', 'nzmai', 1, 8, NOW()),
(0, 1, '万达舞萌DX', 'wdmai', 1, 8, NOW()),
(0, 1, '城广舞萌DX', 'cgmai', 1, 8, NOW()),
(0, 1, '大润发舞萌DX', 'drfmai', 1, 8, NOW()),
(0, 1, '极限主场华卡音舞', 'cgwa', 2, 5, NOW()),
(0, 1, '开心主场华卡音舞', 'sywa', 2, 5, NOW()),
/* 贵阳 */
(0, 2, '花溪-万宜欢乐工坊', 'wy', 1, 8, NOW()),
(0, 2, '云岩-风云再起', 'fy', 1, 8, NOW()),
(0, 2, '南明-亨特大玩家', 'ht', 1, 8, NOW()),
(0, 2, '观山湖-万象汇星际传奇', 'wx', 1, 8, NOW()),
(0, 2, '观山湖-万达大玩家', 'wd', 1, 8, NOW()),
(0, 2, '观山湖-玖福城梦时代', 'jf', 1, 8, NOW()),
/* 贺州 */
(0, 3, '欢乐哆新旺角店舞萌DX', 'mai', 2, 8, NOW());

INSERT INTO qun_queue (qun_id, region_id, qun_uim) VALUES
(0, 1, '932678745'),
(0, 1, '917440536'),
(0, 1, '742601422'),
(0, 2, '574288172'),
(0, 3, '275331173');

INSERT INTO qun_maimaidx (qun_id, qun_uim) VALUES
(0, '932678745'),
(0, '742601422'),
(0, '995093868');
