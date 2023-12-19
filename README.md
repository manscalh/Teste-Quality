# Prerequisites
* python 

# Install Linux

* open new terminal in project root folder
* delete .venv if already exists
* install new venv: python3 -m venv .venv
* activate venv:  source .venv/bin/activate
* install dependencies: pip install -r requirements.txt
* to execute all tests run: python3 -m unittest  -v tests/Test*.py

# Install Windows

* open new terminal in project root folder
* delete .venv if already exists
* install new venv: python -m venv .venv
* activate venv:  .\.venv\Scripts\activate
* install dependencies: pip install -r requirements.txt
* to execute all tests: python -m unittest discover -v "Test*.py" -s tests

# Tests Results (Linux)

python3 -m unittest  -v tests/Test*.py

test_CT23_continue_shopping_stardard_user (tests.TestCartContinueShopping.TestCartContinueShopping) ... ok
test_CT22_remove_cart_error_user (tests.TestCartPageCart.TestCartPageCart) ... ok
test_CT16_add_cart_standard_user (tests.TestCartPageInventory.TestCartPageInvetory) ... ok
test_CT17_remove_cart_standard_user (tests.TestCartPageInventory.TestCartPageInvetory) ... ok
test_CT18_add_cart_problem_user (tests.TestCartPageInventory.TestCartPageInvetory) ... ok
test_CT19_remove_cart_problem_user (tests.TestCartPageInventory.TestCartPageInvetory) ... ok
test_CT20_add_cart_error_user (tests.TestCartPageInventory.TestCartPageInvetory) ... ok
test_CT21_remove_cart_error_user (tests.TestCartPageInventory.TestCartPageInvetory) ... ok
test_CT24_checkout_firtname_empty_standard_user (tests.TestCheckout.TestCheckout) ... ok
test_CT25_checkout_lastname_empty_standard_user (tests.TestCheckout.TestCheckout) ... ok
test_CT26_checkout_zipcode_empty_standard_user (tests.TestCheckout.TestCheckout) ... ok
test_CT27_checkout_firtname_standard_user (tests.TestCheckout.TestCheckout) ... ok
test_CT28_checkout_lastname_standard_user (tests.TestCheckout.TestCheckout) ... ok
test_CT29_checkout_zipcode_standard_user (tests.TestCheckout.TestCheckout) ... ok
test_CT30_checkout_cancel_standard_user (tests.TestCheckout.TestCheckout) ... ok
test_CT31_checkout_finish_standard_user (tests.TestCheckout.TestCheckout) ... ok
test_CT01_standard_user_login (tests.TestLoginPage.TestLoginPage) ... ok
test_CT02_locked_out_user_login (tests.TestLoginPage.TestLoginPage) ... ok
test_CT03_empty_login (tests.TestLoginPage.TestLoginPage) ... ok
test_CT04_problem_user_Login (tests.TestLoginPage.TestLoginPage) ... ok
test_CT05_performance_glitch_user_login (tests.TestLoginPage.TestLoginPage) ... ok
test_CT06_error_user_login (tests.TestLoginPage.TestLoginPage) ... ok
test_CT07_visual_user_login (tests.TestLoginPage.TestLoginPage) ... ok
test_CT11_logout (tests.TestLogout.TestLogout) ... ok
test_CT08_default_password (tests.TestPassword.TestPassword) ... ok
test_CT09_empty_password (tests.TestPassword.TestPassword) ... ok
test_CT10_invalid_password (tests.TestPassword.TestPassword) ... ok
test_CT12_Sort_Z_to_A (tests.TestSort.TestSort) ... ok
test_CT13_Sort_A_to_Z (tests.TestSort.TestSort) ... ok
test_CT14_sort_price_low_to_high (tests.TestSort.TestSort) ... ok
test_CT15_sort_price_high_to_low (tests.TestSort.TestSort) ... ok

----------------------------------------------------------------------
Ran 31 tests in 220.842s

OK


# Tests Results (Windows)

python -m unittest discover -v "Test*.py" -s tests

