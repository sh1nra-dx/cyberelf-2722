DROP TABLE IF EXISTS shop;
CREATE TABLE shop (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    sname VARCHAR(150) NOT NULL,
    command VARCHAR(20) NOT NULL,
    cabinet_count INT UNSIGNED NOT NULL DEFAULT 1,
    single_max_capacity INT UNSIGNED NOT NULL,
    player_count INT UNSIGNED NOT NULL DEFAULT 0,
    update_time DATETIME NOT NULL,
    PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET = 'utf8';

INSERT INTO shop (id, sname, command, cabinet_count, single_max_capacity,  update_time) VALUES
(1, '疯狂牛仔城舞萌DX', 'nzcmai', 1, 10, NOW()),
(2, '天空之城舞萌DX', 'wdmai', 1, 10, NOW())
(3, '城市广场华卡音舞', 'cgwacca', 1, 8, NOW()),
(4, '顺盈时代广场华卡音舞', 'sywacca', 1, 8, NOW());
