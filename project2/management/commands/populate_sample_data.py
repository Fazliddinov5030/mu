from django.core.management.base import BaseCommand
from project2.models import Category, Post
from django.utils import timezone


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        # Create categories
        categories_data = [
            {'name': 'Technology'},
            {'name': 'Business'},
            {'name': 'Politics'},
            {'name': 'Sports'},
            {'name': 'Entertainment'},
            {'name': 'Health'},
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(name=cat_data['name'])
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {cat_data["name"]}'))
            else:
                self.stdout.write(f'Category already exists: {cat_data["name"]}')

        # Create sample posts
        posts_data = [
            {
                'title': 'Revolutionary AI Breakthrough Changes Industry',
                'category': 'Technology',
                'body': 'Artificial Intelligence continues to advance at a rapid pace. Recent developments in machine learning have opened new possibilities for automation and data analysis. Organizations worldwide are adopting AI technologies to improve efficiency and make better decisions.\n\nThe impact of these innovations extends across various sectors including healthcare, finance, manufacturing, and education. Experts predict that AI will become even more integrated into our daily lives in the coming years.\n\nHowever, with these advancements come important questions about ethics, privacy, and the future of work. Governments and companies are working together to establish guidelines and best practices for responsible AI development.',
                'is_featured': True,
            },
            {
                'title': 'Global Markets Experience Significant Growth',
                'category': 'Business',
                'body': 'Financial markets have shown strong performance following positive economic indicators. Investors are optimistic about prospects for the coming quarters. Major indices have reached new highs as companies report strong earnings.\n\nThe tech sector continues to lead gains, with several companies announcing expansion plans and new product launches. Meanwhile, traditional sectors like manufacturing and energy are also showing resilience.\n\nEconomists attribute the positive trend to stable interest rates, strong consumer spending, and business investment in technology and infrastructure. However, some analysts caution about potential risks and recommend a balanced investment approach.',
                'is_featured': True,
            },
            {
                'title': 'Historic Trade Agreement Signed',
                'category': 'Politics',
                'body': 'Government leaders have successfully negotiated a landmark trade agreement that is expected to strengthen economic ties between nations. The agreement covers several sectors including technology, agriculture, and manufacturing.\n\nOficials from both sides expressed optimism about the future cooperation and potential benefits for their economies. The deal is expected to create new opportunities for businesses and workers.\n\nParliamentary approval is expected in the coming weeks, paving the way for implementation of the agreement starting next quarter.',
                'is_featured': True,
            },
            {
                'title': 'Championship Team Wins in Thrilling Match',
                'category': 'Sports',
                'body': 'In an exciting finish, the championship team secured victory in a match that kept fans on the edge of their seats. The team displayed exceptional teamwork and determination throughout the game.\n\nKey players delivered outstanding performances, with the star player scoring the winning goal in the final minutes of the match. The crowd erupted in celebration as the final whistle blew.\n\nThe team is now preparing for the next round of competitions, with hopes of maintaining their winning streak and ultimately claiming the season title.',
                'is_featured': False,
            },
            {
                'title': 'New Movie Breaks Box Office Records',
                'category': 'Entertainment',
                'body': 'A highly anticipated movie release has shattered box office records, becoming the highest-grossing film of the year so far. Audiences have embraced the film\'s compelling storyline and impressive cinematography.\n\nCritics praised the performances of the lead actors and the director\'s vision for bringing the story to life. The film\'s success has sparked interest in potential sequels and spin-offs.\n\nThe movie is now available in theaters worldwide and is expected to continue drawing audiences in the coming weeks.',
                'is_featured': False,
            },
            {
                'title': 'Health Experts Share Tips for Wellness',
                'category': 'Health',
                'body': 'Leading health professionals have released guidelines for maintaining optimal health and wellness. The recommendations emphasize the importance of regular exercise, balanced nutrition, and adequate sleep.\n\nExperts also highlight the significance of mental health and stress management in overall well-being. Simple lifestyle changes can make a significant difference in long-term health outcomes.\n\nRegular health check-ups and preventive measures are crucial for early detection of potential health issues. The guidelines are now available to the public through health centers and online resources.',
                'is_featured': False,
            },
            {
                'title': 'Startup Secures Major Funding Round',
                'category': 'Business',
                'body': 'An innovative startup focused on sustainable technology has announced a successful funding round, securing investment from leading venture capital firms. The funds will be used to expand product development and market reach.\n\nThe company aims to revolutionize how industries approach sustainability and environmental responsibility. Their innovative solutions have attracted attention from major corporations and environmental organizations.\n\nWith this funding, the startup plans to hire top talent, establish new offices in key markets, and accelerate the development of their flagship product.',
                'is_featured': False,
            },
        ]

        for post_data in posts_data:
            category = categories[post_data['category']]
            post, created = Post.objects.get_or_create(
                title=post_data['title'],
                defaults={
                    'category': category,
                    'body': post_data['body'],
                    'is_featured': post_data.get('is_featured', False),
                    'publication_date': timezone.now(),
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created post: {post_data["title"]}'))
            else:
                self.stdout.write(f'Post already exists: {post_data["title"]}')

        self.stdout.write(self.style.SUCCESS('Sample data population complete!'))