test_CT23_continue_shopping_stardard_user (TestCartContinueShopping.TestCartContinueShopping.test_CT23_continue_shopping_stardard_user) ... 
DevTools listening on ws://127.0.0.1:52343/devtools/browser/c1aa0300-3850-458a-91c9-177bf47fdac9
ok
test_CT22_remove_cart_error_user (TestCartPageCart.TestCartPageCart.test_CT22_remove_cart_error_user) ... 
DevTools listening on ws://127.0.0.1:52370/devtools/browser/9806ce74-7859-4c26-a2cc-eac2ca25070f
ok
test_CT16_add_cart_standard_user (TestCartPageInventory.TestCartPageInvetory.test_CT16_add_cart_standard_user) ... 
DevTools listening on ws://127.0.0.1:52399/devtools/browser/7c09c421-2f1f-41f2-8e25-3e443f116cff
ok
test_CT17_remove_cart_standard_user (TestCartPageInventory.TestCartPageInvetory.test_CT17_remove_cart_standard_user) ... 
DevTools listening on ws://127.0.0.1:52428/devtools/browser/1fa32754-d3cd-454e-b05a-3a68621b0383
ok
test_CT18_add_cart_problem_user (TestCartPageInventory.TestCartPageInvetory.test_CT18_add_cart_problem_user) ... 
DevTools listening on ws://127.0.0.1:52455/devtools/browser/d5b27613-9ab1-45e2-bc19-4389ac2324e1
ok
test_CT19_remove_cart_problem_user (TestCartPageInventory.TestCartPageInvetory.test_CT19_remove_cart_problem_user) ... 
DevTools listening on ws://127.0.0.1:52484/devtools/browser/24ef2461-79e4-46aa-be8f-c6efa888c6fc
ok
test_CT20_add_cart_error_user (TestCartPageInventory.TestCartPageInvetory.test_CT20_add_cart_error_user) ... 
DevTools listening on ws://127.0.0.1:52518/devtools/browser/f342a18f-4f91-476e-aec8-2c9432287337
ok
test_CT21_remove_cart_error_user (TestCartPageInventory.TestCartPageInvetory.test_CT21_remove_cart_error_user) ... 
DevTools listening on ws://127.0.0.1:52548/devtools/browser/372e34a0-0c60-4180-bd8e-f84f754d9779
ok
test_CT24_checkout_firtname_empty_standard_user (TestCheckout.TestCheckout.test_CT24_checkout_firtname_empty_standard_user) ... 
DevTools listening on ws://127.0.0.1:52577/devtools/browser/a34dbf83-06c1-4517-bdec-31ba5fd41cd3
ok
test_CT25_checkout_lastname_empty_standard_user (TestCheckout.TestCheckout.test_CT25_checkout_lastname_empty_standard_user) ... 
DevTools listening on ws://127.0.0.1:52606/devtools/browser/02b8105b-4682-4bbe-8840-728a1e94cb71
ok
test_CT26_checkout_zipcode_empty_standard_user (TestCheckout.TestCheckout.test_CT26_checkout_zipcode_empty_standard_user) ... 
DevTools listening on ws://127.0.0.1:52638/devtools/browser/bd751db3-4360-4e4c-9ce9-2190168f03a3
ok
test_CT27_checkout_firtname_standard_user (TestCheckout.TestCheckout.test_CT27_checkout_firtname_standard_user) ... 
DevTools listening on ws://127.0.0.1:52670/devtools/browser/320b6431-d3cf-44e0-881f-ceccd09765ee
ok
test_CT28_checkout_lastname_standard_user (TestCheckout.TestCheckout.test_CT28_checkout_lastname_standard_user) ... 
DevTools listening on ws://127.0.0.1:52699/devtools/browser/4da4f3f4-0a91-40c5-867d-dc50f87602b8
ok
test_CT29_checkout_zipcode_standard_user (TestCheckout.TestCheckout.test_CT29_checkout_zipcode_standard_user) ... 
DevTools listening on ws://127.0.0.1:52728/devtools/browser/79e2b69b-6feb-4f08-8ae8-6ee6b291a0d3
ok
test_CT30_checkout_cancel_standard_user (TestCheckout.TestCheckout.test_CT30_checkout_cancel_standard_user) ... 
DevTools listening on ws://127.0.0.1:52757/devtools/browser/51255d0c-28ff-4247-ae6d-db94809dae9b
ok
test_CT31_checkout_finish_standard_user (TestCheckout.TestCheckout.test_CT31_checkout_finish_standard_user) ... 
DevTools listening on ws://127.0.0.1:52787/devtools/browser/24836637-7bdb-4282-975b-bffa9f5a48d3
ok
test_CT01_standard_user_login (TestLoginPage.TestLoginPage.test_CT01_standard_user_login) ... 
DevTools listening on ws://127.0.0.1:52816/devtools/browser/0337673d-6c9e-40cc-8d36-19ad486eb242
ok
test_CT02_locked_out_user_login (TestLoginPage.TestLoginPage.test_CT02_locked_out_user_login) ... 
DevTools listening on ws://127.0.0.1:52845/devtools/browser/439d9df4-0402-437e-b64b-341597836b02
ok
test_CT03_empty_login (TestLoginPage.TestLoginPage.test_CT03_empty_login) ... 
DevTools listening on ws://127.0.0.1:52875/devtools/browser/559bb5a9-0f15-4f91-8f1d-ab0087191e36
ok
test_CT04_problem_user_Login (TestLoginPage.TestLoginPage.test_CT04_problem_user_Login) ... 
DevTools listening on ws://127.0.0.1:52908/devtools/browser/576fbf6b-bb0b-4421-8d3e-a3dc50792cd3
ok
test_CT05_performance_glitch_user_login (TestLoginPage.TestLoginPage.test_CT05_performance_glitch_user_login) ... 
DevTools listening on ws://127.0.0.1:52937/devtools/browser/d8ce2d31-4d2f-43e5-b4ff-d5732250ef8b
ok
test_CT06_error_user_login (TestLoginPage.TestLoginPage.test_CT06_error_user_login) ... 
DevTools listening on ws://127.0.0.1:52966/devtools/browser/4f39ad73-c991-412d-9a4a-715906adbec4
ok
test_CT07_visual_user_login (TestLoginPage.TestLoginPage.test_CT07_visual_user_login) ... 
DevTools listening on ws://127.0.0.1:52995/devtools/browser/876dbec7-59da-4515-a650-1289b2ddb092
ok
test_CT11_logout (TestLogout.TestLogout.test_CT11_logout) ... 
DevTools listening on ws://127.0.0.1:53024/devtools/browser/521bdcf0-a957-4054-ad40-8b1567c455f8
ok
test_CT08_default_password (TestPassword.TestPassword.test_CT08_default_password) ... 
DevTools listening on ws://127.0.0.1:53053/devtools/browser/9f3cabe9-33f2-4e5d-9998-bf4521a26d6f
ok
test_CT09_empty_password (TestPassword.TestPassword.test_CT09_empty_password) ... 
DevTools listening on ws://127.0.0.1:53082/devtools/browser/db03c40a-38e1-4c2e-9f62-05bd2eda47b3
ok
test_CT10_invalid_password (TestPassword.TestPassword.test_CT10_invalid_password) ... 
DevTools listening on ws://127.0.0.1:53111/devtools/browser/a7f4d3e6-6381-4723-b126-c14ec8e66057
ok
test_CT12_Sort_Z_to_A (TestSort.TestSort.test_CT12_Sort_Z_to_A) ... 
DevTools listening on ws://127.0.0.1:53141/devtools/browser/65184a75-3965-4f13-9bc3-3ba7e180d6de
ok
test_CT13_Sort_A_to_Z (TestSort.TestSort.test_CT13_Sort_A_to_Z) ... 
DevTools listening on ws://127.0.0.1:53171/devtools/browser/8fb1aabb-bbdc-43e6-b6a5-9752ecb3efcc
ok
test_CT14_sort_price_low_to_high (TestSort.TestSort.test_CT14_sort_price_low_to_high) ... 
DevTools listening on ws://127.0.0.1:53200/devtools/browser/feef2368-b3bf-435e-95cc-5d901c8f0b62
ok
test_CT15_sort_price_high_to_low (TestSort.TestSort.test_CT15_sort_price_high_to_low) ... 
DevTools listening on ws://127.0.0.1:53230/devtools/browser/dfac89bc-d1f2-4255-a025-5c913b4cec71
ok

----------------------------------------------------------------------
Ran 31 tests in 481.330s

OK