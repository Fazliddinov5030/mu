# Kun.uz - Django News Portal

A modern, responsive news portal built with Django and Tailwind CSS. This application provides a complete content management system for publishing news articles with categories, featured stories, and an intuitive admin interface.

## Features

✨ **Modern Design**
- Responsive layout that works on all devices
- Clean, professional UI with Tailwind CSS
- Smooth animations and transitions
- Dark mode ready infrastructure

📰 **Content Management**
- Post model with rich fields (title, slug, category, featured image, body text, publication date)
- Category system for organizing content
- Featured posts highlight system
- Automatic slug generation

🎯 **User Experience**
- Home page with featured stories section
- Responsive news grid layout
- Category sidebar for easy navigation
- Individual post detail pages
- Related posts suggestions
- Social sharing buttons
- Newsletter subscription widget
- Trending posts sidebar

🔧 **Admin Interface**
- Customized Django admin with organized fieldsets
- Easy post and category management
- Date hierarchy for posts
- Search and filtering capabilities
- Pre-populated slug fields

## Project Structure

```
project1/
├── manage.py
├── project1/                      # Django project configuration
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Main URL router
│   ├── wsgi.py
│   ├── asgi.py
│   └── templates/
│       └── project2/
│           ├── base.html         # Base template with Tailwind CSS
│           ├── index.html        # Home page template
│           └── detail.html       # Post detail page template
│
└── project2/                      # Django app for news content
    ├── models.py                 # Post and Category models
    ├── views.py                  # Home and detail views
    ├── urls.py                   # App URL routing
    ├── admin.py                  # Admin customization
    └── migrations/
```

## Installation & Setup

### 1. Create and activate a virtual environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install django pillow
```

### 3. Run migrations

```bash
cd project1
python manage.py migrate
```

### 4. Create a superuser (admin account)

```bash
python manage.py createsuperuser
# Follow the prompts to create your admin account
```

### 5. Start the development server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000/`

## Usage

### Accessing the Application

- **Homepage:** http://localhost:8000/
- **Admin Panel:** http://localhost:8000/admin/
- **Post Detail:** http://localhost:8000/post/{slug}/

### Creating Content

1. Log in to the admin panel at `http://localhost:8000/admin/`
2. Navigate to **Posts** or **Categories**
3. Create a new category if needed
4. Create a new post with:
   - Title (slug is auto-generated)
   - Category
   - Featured image
   - Body text
   - Toggle "Featured" if you want it to appear in the featured section

### Categories

The sidebar displays all categories with post counts. Click any category to filter posts.

## Template Features

### Base Template (`base.html`)
- Sticky navigation bar with category dropdown
- Mobile-friendly hamburger menu
- Footer with category links and social media
- Tailwind CSS styling with custom utilities

### Home Page (`index.html`)
- Featured stories carousel (up to 3 posts)
- Responsive news grid (auto-adjusts to screen size)
- Category sidebar with filtering
- Trending posts widget
- Newsletter subscription form

### Detail Page (`detail.html`)
- Breadcrumb navigation
- Full article content with featured image
- Article metadata (date, author, word count)
- Social sharing buttons (Facebook, Twitter, LinkedIn, WhatsApp)
- Related posts from the same category
- Comments section (ready for future implementation)

## Styling with Tailwind CSS

The project uses **Tailwind CSS via CDN**, making it easy to customize:

- **Color scheme:** Red (#FF6B6B) for primary actions and highlights
- **Typography:** Responsive font sizes and line heights
- **Spacing:** Consistent padding and margins using Tailwind's scale
- **Responsive design:** Mobile-first approach with `sm:`, `md:`, `lg:` breakpoints

To modify colors, update the style in `base.html`:
- Primary color: Change `text-red-600`, `bg-red-600` to your preferred Tailwind color
- Accent colors: Modify gradient colors in featured badges and sections

## Models

### Category
```python
- name: CharField (max_length=100)
- slug: SlugField (auto-generated from name)
```

### Post
```python
- title: CharField (max_length=200)
- slug: SlugField (auto-generated from title)
- category: ForeignKey (related to Category)
- featured_image: ImageField
- body: TextField
- publication_date: DateTimeField (auto-set on creation)
- updated_at: DateTimeField (auto-updated)
- is_featured: BooleanField (default=False)
```

## Development Notes

### Adding More Features

1. **Comments System:** Use Django's built-in comments framework or `django-comments`
2. **Search:** Add a search view and implement full-text search
3. **Tags:** Add a tags system for better categorization
4. **Social Login:** Integrate social authentication with `django-allauth`
5. **API:** Create a REST API with `django-rest-framework`

### Performance Optimization

- **Image Optimization:** Consider using `django-imagekit` for thumbnail generation
- **Caching:** Implement Django cache for frequently accessed posts
- **Pagination:** Add pagination to the home page for large post collections

### Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS` with your domain
3. Use a production database (PostgreSQL recommended)
4. Serve static and media files with a web server (Nginx/Apache)
5. Use environment variables for sensitive settings (SECRET_KEY, etc.)
6. Run `python manage.py collectstatic` before deployment

## Troubleshooting

### Images not displaying
- Ensure the media directory exists: `mkdir media`
- Check that `MEDIA_URL` and `MEDIA_ROOT` are configured in settings.py
- Verify image file permissions

### Static files not loading
- Run `python manage.py collectstatic` in production
- In development, ensure `DEBUG = True`

### Database errors
- Run migrations: `python manage.py migrate`
- Check for migration conflicts: `python manage.py showmigrations`

## Technologies Used

- **Backend:** Django 6.0.2
- **Frontend:** HTML5, Tailwind CSS 3.x (CDN)
- **Database:** SQLite (development), can be changed to PostgreSQL/MySQL
- **Image handling:** Pillow
- **Icons:** Font Awesome 6.4

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or contributions, please reach out through the admin panel contact form or social media channels.

---

Happy publishing! 🚀
