import urllib.request as req
# url = "http://uta.pw/shodou/img/28/214.png"
 url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fimagingsolution.blog.fc2.com%2Fblog-entry-180.html&psig=AOvVaw00PG3GqkblTz_EEjMNQIWy&ust=1584855886409000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOjB7bnuqugCFQAAAAAdAAAAABAD"

req.urlretrieve(url, "test.png")

import cv2
img = cv2.imread("test.png")
print(img)
