# Athena.Live

Athena.Live is a Django-powered professional networking platform inspired by LinkedIn. The platform helps professionals showcase their experience, connect with peers, share insights, chat in real time, explore job opportunities, and unlock premium features backed by analytics.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Project Layout

- `athena_live/` – Django project configuration (settings, URLs, ASGI/WGI entry points).
- `users/` – User profiles, authentication endpoints, and serializers.
- `network/` – Connection graph and recommendations.
- `posts/` – Feed, posts, comments, and likes.
- `messaging/` – Real-time chat powered by Django Channels.
- `jobs/` – Job listings, applications, and company profiles.
- `notifications/` – In-app and email notifications.
- `analytics/` – Engagement metrics and dashboards.
- `payments/` – Premium subscriptions, invoices, and payment webhooks.
- `search/` – Cross-domain discovery utilities and views.
- `templates/`, `static/` – Shared UI assets for server-rendered pages.

## Feature-to-Component Mapping

### 1. User Profiles & Authentication
- **Features**: Sign up/login/logout, email or OAuth auth, editable profiles (bio, experience, education, avatar), privacy controls, profile view insights.
- **Backend components**: `users.models.Profile`, `users.views`, `users.serializers`, `network.models.Connection`, `analytics.models.ProfileView`.

### 2. Feed, Posts & Engagement
- **Features**: Rich post creation (text, media links), likes/comments/shares, personalized feed, mentions & hashtags, engagement notifications.
- **Backend components**: `posts.models.Post`, `posts.models.Comment`, `posts.models.Like`, `posts.views.FeedView`, `notifications.signals`, `analytics.models.PostImpression`.

### 3. Connections & Networking
- **Features**: Send/accept/reject requests, mutual connections, “People You May Know”, alerts for accepted requests.
- **Backend components**: `network.models.Connection`, `network.views.ConnectionRequestView`, `notifications.models.Notification`, `users.serializers.ProfileSerializer`.

### 4. Messaging & Real-Time Chat
- **Features**: One-to-one and group messaging, WebSocket-powered delivery, read receipts, instant notifications.
- **Backend components**: `messaging.models.Thread`, `messaging.models.Message`, `messaging.consumers.ChatConsumer`, `messaging.routing`, `notifications.signals.message_sent`, `athena_live/asgi.py`.

### 5. Jobs & Career Tools
- **Features**: Job listings, company profiles, applying/saving/tracking applications, advanced job search, analytics for employers.
- **Backend components**: `jobs.models.Company`, `jobs.models.JobPost`, `jobs.models.Application`, `jobs.views.JobListView`, `jobs.views.ApplyView`, `search.utils.JobSearch`, `analytics.models.JobView`.

### 6. Notifications
- **Features**: Real-time alerts for messages, connections, engagement, job matches; notification center with read/unread state; in-app & email delivery.
- **Backend components**: `notifications.models.Notification`, `notifications.signals`, `notifications.views.NotificationListView`.

### 7. Search & Discovery
- **Features**: Global search across people, posts, jobs, companies; filtering by skills, location, or role; autocomplete & fuzzy matching.
- **Backend components**: `search.utils`, `search.views`, integrations with `users`, `posts`, and `jobs` querysets (optionally extended with `django-filter` or ElasticSearch).

### 8. Analytics & Insights
- **Features**: Track post impressions, profile views, job performance; dashboards with daily/weekly summaries.
- **Backend components**: `analytics.models.ProfileView`, `analytics.models.PostImpression`, `analytics.services.AnalyticsService`, `analytics.views.AnalyticsDashboardView`.

### 9. Payments & Premium
- **Features**: Premium membership tiers, boosted profiles or promoted jobs, billing history, Stripe/PayPal integration.
- **Backend components**: `payments.models.Subscription`, `payments.models.Invoice`, `payments.views.UpgradeView`, `payments.webhooks`.

## Inter-App Communication

| From app | To app | Purpose |
| --- | --- | --- |
| `posts` | `notifications` | Notify on likes, comments, and mentions. |
| `network` | `notifications` | Alert users about connection requests and acceptances. |
| `messaging` | `notifications` | Push new message alerts. |
| `jobs` | `analytics` | Capture job post performance metrics. |
| `users` | `analytics` | Track profile views and engagement. |

## Optional Extensions

- `recommendations/` – ML-driven job or connection suggestions.
- `api/` – Unified REST or GraphQL endpoints that aggregate app-level views.
- `admin_dashboard/` – Internal moderation and reporting tools for admins.

## Next Steps

- Configure environment variables for email, storage, and payment gateways.
- Build CI workflows to run tests and enforce linting.
- Add production deployment scripts (container images, ASGI server, task queue).
