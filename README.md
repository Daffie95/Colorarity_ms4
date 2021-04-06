
# Colorarity

Colorarity is a companypage that acts as a wholesale for paint. With fast worldwide shipping and a high variety of colors in spray cans and buckets. This is a project that acts like the Milestone project 4, which is the 
last project in the full stack course hosted by Code Institute. This project focuses on using full stack frameworks, and in this case I will be using Django.


### Index
1. Project Planning.
2. Updates Timeline.
3. Planned Updates.
4. Bugs & Errors.
5. Additional Comments.
6. External Resources.
7. Testing.
8. Deployment.
9. Conclusion.


## 1. Project Planning.
I have created a wireframe of a model I would like to create. Its intuitive for the user and the focus is on the products we sell. What I want to do differently from the Boutique Ado project where there is eyecatching designs to promote user interactions, I would like to focus on the products colors(which they are) to try and make them look good and eye-catching.<br>
There is no way bombarding the page with fancy colors and flashy designs when the product I'd sell is actual colors. And there is a need for the products to be seen clearly and not polluted by background colors and/or things that might disturb the view.<br>
While at the same time I want the page to be interesting and not look like a Windows98 interface, I think this is a case of spartan designs and a easy-on-the-eyes color palette. 

>> User Goals:
The user goals are quite self explanitary, a potential customer lands on the page looking for color, perhaps they are painting a fence, a baby chamber, or just like graffiti, who am I to judge. The user will be able to use a search function to find different colors. searching for "red", would bring up all colors with the word red in it (e.g "Sunset Red", "Coca Cola Red", "Tomato Red"). And the same for any other color. 

>> Owner Goals:
The goal for me as the company/page owner, would be to offer a reliable customer service where I sell paint to paying customers, sorting payments and shipping. To create the easiest and most trustworthy experience for the customer.

>> User stories:
## 2. Updates Timeline.
> **2021-04-04**
>> Installed Django <br>
>> Installed AllAuth  <br>
>> Configured AllAuth BACKEND's <br>
>> Set up Superuser<br>
>> created requirements.txt<br>
>> created templates using AllAuth templates<br>
>> created base.html<br>
>> configured nav in base.html<br>
>> created static and media folders<br>
>> created basic CSS for text, buttons, and media querys<br>

> **2021-04-05**<br>
>> created /Includes for easy access and editing html code<br>
>> created navigation in /Includes for mobile and larger screens<br>
>> included navigation in base.html<br>
>> set up CSS and background image<br>
>> created a banner on homepage for shipping threshold<br>
>> updated homepage text<br>
>> Created fixtures for products and categories<br>
>> tested database functionality<br>
>> created products page<br>
>> created detailed products page<br>
>> created products layout on products.html template<br>
>> created search function<br>
>> created shopping bag function and view<br>
>> created and configured <br>
>> removed text tecoration on homepage button<br>
>> formatted README<br>
>> created increment/decrement buttons for quantity selection on products<br>
>> configured incr/decr buttons for quantity on products using JS<br>
>> up to version after GitPod Crash<br>
>> created remove function to shopping bag<br>
>> configured remove function to shopping bag<br>



> **2021-04-06**
>> configured toasts messages on success, update, and remove items from shopping bag.<br>
>> created toasts<br>
>> configured toasts <br>
>> styled toasts using CSS-trix <br>
>> configured checkout forms<br>
>> configured checkouts signals.py<br>
>> configured checkouts models.py<br>
>> configured checkouts views.py<br>
>> configured checkouts urls.py<br>
>> installed crispy_forms<br>
>> updated requirements.txt<br>
>> configured builtins to templates<br>
>> created checkout css<br>
>> created checkout JS<br>
>> created stripe_elements.JS for stripe visibility<br>
>> added stripe keys to context<br>
>> added bag_contents to bag contexts<br>
>> configured stripe keys<br>
>> configured submit handler<br>



## 3. Planned Updates.
|  Update | Finished |
|---|---|
| Templates  |  |
|  Auth  |   |
|  Products |  Yes |
| Cart  |  Yes |
| User feedback  | Yes(Toasts) | 
| Checkout  |   |
| User Profile  |   |
| Admin  |   |
|  Design and color |   |
|  user stories |   |
|  searching |  Yes  |
|   |   |
|   |   |
## 4. Bugs & Errors.
> ~~While working on creating the navigation, I could not get my current bootstrap/JS to actually display the dropdown menu on the page, the link worked but no dropdown would show.
I went trough Slack and found similar issues that all reverted back to the source code for the Boutique Ado project.~~ I went and tried the same thing and changing the JS script CDNs 
made it work. 
<br>
<br>
> ~~The Products does render the correct template but the injected content is not displayed on screen.~~<br>
a break in the logo caused layering issues.

## 5. Additional Comments.
> having to end working early (21-04-04) due to scheduled power outage in my appartment complex. <br> <br>

> **if forloop.counter|divisibleby:X** <br>
> While this DID take me a good while to figure out, its an amazing feature used in the Boutique Ado project.
What this does is that there are X numbers of products displayed one each row(which changes on different screen sizes)
the HR is displayed.<br>

> **quant_input_script** <br>
>>I tried figuring out this on my own but couldnt make it work reliably and again reverted back to the source code of the Boutique Ado project,
I struggled with this for a while but finally made it work after researching both the videos and source code extensively.

> **GitPod Error**
>> GitPod decided to throw me out and currently im trying to patch things back up. 
>> After throwing me out extentions like Prettier and visual enhancements are not working making it incredibly hard to read anything.

> **remove_from_bag function**
>> I struggled a lot with trying to recover after GitPod crashing on me and couldnt actually make
>> this work, I headed over to the source code for the Boutique Ado project, but I will be honest and say that I 
>> am not 100% sure how this view works, as I am not using sizes in my projects there wont be any conflicts in the actual
>> funtion as it will always fire the bag.pop instead of finding a size attribute. 
>> but it is not the way I would have wanted to work it out.

> **Stripe AUTH error**
>> ~~I was having problems with authorizing stripe using my secret keys, I tried using the GitPod Env Variables but couldnt get it to work.~~<br> I changed 
>> the targeted Repos and made sure correct capitalization was used.

## 6. External Resources.
> Django allAuth<br>
> Pillow<br>
> crispy_forms
> bootstrap<br>
> Google Fonts<BR>
> Font awesome<br>
> CSS-trix (base.css line 145)<br>
> Boutique Ado Mini-project Soruce Code<br>
>>A lot of code used in this project is revamped code from the previous Boutique Ado project, because I feel like there is not really a better way to implement the same code, but in a different way.
>> The Boutique Ado project suffers greatly from the lack of explanitary measures of WHY and HOW functions work the way they do, knowing what does this and that is great, but the learning outcomes are very slim
>> and without extensively going trough Django documentation, there really isnt a whole lot to take away from it. <br>
>> 


## 7. Testing.
## 8. Deployment.
## 9. Conclusions.
