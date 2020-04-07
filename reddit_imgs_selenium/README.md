# reddit-images-selenium
Extracts images from Reddit given list of posts (Selenium, not API).
1) links_from_posts.py: given a list of Reddit posts, extracts image and miscellaneous urls, and downloads images;
2) removed_posts_handler.py: from miscellaneous urls, removes that those belong to deleted posts (if you will so need to check those - videos, gifs, etc. - manually);
3) repair_order.py: repairs filenames (bringing them to order 1, 2, ..., preserving multi-part imgs like  1.1, 1.2, 1.3, ...)
