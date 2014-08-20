
-- Table: book
CREATE TABLE book ( 
    id   INTEGER         NOT NULL,
    name VARCHAR( 255 ),
    PRIMARY KEY ( id ) 
);

INSERT INTO [book] ([id], [name]) VALUES (1, '������� ����');
INSERT INTO [book] ([id], [name]) VALUES (2, '������ � ���������');
INSERT INTO [book] ([id], [name]) VALUES (3, '���');
INSERT INTO [book] ([id], [name]) VALUES (4, '�������');
INSERT INTO [book] ([id], [name]) VALUES (5, '������ �������');
INSERT INTO [book] ([id], [name]) VALUES (6, '������ ������');

-- Table: author
CREATE TABLE author ( 
    id   INTEGER         NOT NULL,
    name VARCHAR( 255 ),
    PRIMARY KEY ( id ) 
);

INSERT INTO [author] ([id], [name]) VALUES (1, '������� ���������� ������');
INSERT INTO [author] ([id], [name]) VALUES (2, '�. ��������');
INSERT INTO [author] ([id], [name]) VALUES (3, '����� ���������� �����������');
INSERT INTO [author] ([id], [name]) VALUES (4, '�������� �������');

-- Table: author_book
CREATE TABLE author_book ( 
    author_id INTEGER NOT NULL,
    book_id   INTEGER NOT NULL,
    PRIMARY KEY ( author_id, book_id ),
    FOREIGN KEY ( author_id ) REFERENCES author ( id ),
    FOREIGN KEY ( book_id ) REFERENCES book ( id ) 
);

INSERT INTO [author_book] ([author_id], [book_id]) VALUES (1, 1);
INSERT INTO [author_book] ([author_id], [book_id]) VALUES (1, 3);
INSERT INTO [author_book] ([author_id], [book_id]) VALUES (2, 2);
INSERT INTO [author_book] ([author_id], [book_id]) VALUES (2, 6);
INSERT INTO [author_book] ([author_id], [book_id]) VALUES (3, 4);
INSERT INTO [author_book] ([author_id], [book_id]) VALUES (3, 5);
INSERT INTO [author_book] ([author_id], [book_id]) VALUES (4, 6);
