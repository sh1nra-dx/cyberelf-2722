DROP TABLE IF EXISTS shop;
CREATE TABLE shop (
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

DROP TABLE IF EXISTS region;
CREATE TABLE region (
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

INSERT INTO region (region_id, region_name) VALUES
(1, '清远'),
(2, '贵阳');

INSERT INTO shop (shop_id, region_id, shop_name, command, cabinet_count, single_max_capacity, update_time) VALUES
/* 清远 */
(1, 1, '疯狂牛仔城舞萌DX', 'nzcmai', 1, 8, NOW()),
(2, 1, '天空之城舞萌DX', 'wdmai', 1, 8, NOW()),
(3, 1, '极限主场舞萌DX', 'cgmai', 1, 8, NOW()),
(4, 1, '极限主场华卡音舞', 'cgwa', 2, 5, NOW()),
(5, 1, '开心主场华卡音舞', 'sywa', 2, 5, NOW()),
/* 贵阳 */
(6, 2, '花溪-万宜欢乐工坊', 'wy', 1, 8, NOW()),
(7, 2, '云岩-风云再起', 'fy', 1, 8, NOW()),
(8, 2, '南明-亨特大玩家', 'ht', 1, 8, NOW()),
(9, 2, '观山湖-万象汇星际传奇', 'wx', 1, 8, NOW()),
(10, 2, '观山湖-万达大玩家', 'wd', 1, 8, NOW()),
(11, 2, '观山湖-玖福城梦时代', 'jf', 1, 8, NOW());

INSERT INTO qun_queue (qun_id, region_id, qun_uim) VALUES
(0, 1, '917440536'),
(0, 1, '742601422'),
(0, 2, '574288172');

INSERT INTO qun_maimaidx (qun_id, qun_uim) VALUES
(0, '742601422'),
(0, '995093868');
