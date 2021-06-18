from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from crum import get_current_user
User = get_user_model()


class Post(models.Model):
    title_post = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Post_image')
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title_post
    
    def save(self, *args, **kwargs): 
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        
        super(Post, self).save(*args, **kwargs)



class Comment(models.Model):
    text = models.CharField(max_length=240)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    def save(self,*args,**kwargs):   #if we donot do this integrity errors comes
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        #print(user)
        super(Comment,self).save(*args,**kwargs)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    liked_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post.id)

    def save(self,*args,**kwargs):   #if we donot do this integrity errors comes
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        #print(user)
        super(Like,self).save(*args,**kwargs)




class Follow(models.Model):
    user = models.ForeignKey(User, related_name='follow_follower', on_delete=models.CASCADE, editable=False)
    followed = models.ForeignKey(User, related_name='follow_followed', on_delete=models.CASCADE)
    followed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user} --> {self.followed}"

    def save(self,*args,**kwargs):   #if we donot do this integrity errors comes
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        #print(user)
        super(Follow,self).save(*args,**kwargs)





class SavedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    saved_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post.pk)
    
    def save(self,*args,**kwargs):   #if we donot do this integrity errors comes
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        #print(user)
        super(SavedPost,self).save(*args,**kwargs)
