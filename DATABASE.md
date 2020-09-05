# Video Membership Project

User

## Content via Vimeo

Video
    - vimeo_id

BlogPost
    - title
    - ....

Content
    - content: video / ... / podcast
    - data: 
        {vimeo_video_id: 4363464574}
        blogpost: {title, ..., image}
    - pricing(FK or ManyToMany)

## Subscription via Stripe

Pricing
    - price per month
    - currency
    - id
    - name (basic / pro / ...)

Subscriptiom
    - user(FK)
    - stripe_subscription_id
    - status (active / canceled / past_due / trialing)
    - pricing(FK)