# Quick Start Guide - Kun.uz News Portal

Follow these steps to get your news portal up and running in minutes.

## Step 1: Set Up Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Run Database Migrations

```bash
cd project1
python manage.py migrate
```

## Step 4: Create Admin Account

```bash
python manage.py createsuperuser
```

When prompted:
- **Username:** admin (or your preferred username)
- **Email:** admin@example.com (or your email)
- **Password:** Choose a strong password
- **Confirm password:** Re-enter the password

## Step 5: Populate Sample Data (Optional)

```bash
python manage.py populate_sample_data
```

This creates sample categories and posts so you can see how the site looks with content.

## Step 6: Start Development Server

```bash
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Step 7: Access the Application

Open your browser and visit:

- **Homepage:** http://localhost:8000/
- **Admin Panel:** http://localhost:8000/admin/

Log in with your superuser credentials from Step 4.

## Creating Your First Post

1. Go to http://localhost:8000/admin/
2. Log in with your credentials
3. Click on **Categories** and add your first category (e.g., "News", "Technology")
4. Click on **Posts** and click "Add Post"
5. Fill in the form:
   - **Title:** Your article title
   - **Slug:** Auto-filled based on title (you can edit it)
   - **Category:** Select the category you created
   - **Featured Image:** Upload an image (required)
   - **Body:** Write your article content
   - **Is featured:** Check this box to show it in the featured section
6. Click "Save"

Your post will immediately appear on the homepage!

## Key URLs

| URL | Purpose |
|-----|---------|
| `/` | Homepage with all posts |
| `/admin/` | Django admin panel |
| `/post/<slug>/` | Individual post page |
| `/?category=<slug>` | Posts filtered by category |

## Tips & Tricks

### Change Site Header
Edit the navigation in `project1/templates/project2/base.html` to customize:
- Site name/logo
- Navigation links
- Color scheme (look for `text-red-600`, `bg-red-600`)

### Customize Colors
All colors are Tailwind CSS classes. To change the primary color:
1. Open `base.html`, `index.html`, or `detail.html`
2. Find `text-red-600` or `bg-red-600`
3. Replace with your preferred Tailwind color (e.g., `blue-600`, `green-600`)

### Upload Default Images
1. Create a `media/` folder in the `project1` directory if it doesn't exist
2. Add default images
3. Reference them in posts by uploading via the admin

### Add More Categories
Simply go to the admin panel and add categories. They'll automatically appear in:
- The sidebar on the homepage
- The category dropdown in the header
- The footer

## Troubleshooting

### Port Already in Use
If port 8000 is in use, run:
```bash
python manage.py runserver 8001
```

### No Photos Displaying
Ensure you've uploaded images through the admin panel. Images won't display if:
- The media folder doesn't exist: `mkdir media`
- Images weren't uploaded through the form (they need to be in the database record)

### Template Not Found Error
Make sure you're running the server from the correct directory:
```bash
cd project1
python manage.py runserver
```

### Database Errors
Reset your database:
```bash
python manage.py migrate
python manage.py populate_sample_data
```

**Warning:** This will delete all existing data!

## Next Steps

Once you have the site running:

1. **Customize Styling:** Edit CSS classes in the templates
2. **Add More Categories:** Create as many as you need
3. **Write More Posts:** The system supports unlimited posts
4. **Deploy:** When ready, follow the deployment guide in README.md

## Need Help?

- Check the main README.md for detailed documentation
- Review Django docs: https://docs.djangoproject.com/
- Tailwind CSS docs: https://tailwindcss.com/docs/

---

Happy publishing! 🎉
