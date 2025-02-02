Feature: Profile Page Testing

  Scenario: My profile
    Given Open "dev" environment
    Then The user enters "houseattheocean@gmail.com" into the "my_email" field
    Then The user enters "mCtwAtjpizSTWEz7" into the "my_password" field

#    Then Type "houseattheocean@gmail.com" into "my_email"
#    Then Type "mCtwAtjpizSTWEz7" into "my_password"
    Then Click element "my_login_button"
    Then Click element "my_profile_icon"
    Then Click element "page_my_profile"
    Then Type "John" into "first_name_field"
    Then Type "Kennedy" into "last_name_field"
    Then Verify text "houseattheocean@gmail.com" is in "email_field"
    Then Click element "add_phone_button"
    # check xpath:
    Then Click element "select_prefix"
    Then Click element "prefix_us"
    Then Type "550-55-50" into "enter_phone"
    Then Toggle SMS acceptance to True
    Then Click element "save_button"
    Then Verify the "change_password_h5" page is displayed
    Then Type "mCtwAtjpizSTWEz7" into "current_password_field"
    Then Type "7563259BuyaCat" into "new_password_field"
    Then Type "7563259BuyaCat" into "confirm_password_field"
    Then Click element "change_password_button"











