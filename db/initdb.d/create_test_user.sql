-- test_userテーブル作成用

CREATE TABLE test_user (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(128) NOT NULL,
    PRIMARY KEY (id)
);
