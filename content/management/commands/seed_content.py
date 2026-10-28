from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from content.models import (
    HeroBanner, Program, CelebrityVideo, Transformation, Coach, MembershipTier, FAQItem, ShopProduct
)

class Command(BaseCommand):
    help = "Seed database with all initial content from SWEAT HQ website HTML templates"

    def handle(self, *args, **options):
        self.stdout.write("Seeding SWEAT HQ initial data...")

        # 1. Ensure Superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@sweathq.in', 'Admin@1234')
            self.stdout.write(self.style.SUCCESS("Created admin user (admin / Admin@1234)"))

        # 2. All 17 Hero Banners
        heroes_data = [
            {
                'page_identifier': 'home',
                'eyebrow': "SWEAT HQ · Andheri · Entry by assessment",
                'headline': "WHERE THE STARS TRAIN. NOW IT'S YOU.",
                'highlight_text': "NOW IT'S YOU.",
                'subheading': "The coaches and team behind Bollywood's best-known bodies are now coaching Andheri. Stronger, leaner and surer of yourself, with the same system the stars trust.",
                'cta_primary_text': "Experience SWEAT",
                'cta_primary_link': "/book",
                'cta_secondary_text': "Fitness assessment",
                'cta_secondary_link': "/assessment",
            },
            {
                'page_identifier': 'bootcamp',
                'eyebrow': "SWEAT Bootcamp · Olympic Lifting & MetCon",
                'headline': "BOOTCAMP.",
                'highlight_text': "BOOTCAMP.",
                'subheading': "Walk in tired of starting over. Walk out stronger, leaner and certain you are finally getting somewhere. Olympic lifting, gymnastics and conditioning under one standard.",
                'cta_primary_text': "Experience SWEAT",
                'cta_primary_link': "/book",
                'cta_secondary_text': "Fitness assessment",
                'cta_secondary_link': "/assessment",
            },
            {
                'page_identifier': 'pilates',
                'eyebrow': "SWEAT Reformer Pilates · Precision Movement",
                'headline': "PILATES.",
                'highlight_text': "PILATES.",
                'subheading': "Start the fitness journey you keep postponing. Move without fear, stand taller and feel at home in your body again with athletic reformer Pilates.",
                'cta_primary_text': "Experience SWEAT",
                'cta_primary_link': "/book",
                'cta_secondary_text': "Fitness assessment",
                'cta_secondary_link': "/assessment",
            },
            {
                'page_identifier': 'glutes',
                'eyebrow': "SWEAT Glutes & Abs · Shape & Core Power",
                'headline': "GLUTES & ABS.",
                'highlight_text': "GLUTES & ABS.",
                'subheading': "Build the shape strength gives you. High-tension posterior chain work combined with deep abdominal bracing and dynamic metabolic conditioning.",
                'cta_primary_text': "Experience SWEAT",
                'cta_primary_link': "/book",
                'cta_secondary_text': "Fitness assessment",
                'cta_secondary_link': "/assessment",
            },
            {
                'page_identifier': 'coaching',
                'eyebrow': "SWEAT 1:1 Coaching · Bespoke Standard",
                'headline': "ONE-ON-ONE.",
                'highlight_text': "ONE-ON-ONE.",
                'subheading': "Your goal. Your coach. Your timeline. Complete undivided attention on the floor with the exact personal coaching system used on Bollywood's elite.",
                'cta_primary_text': "Experience 1:1 Coaching",
                'cta_primary_link': "/book",
                'cta_secondary_text': "Book Assessment",
                'cta_secondary_link': "/assessment",
            },
            {
                'page_identifier': 'assessment',
                'eyebrow': "The SWEAT Assessment · Movement & Strength",
                'headline': "ASSESSMENT.",
                'highlight_text': "ASSESSMENT.",
                'subheading': "Know exactly where you stand. Our 4-lens biometric screening places you into the right program level and sets your personalized milestone roadmap.",
                'cta_primary_text': "Book Your Assessment",
                'cta_primary_link': "/book",
                'cta_secondary_text': "Experience SWEAT",
                'cta_secondary_link': "/book",
            },
            {
                'page_identifier': 'programs',
                'eyebrow': "The Curriculum · Seven Ways In",
                'headline': "SEVEN WAYS IN. ONE OUTCOME.",
                'highlight_text': "ONE OUTCOME.",
                'subheading': "Every body is placed into the exact room and class level matched to their movement screening and goals. Explore our full training ecosystem.",
                'cta_primary_text': "Explore Programs",
                'cta_primary_link': "/programs",
                'cta_secondary_text': "Book Assessment",
                'cta_secondary_link': "/assessment",
            },
            {
                'page_identifier': 'membership',
                'eyebrow': "SWEAT Membership · Transparent Tiers",
                'headline': "TWO WAYS IN.",
                'highlight_text': "TWO WAYS IN.",
                'subheading': "Feel the studio first, or find your starting point first. Either way you choose the slot, we confirm on WhatsApp, and your membership matches what you want.",
                'cta_primary_text': "Experience SWEAT",
                'cta_primary_link': "/book",
                'cta_secondary_text': "Book Assessment",
                'cta_secondary_link': "/assessment",
            },
            {
                'page_identifier': 'nutrition',
                'eyebrow': "SWEAT Nutrition · Fuel Your Transformation",
                'headline': "NUTRITION.",
                'highlight_text': "NUTRITION.",
                'subheading': "Eat for the result you want. Zero crash diets. Plans calculated to your metabolic burn and logged weekly in the companion SWEAT app.",
                'cta_primary_text': "Book Nutrition Consult",
                'cta_primary_link': "/book",
                'cta_secondary_text': "Fitness Assessment",
                'cta_secondary_link': "/assessment",
            },
            {
                'page_identifier': 'recovery',
                'eyebrow': "SWEAT Recovery · Athletic Restoration",
                'headline': "RECOVERY.",
                'highlight_text': "RECOVERY.",
                'subheading': "Train hard. Recover faster. In-house physiotherapy, contrast therapy cold plunge, and targeted myofascial release under one suite.",
                'cta_primary_text': "Experience Recovery Suite",
                'cta_primary_link': "/book",
                'cta_secondary_text': "Book Assessment",
                'cta_secondary_link': "/assessment",
            },
            {
                'page_identifier': 'online',
                'eyebrow': "SWEAT Online · Global Remote System",
                'headline': "ONLINE.",
                'highlight_text': "ONLINE.",
                'subheading': "Your coach, wherever you are. The exact SWEAT training standard and periodization, delivered remotely with video form review.",
                'cta_primary_text': "Start Online Coaching",
                'cta_primary_link': "/book",
                'cta_secondary_text': "Virtual Assessment",
                'cta_secondary_link': "/assessment",
            },
            {
                'page_identifier': 'elite',
                'eyebrow': "SWEAT Elite · All-Inclusive VIP",
                'headline': "SWEAT ELITE.",
                'highlight_text': "SWEAT ELITE.",
                'subheading': "Everything handled. Bootcamp, reformer Pilates, personal coaching, recovery suite, and sports nutrition under one bespoke tier.",
                'cta_primary_text': "Apply For Elite",
                'cta_primary_link': "/book",
                'cta_secondary_text': "Book Assessment",
                'cta_secondary_link': "/assessment",
            },
            {
                'page_identifier': 'team',
                'eyebrow': "The Coaches & Founders · One Standard",
                'headline': "THE TEAM.",
                'highlight_text': "THE TEAM.",
                'subheading': "Specialists in strength training, precision movement, nutrition, recovery and athletic periodization. The people on the floor with you.",
                'cta_primary_text': "Meet The Coaches",
                'cta_primary_link': "/team",
                'cta_secondary_text': "Book Assessment",
                'cta_secondary_link': "/assessment",
            },
            {
                'page_identifier': 'shop',
                'eyebrow': "SWEAT Official Store · Gear & Apparel",
                'headline': "SWEAT SHOP.",
                'highlight_text': "SWEAT SHOP.",
                'subheading': "Designed for high-intensity training. Official SWEAT performance apparel, lifting straps, accessories and performance fuel.",
                'cta_primary_text': "Browse Collection",
                'cta_primary_link': "/shop",
                'cta_secondary_text': "Visit Studio",
                'cta_secondary_link': "/visit",
            },
            {
                'page_identifier': 'visit',
                'eyebrow': "SWEAT HQ Andheri · Location & Studio Tour",
                'headline': "VISIT ANDHERI.",
                'highlight_text': "VISIT ANDHERI.",
                'subheading': "Experience the floor in person. 12,000 sq ft of Olympic rigs, 8-bed reformer studio, recovery plunge and dedicated consultation suites.",
                'cta_primary_text': "Book Studio Tour",
                'cta_primary_link': "/book",
                'cta_secondary_text': "Get Directions",
                'cta_secondary_link': "/visit",
            },
            {
                'page_identifier': 'app',
                'eyebrow': "SWEAT Digital Companion · iOS & Android",
                'headline': "THE SWEAT APP.",
                'highlight_text': "THE APP.",
                'subheading': "Book your floor slots, log workouts, track nutrition macros and review biometric reassessments from your phone.",
                'cta_primary_text': "Download App",
                'cta_primary_link': "/app",
                'cta_secondary_text': "Experience SWEAT",
                'cta_secondary_link': "/book",
            },
            {
                'page_identifier': 'book',
                'eyebrow': "SWEAT HQ · Reserve Your Session",
                'headline': "EXPERIENCE SWEAT.",
                'highlight_text': "RESERVE NOW.",
                'subheading': "Choose your preferred discipline and slot. Our team confirms immediately via WhatsApp with zero sales pressure.",
                'cta_primary_text': "Reserve Session",
                'cta_primary_link': "/book",
                'cta_secondary_text': "Book Assessment",
                'cta_secondary_link': "/assessment",
            },
        ]
        for h in heroes_data:
            HeroBanner.objects.update_or_create(
                page_identifier=h['page_identifier'],
                defaults={**h, 'is_active': True}
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(heroes_data)} Hero Banners"))

        # 3. Programs (7 Programs)
        programs_data = [
            {
                'number': '01',
                'name': 'BOOTCAMP',
                'slug': 'bootcamp',
                'tagline': 'Get stronger, leaner and sure of yourself.',
                'description': 'Olympic lifting, gymnastics and conditioning in four classes, from Foundation to DTP.',
                'level_tags': ['Olympic Lifting', 'Gymnastics', 'DTP', 'MetCon'],
                'class_ratio': '2 coaches on the floor · capped at 16',
                'duration': '55 Mins',
                'order': 1
            },
            {
                'number': '02',
                'name': 'PILATES',
                'slug': 'pilates',
                'tagline': 'Start your fitness journey. Feel good in your body again.',
                'description': 'Athletic Pilates on the reformer in four levels, Rehab to Athletic.',
                'level_tags': ['Rehab', 'Stretch', 'Athletic Reformer', 'Core Flow'],
                'class_ratio': '1 coach per 8 reformers · precision cueing',
                'duration': '50 Mins',
                'order': 2
            },
            {
                'number': '03',
                'name': 'GLUTES & ABS',
                'slug': 'glutes',
                'tagline': 'Build the shape strength gives you.',
                'description': 'A circuit class for glutes, legs and core, with conditioning built in.',
                'level_tags': ['Hip Thrusts', 'Posterior Chain', 'Abs Circuit'],
                'class_ratio': '2 coaches on the floor · capped at 16',
                'duration': '50 Mins',
                'order': 3
            },
            {
                'number': '04',
                'name': 'ONE-ON-ONE',
                'slug': 'coaching',
                'tagline': 'Your goal, your coach, your timeline.',
                'description': 'Personal coaching built around one person with undivided attention.',
                'level_tags': ['Bespoke Program', '1-on-1 Floor Ratio', 'Direct Accountability'],
                'class_ratio': '1-on-1 private coaching',
                'duration': '60 Mins',
                'order': 4
            },
            {
                'number': '05',
                'name': 'ASSESSMENT',
                'slug': 'assessment',
                'tagline': 'Know exactly where you stand.',
                'description': 'The biometric sitting that places you and sets your customized roadmap.',
                'level_tags': ['Mobility Screening', 'Cardio V02', 'Strength Diagnostics'],
                'class_ratio': '1-on-1 diagnostic evaluation',
                'duration': '45 Mins',
                'order': 5
            },
            {
                'number': '06',
                'name': 'NUTRITION',
                'slug': 'nutrition',
                'tagline': 'Eat for the result you want.',
                'description': 'One-to-one consultations and a macro plan tracked in the app.',
                'level_tags': ['Macro Coaching', 'Meal Planning', 'App Tracking'],
                'class_ratio': '1-on-1 sports nutritionist',
                'duration': '45 Mins',
                'order': 6
            },
            {
                'number': '07',
                'name': 'ONLINE',
                'slug': 'online',
                'tagline': 'Your coach, wherever you are.',
                'description': 'Coaching and the SWEAT system, delivered remotely worldwide.',
                'level_tags': ['Remote Coaching', 'Form Review', 'Global Community'],
                'class_ratio': 'Dedicated remote coach',
                'duration': 'Ongoing',
                'order': 7
            },
        ]
        for p in programs_data:
            Program.objects.update_or_create(slug=p['slug'], defaults={**p, 'is_active': True})
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(programs_data)} Programs"))

        # 4. Celebrity Videos
        celebs = [
            {'star_name': 'Shraddha Kapoor', 'display_order': 1, 'duration_label': '30 to 60s · vertical', 'quote': 'SWEAT gave me the conditioning and athletic strength I needed for demanding multi-week shoot schedules.'},
            {'star_name': 'Abhishek Bachchan', 'display_order': 2, 'duration_label': '30 to 60s · vertical', 'quote': 'Praveen and the SWEAT team run a world-class room. It is disciplined, structured and delivers.'},
            {'star_name': 'Kartik Aaryan', 'display_order': 3, 'duration_label': '30 to 60s · vertical', 'quote': 'High energy, intense accountability and coaches who push your limits every single workout.'},
            {'star_name': 'Aditya Roy Kapur', 'display_order': 4, 'duration_label': '30 to 60s · vertical', 'quote': 'Real strength, honest coaching. SWEAT transforms how you move and feel.'},
            {'star_name': 'Sushant Singh Rajput', 'display_order': 5, 'duration_label': '30 to 60s · vertical', 'quote': 'Discipline on the floor translates to discipline everywhere in life.'},
        ]
        for c in celebs:
            CelebrityVideo.objects.update_or_create(star_name=c['star_name'], defaults={**c, 'is_active': True})
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(celebs)} Celebrity Reels"))

        # 5. Coaches & Team
        coaches_data = [
            {
                'name': 'Praveen Nair',
                'role_title': 'Co-Founder & Head of Training',
                'celebrities_trained': 'Shraddha Kapoor · Aditya Roy Kapur · Sushant Singh Rajput',
                'specialties': ['Olympic Weightlifting', 'Athletic Conditioning', 'Elite Periodization'],
                'bio': 'Pioneer of functional strength and athletic conditioning in Bollywood for over 15 years.',
                'display_order': 1
            },
            {
                'name': 'Farhan Malik',
                'role_title': 'Senior Floor Coach · DTP Lead',
                'celebrities_trained': 'Bollywood & National Athletes',
                'specialties': ['DTP Metabolic Conditioning', 'Barbell Mechanics', 'Kinetic Force'],
                'bio': 'Specializes in high-intensity metabolic conditioning and progressive resistance lifting.',
                'display_order': 2
            },
            {
                'name': 'Maya Sen',
                'role_title': 'Lead Reformer Pilates Specialist',
                'celebrities_trained': 'Leading Actors & Posture Athletes',
                'specialties': ['Rehab Pilates', 'Athletic Reformer', 'Spinal Decompression'],
                'bio': 'Master instructor specializing in posture alignment, injury rehabilitation, and athletic core stability.',
                'display_order': 3
            },
            {
                'name': 'Rohan Varma',
                'role_title': 'Strength & Movement Coach',
                'celebrities_trained': 'Competitive Powerlifters & Executives',
                'specialties': ['Functional Mobility', 'Kettlebell Mechanics', 'Posterior Chain'],
                'bio': 'Focuses on building durable bodies through multi-planar loading and biomechanical longevity.',
                'display_order': 4
            },
        ]
        for coach in coaches_data:
            Coach.objects.update_or_create(name=coach['name'], defaults={**coach, 'is_active': True})
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(coaches_data)} Coaches"))

        # 6. Transformations
        transformations_data = [
            {
                'member_name': 'Kabir S.',
                'metric_label': '-8.4 kg fat · +3.2 kg muscle',
                'timeline_weeks': 12,
                'display_order': 1,
            },
            {
                'member_name': 'Rhea M.',
                'metric_label': '-11.2 kg fat · +2.8 kg muscle',
                'timeline_weeks': 16,
                'display_order': 2,
            },
            {
                'member_name': 'Aarav P.',
                'metric_label': '+4.5 kg muscle · Posture Realigned',
                'timeline_weeks': 12,
                'display_order': 3,
            },
            {
                'member_name': 'Ananya D.',
                'metric_label': '-6.8 kg fat · -4 inches waist',
                'timeline_weeks': 10,
                'display_order': 4,
            },
        ]
        for t in transformations_data:
            Transformation.objects.update_or_create(member_name=t['member_name'], defaults={**t, 'is_active': True})
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(transformations_data)} Transformations"))

        # 7. Memberships
        tiers = [
            {
                'tier_name': 'BOOTCAMP UNLIMITED',
                'slug': 'bootcamp-unlimited',
                'price_display': '₹16,500 / month',
                'billing_period': 'Monthly',
                'features_list': ['Unlimited Bootcamp floors', '2 coaches on the floor', '15-day reassessments', 'SWEAT App full access'],
                'order': 1
            },
            {
                'tier_name': 'PILATES REFORMER',
                'slug': 'pilates-reformer',
                'price_display': '₹21,000 / month',
                'billing_period': 'Monthly',
                'features_list': ['Capped 8 reformers studio', 'Levels 1 to 4 progression', 'Posture diagnostics', 'Nutrition consultation'],
                'order': 2
            },
            {
                'tier_name': 'SWEAT ELITE',
                'slug': 'sweat-elite',
                'price_display': '₹38,000 / month',
                'billing_period': 'Monthly',
                'features_list': ['All Bootcamp & Reformer Pilates', 'Recovery Suite & Cold Plunge', 'Dedicated Head Coach', 'Priority slot bookings'],
                'is_highlighted': True,
                'order': 3
            },
        ]
        for t in tiers:
            MembershipTier.objects.update_or_create(slug=t['slug'], defaults=t)
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(tiers)} Membership Tiers"))

        # 8. FAQs
        faqs_data = [
            {
                'question': "How does entry by assessment work?",
                'answer': "Before any membership is confirmed, our head coaches conduct a comprehensive 45-minute assessment analyzing your movement mechanics, strength baseline, endurance and body composition.",
                'page_category': 'home',
                'order': 1
            },
            {
                'question': "Can I do both Bootcamp and Pilates?",
                'answer': "Yes. Our Sweat Elite membership and hybrid passes grant full unrestricted access to both our high-intensity bootcamp rig floor and the 8-bed reformer studio.",
                'page_category': 'home',
                'order': 2
            },
            {
                'question': "What is the coach-to-member ratio on the floor?",
                'answer': "We maintain a strict maximum ratio of 1 coach for every 8 members on the floor, and 2 coaches lead every peak-hour class so nobody trains unseen.",
                'page_category': 'home',
                'order': 3
            },
            {
                'question': "Are the classes beginner friendly?",
                'answer': "Every program features level-graded classes. Bootcamp begins at Foundation level, and Pilates offers gentle Rehab & Stretch levels.",
                'page_category': 'home',
                'order': 4
            },
            {
                'question': "Is the SWEAT mobile app free for members?",
                'answer': "All active members receive full unlocked access to the SWEAT app including workout logging, 15-day check-in logs, nutrition guidance, and slot reservations.",
                'page_category': 'app',
                'order': 1
            },
            {
                'question': "Can I use the app without an in-person club membership?",
                'answer': "Yes, our Online & Digital passes allow global athletes to access remote programming, video libraries, and coach check-ins from anywhere in the world.",
                'page_category': 'app',
                'order': 2
            },
            {
                'question': "How do reassessments work inside the app?",
                'answer': "Every 15 days, your assigned head coach logs biometric progress, strength indexes, and movement improvements directly into your private app roadmap.",
                'page_category': 'app',
                'order': 3
            },
        ]
        for f in faqs_data:
            FAQItem.objects.update_or_create(question=f['question'], defaults=f)
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(faqs_data)} FAQs"))

        # 9. Shop Products
        products_data = [
            {
                'name': 'SWEAT Heavyweight Boxy Tee',
                'category': 'APPAREL',
                'price': '₹2,400',
                'description': '280 GSM combed cotton oversized boxy silhouette engineered for gym and street.',
                'order': 1,
                'is_available': True
            },
            {
                'name': 'SWEAT Pro Lifting Straps',
                'category': 'GEAR',
                'price': '₹1,200',
                'description': 'Heavy-duty cotton webbing with neoprene wrist padding for heavy pull days.',
                'order': 2,
                'is_available': True
            },
            {
                'name': '100% Grass-Fed Whey Isolate',
                'category': 'SUPPLEMENTS',
                'price': '₹4,200',
                'description': 'Ultra-filtered cold-pressed isolate, 27g protein per scoop, zero fillers.',
                'order': 3,
                'is_available': True
            },
            {
                'name': 'SWEAT Stainless Steel Shaker (750ml)',
                'category': 'LIFESTYLE',
                'price': '₹1,499',
                'description': 'Double-wall insulated matte black shaker bottle keeps liquids chilled 24 hours.',
                'order': 4,
                'is_available': True
            },
            {
                'name': 'Electrolyte & Hydration Matrix',
                'category': 'SUPPLEMENTS',
                'price': '₹1,800',
                'description': 'Bio-available sodium, potassium and magnesium for intense MetCon recovery.',
                'order': 5,
                'is_available': True
            },
            {
                'name': 'SWEAT Comp Training Shorts',
                'category': 'APPAREL',
                'price': '₹2,800',
                'description': '4-way stretch ripstop fabric with compression liner and zip pocket.',
                'order': 6,
                'is_available': True
            },
        ]
        for p in products_data:
            ShopProduct.objects.update_or_create(name=p['name'], defaults=p)
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(products_data)} Shop Products"))

        self.stdout.write(self.style.SUCCESS("All SWEAT HQ dynamic data seeded successfully!"))