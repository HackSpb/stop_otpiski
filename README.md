# stop_otpiski

## API:

**получить все проблемы**
__запрос__: `GET  /api/issue`
__ответ__: ```[{
            "id": 123,
            "user": {
                "id": 1245,
                "user_name": "name"
            }, "title": "title_value"
}]```

**получить конкретную проблемы**
__запрос__: `GET  /api/issue?id=<id_of_issue>`
__ответ__: ```{
            "id": 123,
            "user": {
                "id": 1245,
                "user_name": "name"
            }, "title": "title_value"
}```

**создать проблему**
__запрос__: `POST  /api/issue`
__данные__: ```{
    "title": "title_value",
    "text": "some_text"
}```
__ответ__:  `{"id": 123}`

**получить все комменты по проблеме**
__запрос__: `GET  /api/comment?issue_id=<id_of_issue>`
__ответ__: ```[{
            "id": 15323, 
            "text": "comment_text",
            "date": "Sun Dec 15 19:52:16 2019",
            "user": "user": {
                "id": 1245,
                "user_name": "name"
            }, "issue_id": 4563}]```

**создать коммент к проблеме**
__запрос__: `POST  /api/issue`
__данные__: ```{
    "text": "some_text",
    "issue_id": 1446
}```
__ответ__:  `{"id": 123}`
