# sql_requests.py
# MM 2020 7 avril
# module of sql request string

# -----------
# CATEGORY  |
# -----------

# get all category
index_category = "SELECT * FROM T_Category"

# show one category NEED ARGUMENT id_category
show_category = "SELECT * FROM `T_Category` WHERE `id_category` = %(id_category)s "

# create category
create_category = (
    "INSERT INTO `T_Category` (`id_category`, `name`, `description`, `created_at`) VALUES (NULL, "
    "%(name)s, %(description)s, CURRENT_TIMESTAMP); "
)

# update category

update_category = (
    "UPDATE `T_Category` SET `name` = %(name)s, `description` = %(description)s WHERE "
    "`T_Category`.`id_category` = %(id)s; "
)

# delete category

delete_category = (
    "DELETE FROM `T_Category` WHERE T_Category.id_category = %(id_category)s;"
)

# -----------
# ITEM  |
# -----------

# create item
create_item = (
    "INSERT INTO `T_Item` (`id_item`, `fk_category`, `name`, `description`, `created_at`) VALUES (NULL, "
    "%(id_category)s, %(name)s, %(description)s, CURRENT_TIMESTAMP); "
)

# update item
update_item = (
    "UPDATE `T_Item` SET `name` = %(name)s, `description` = %(description)s WHERE `T_Item`.`id_item` = %("
    "id)s; "
)

# delete key contrainte and delete item
delete_item = (
    "UPDATE `T_Tiqet` SET `fk_item`= NULL WHERE `T_Tiqet`.`fk_item` = %(id_item)s;"
)

delete_item_2 = "DELETE FROM `T_Item` WHERE T_Item.id_item = %(id_item)s;"

# show item by category NEED ID_CATEGORY
show_item_by_category = "SELECT * FROM `T_Item` WHERE `fk_category` = %(id_category)s "

# -----------
# TIQET  |
# -----------

# create tiqet
create_tiqet = """INSERT INTO `T_Tiqet` (`id_tiqet`, `fk_priority`, `fk_reporter`, `fk_assigned`, `fk_item`, `title`, 
`content`, `fk_state`, `created_at`) VALUES (NULL, %(id_priority)s, %(id_reporter)s, %(id_assigned)s, %(id_item)s, 
%(title)s, %(content)s, %(id_state)s, CURRENT_TIMESTAMP); """

# get index of tiqet, inner join STATE, PRIORITY etc
index_tiqet = """ SELECT T_Tiqet.id_tiqet, T_Tiqet.title, T_Tiqet.content, T_Tiqet.created_at, 
                  T_Priority.id_priority, T_Priority.name AS "name_priority", 
                  T_State.id_state, T_State.name as "name_state",
                  T_Item.id_item, T_Item.name as "name_item", T_Item.fk_category as "id_category",
                  T_User.id_user, T_User.username
                  FROM T_Tiqet 
                  LEFT OUTER JOIN T_Priority ON T_Tiqet.fk_priority= T_Priority.id_priority
                  LEFT OUTER JOIN T_State ON T_Tiqet.fk_state = T_State.id_state
                  LEFT OUTER JOIN T_Item ON T_Tiqet.fk_item = T_Item.id_item
                  LEFT OUTER JOIN T_User ON T_Tiqet.fk_assigned = T_User.id_user
                  ORDER BY T_Tiqet.created_at  """

# edit only the state of the tiqet
edit_state_tiqet = "UPDATE `T_Tiqet` SET `fk_state` = %(id_state)s WHERE `T_Tiqet`.`id_tiqet` = %(id_tiqet)s;"


def tiqet_edit_request(values, id_tiqet):
    request = "UPDATE `T_Tiqet` SET "
    params = {
        "title",
        "content",
        "state",
        "fk_priority",
        "fk_reporter",
        "fk_assigned",
        "fk_item",
        "fk_state",
    }
    first = True

    for param in params:
        if param in values:
            if not first:
                request += ", "
            request += f"`{param}` = %({param})s"
            first = False

    request += f" WHERE `T_Tiqet`.`id_tiqet` = {id_tiqet}"
    return request


show_tiqet = """ SELECT T_Tiqet.id_tiqet, T_Tiqet.title, T_Tiqet.content, T_Tiqet.created_at, 
                  T_Priority.id_priority, T_Priority.name AS "name_priority", 
                  T_State.id_state, T_State.name as "name_state",
                  T_Item.id_item, T_Item.name as "name_item", T_Item.fk_category as "id_category",
                  T_User.id_user, T_User.username
                  FROM T_Tiqet 
                  LEFT OUTER JOIN T_Priority ON T_Tiqet.fk_priority= T_Priority.id_priority
                  LEFT OUTER JOIN T_State ON T_Tiqet.fk_state = T_State.id_state
                  LEFT OUTER JOIN T_Item ON T_Tiqet.fk_item = T_Item.id_item
                  LEFT OUTER JOIN T_User ON T_Tiqet.fk_assigned = T_User.id_user
                  WHERE `T_Tiqet`.`id_tiqet` = %(id_tiqet)s  """

# -----------
# STATE  |
# -----------

#  index of state
index_state = "SELECT * FROM `T_State`"

