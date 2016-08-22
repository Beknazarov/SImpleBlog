Feature: Simple Blog
  Scenario: Registration
    Open "register_user" page
    Name "username" value "test"
    Name "password" value "123"
    Name "email" value "nurs@gmail.com"
    Click "register"

  Scenario: Login
    Open "login_user" page
    Name "username" value "test"
    Name "password" value "123"
    Click "login"

  Scenario: CreatePost
    Open "create_post" page
    Name "title" value "python django tutorial"
    Name "description" value "THe best language in the world"
    Click "create"

  Scenario: CreatePost
    Open "create_post" page
    Name "title" value "c++ tutorial"
    Name "description" value "THe olympic language in the world"
    Click "create"

  Scenario: UpdatePost
    Open "update_post" page
    Click "update_link"
    Name "title" value "python django + java tutorial"
    Name "description" value "THe best language in the world and one of the world"
    Click "update"

  Scenario: DeletePost
    Open "delete_post" page
    Click2 "delete"

  Scenario: Logout
    Open "logout" page
    Click2 "logout_link"

  Scenario: Home
    Open "home" page
#
#  Scenario: Search pc fail
#    Open "pc_search" page
#    Click "computers"
#    Click "notebook"
#    See "27012" in "model_number"