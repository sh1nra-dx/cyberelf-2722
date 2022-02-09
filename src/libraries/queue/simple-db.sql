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
(1, '疯狂牛仔城清远宝银旺店', 'nzc', 1, 10, NOW()),
(2, '天空之城清远万达店', 'wd', 1, 10, NOW());