edit_state = "UPDATE `T_State` SET `name` = %(name)s, `display` = %(display)s WHERE `T_State`.`id_state` = %(id_state)s; "

create_state = "INSERT INTO `T_State` (`id_state`, `name`, `display`, `created_at`) VALUES (NULL, %(name)s, '1', CURRENT_TIMESTAMP); "

delete_key_state = "DELETE FROM `T_Tiqet` WHERE fk_state = %(id_state)s"

delete_state = "DELETE FROM `T_State` WHERE T_State.id_state = %(id_state)s;"

# -----------
# PRIORITY  |
# -----------

#  index of priority
index_priorities = "SELECT * FROM `T_Priority` ORDER BY `T_Priority`.`level` DESC "

edit_priority = """ UPDATE `T_Priority` SET `name` = %(name)s, `level` = %(level)s, `description` = %(description)s WHERE `T_Priority`.`id_priority` = %(id_priority)s;  """

create_priority = """ INSERT INTO `T_Priority` (`id_priority`, `name`, `level`, `description`, `created_at`) VALUES (NULL, %(name)s, %(level)s, %(description)s, CURRENT_TIMESTAMP);  """

delete_key_priority = "UPDATE `T_Tiqet` SET `fk_priority` = NULL WHERE `T_Tiqet`.`fk_priority` = %(id_priority)s;"

delete_priority = (
    "DELETE FROM `T_Priority` WHERE T_Priority.id_priority = %(id_priority)s;"
)
# -----------
# USERS     |
# -----------

# index of users
index_users = "SELECT * FROM `T_User` "

# -----------
# COMMENT     |
# -----------

index_comments = """ SELECT T_Comment.fk_tiqet as "id_tiqet", T_Comment.id_comment, T_Comment.created_at,
                    T_Comment.content,  T_User.id_user,  T_User.username
                    FROM T_Comment 
                    LEFT OUTER JOIN T_User ON T_Comment.fk_author = T_User.id_user WHERE fk_tiqet = %(id_tiqet)s 
                    ORDER BY T_Comment.created_at """

create_comment = """ INSERT INTO `T_Comment` (`id_comment`, `fk_author`, `fk_tiqet`, `content`, `created_at`) VALUES (NULL, %(id_user)s, %(id_tiqet)s, %(content)s, CURRENT_TIMESTAMP); """


# -----------
# USER     |
# -----------

auth_login = """ SELECT * FROM `T_User` WHERE lower(username) = lower(%(username)s) OR lower(email) = lower(%(username)s) """

auth_token_login = """ SELECT * FROM `T_User` WHERE `id_user` = %(id_user)s """

auth_create = """ INSERT INTO `T_User` (`id_user`, `username`, `firstname`, `lastname`, `email`, `password`, `created_at`) VALUES (NULL, %(username)s, %(firstname)s, %(lastname)s, %(email)s, %(password)s, CURRENT_TIMESTAMP); """

auth_check_username = """ SELECT * FROM `T_User` WHERE `username` = %(username)s """

auth_check_email = """ SELECT * FROM `T_User` WHERE `email` = %(email)s """

auth_safe_edit = """ UPDATE `T_User` SET `firstname` = %(firstname)s, `lastname` = %(lastname)s, `email` = %(email)s WHERE `T_User`.`id_user` = %(id_user)s;  """

auth_edit_password = """ UPDATE `T_User` SET `password` = %(new_password)s WHERE `T_User`.`id_user` = %(id_user)s;  """


# -----------
# LABEL     |
# -----------

show_label_by_tiqet = """ SELECT T_Tiqet.id_tiqet, T_Label.id_label, T_Label.name, T_Label.color
FROM T_Tiqet
JOIN T_Tiqet_to_Label ON T_Tiqet.id_tiqet = T_Tiqet_to_Label.fk_tiqet
JOIN T_Label ON T_Tiqet_to_Label.fk_label = T_Label.id_label
WHERE T_Tiqet.id_tiqet = %(id_tiqet)s """

create_label = """ INSERT INTO `T_Label` (`id_label`, `name`, `description`, `color`, `created_at`) VALUES (NULL, %(name)s, %(description)s, %(color)s, CURRENT_TIMESTAMP); """

edit_label = """ UPDATE `T_Label` SET `name` = %(name)s, `description` = %(description)s, `color` = %(color)s WHERE `T_Label`.`id_label` = %(id_label)s ;  """

index_label = """ SELECT * FROM `T_Label`  """

delete_key_label = "UPDATE `T_Tiqet_to_Label` SET `fk_label` = NULL WHERE `T_Tiqet_to_Label`.`fk_label` = %(id_label)s;"

delete_label = "DELETE FROM `T_Label` WHERE T_Label.id_label = %(id_label)s;"

delete_tiqet_label_reation = "DELETE FROM `T_Tiqet_to_Label` WHERE T_Tiqet_to_Label.fk_tiqet = %(id_tiqet)s AND T_Tiqet_to_Label.fk_label = %(id_label)s"

create_tiqet_label_reation = "INSERT INTO `T_Tiqet_to_Label` (`id_tiqet_to_label`, `fk_tiqet`, `fk_label`, `created_at`) VALUES (NULL, %(id_tiqet)s, %(id_label)s, CURRENT_TIMESTAMP);"
